import numpy as np


class PCA:
    """
    PCA implementation using NumPy.

    Parameters
    ----------
    n_components : int
        Number of principal components to retain.

    whiten : bool
        Whether to normalize the principal component
        scores to approximately unit variance.
    """

    def __init__(self, n_components=None, whiten=False):
        self.n_components = n_components
        self.whiten = whiten

        self.mean_ = None
        self.components_ = None
        self.eigenvalues_ = None
        self.explained_variance_ = None
        self.explained_variance_ratio_ = None
        self.n_features_in_ = None
        self.n_samples_ = None
        self.covariance_ = None

    def fit(self, X):
        """Learn PCA parameters from X."""
        X = np.asarray(X, dtype=float)

        if X.ndim != 2:
            raise ValueError("X must be a 2-dimensional array.")

        n_samples, n_features = X.shape

        if n_samples < 2:
            raise ValueError("PCA requires at least 2 samples.")

        if self.n_components is None:
            n_components = n_features
        else:
            if not isinstance(self.n_components, (int, np.integer)):
                raise TypeError("n_components must be an integer or None.")

            if not 1 <= self.n_components <= n_features:
                raise ValueError("n_components must be between 1 and n_features.")

            n_components = self.n_components

        self.n_features_in_ = n_features
        self.n_samples_ = n_samples
        self.mean_ = X.mean(axis=0)

        X_centered = X - self.mean_
        self.covariance_ = np.cov(X_centered, rowvar=False)

        eigenvalues, eigenvectors = np.linalg.eigh(self.covariance_)
        indices = np.argsort(eigenvalues)[::-1]
        eigenvalues = eigenvalues[indices]
        eigenvectors = eigenvectors[:, indices]

        self.eigenvalues_ = eigenvalues[:n_components]
        self.components_ = eigenvectors[:, :n_components].T
        self.explained_variance_ = self.eigenvalues_.copy()
        total_variance = eigenvalues.sum()
        self.explained_variance_ratio_ = self.explained_variance_ / total_variance

        return self

    def transform(self, X):
        """Transform X using learned PCA parameters."""
        self._check_is_fitted()
        X = self._validate_input(X)

        X_centered = X - self.mean_
        X_transformed = X_centered @ self.components_.T

        if self.whiten:
            X_transformed = X_transformed / np.sqrt(self.explained_variance_ + 1e-12)

        return X_transformed

    def fit_transform(self, X):
        """Fit PCA and transform X."""
        self.fit(X)
        return self.transform(X)

    def inverse_transform(self, X_transformed):
        """Reconstruct data from PCA representation."""
        self._check_is_fitted()

        X_transformed = np.asarray(X_transformed, dtype=float)

        if X_transformed.ndim != 2:
            raise ValueError("X_transformed must be 2-dimensional.")

        if X_transformed.shape[1] != self.components_.shape[0]:
            raise ValueError("Number of columns in X_transformed does not match n_components.")

        if self.whiten:
            X_transformed = X_transformed * np.sqrt(self.explained_variance_)

        X_centered = X_transformed @ self.components_
        return X_centered + self.mean_

    def _validate_input(self, X):
        X = np.asarray(X, dtype=float)

        if X.ndim != 2:
            raise ValueError("X must be a 2-dimensional array.")

        if X.shape[1] != self.n_features_in_:
            raise ValueError("Number of features does not match the data used during fit.")

        return X

    def _check_is_fitted(self):
        if self.mean_ is None or self.components_ is None:
            raise RuntimeError("PCA has not been fitted yet. Call fit() first.")

    def get_covariance(self):
        """Return the covariance matrix learned during fit()."""
        self._check_is_fitted()
        return self.covariance_.copy()

    def reconstruction_error(self, X):
        """Return the reconstruction MSE for the given data."""
        X = np.asarray(X, dtype=float)
        X_transformed = self.transform(X)
        X_reconstructed = self.inverse_transform(X_transformed)
        return np.mean((X - X_reconstructed) ** 2)


# ============================================================
# CREATE DATASET
# ============================================================

rng = np.random.default_rng(42)
X = rng.normal(size=(200, 6))

print("Original Shape:")
print(X.shape)


# ============================================================
# CREATE PCA MODEL
# ============================================================

pca = PCA(n_components=3)
X_reduced = pca.fit_transform(X)

print("\nReduced Shape:")
print(X_reduced.shape)

print("\nMean:")
print(pca.mean_)

print("\nComponents Shape:")
print(pca.components_.shape)

print("\nEigenvalues:")
print(pca.eigenvalues_)

print("\nExplained Variance:")
print(pca.explained_variance_)

print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nCumulative Explained Variance:")
print(np.cumsum(pca.explained_variance_ratio_))

X_reconstructed = pca.inverse_transform(X_reduced)
mse = np.mean((X - X_reconstructed) ** 2)

print("\nReconstruction MSE:")
print(mse)


# ============================================================
# TEST DATA
# ============================================================

X_test = rng.normal(size=(50, 6))
X_test_reduced = pca.transform(X_test)

print("\nTest Shape:")
print(X_test.shape)

print("\nTest Reduced Shape:")
print(X_test_reduced.shape)


# ============================================================
# WHITENED PCA
# ============================================================

pca_whitened = PCA(n_components=3, whiten=True)
X_white = pca_whitened.fit_transform(X)

print("\nWhitened Data Variance:")
print(X_white.var(axis=0))

print("\nWhitened Covariance:")
print(np.cov(X_white, rowvar=False))

X_white_reconstructed = pca_whitened.inverse_transform(X_white)
whitened_mse = np.mean((X - X_white_reconstructed) ** 2)

print("\nWhitened Reconstruction MSE:")
print(whitened_mse)
