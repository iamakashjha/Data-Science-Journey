import numpy as np


class PCA:
    def __init__(self, n_components=None, whiten=False):
        self.n_components = n_components
        self.whiten = whiten

    def fit(self, X):
        X = np.asarray(X, dtype=float)

        if X.ndim != 2:
            raise ValueError("X must be a 2D array")

        self.mean_ = X.mean(axis=0)
        X_centered = X - self.mean_

        covariance = np.cov(X_centered, rowvar=False)
        eigenvalues, eigenvectors = np.linalg.eigh(covariance)

        indices = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[indices]
        eigenvectors = eigenvectors[:, indices]

        if self.n_components is None:
            n_components = X.shape[1]
        else:
            n_components = min(self.n_components, X.shape[1])

        self.components_ = eigenvectors[:, :n_components]
        self.eigenvalues_ = eigenvalues[:n_components]
        self.explained_variance_ratio_ = self.eigenvalues_ / eigenvalues.sum()

        return self

    def transform(self, X):
        X = np.asarray(X, dtype=float)
        X_centered = X - self.mean_
        X_reduced = X_centered @ self.components_

        if self.whiten:
            X_reduced = X_reduced / np.sqrt(self.eigenvalues_ + 1e-8)

        return X_reduced

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

    def inverse_transform(self, X_reduced):
        X_reduced = np.asarray(X_reduced, dtype=float)

        if self.whiten:
            X_reduced = X_reduced * np.sqrt(self.eigenvalues_ + 1e-8)

        X_centered_reconstructed = X_reduced @ self.components_.T
        return X_centered_reconstructed + self.mean_


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    X = rng.normal(size=(100, 5))

    pca = PCA(n_components=2)
    X_reduced = pca.fit_transform(X)
    X_reconstructed = pca.inverse_transform(X_reduced)

    mse = np.mean((X - X_reconstructed) ** 2)
    print("Reduced shape:", X_reduced.shape)
    print("Reconstruction MSE:", mse)

    pca_white = PCA(n_components=2, whiten=True)
    X_white = pca_white.fit_transform(X)
    print("Whitened shape:", X_white.shape)
    print("Whitened variance:", X_white.var(axis=0))
