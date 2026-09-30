import numpy as np


def pca_numpy(X, n_components):
    """Compute PCA using covariance matrix + eigen decomposition."""
    X = np.asarray(X, dtype=float)

    if X.ndim != 2:
        raise ValueError("X must be a 2D array")

    if not 1 <= n_components <= X.shape[1]:
        raise ValueError("n_components must be between 1 and the number of features")

    mean = X.mean(axis=0)
    X_centered = X - mean

    covariance_matrix = np.cov(X_centered, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[indices]
    eigenvectors = eigenvectors[:, indices]

    explained_variance_ratio = eigenvalues / eigenvalues.sum()
    components = eigenvectors[:, :n_components]
    transformed_data = X_centered @ components

    return transformed_data, components, explained_variance_ratio[:n_components]


def pca_svd(X, n_components):
    """Compute PCA using SVD on centered data."""
    X = np.asarray(X, dtype=float)

    if X.ndim != 2:
        raise ValueError("X must be a 2D array")

    if not 1 <= n_components <= X.shape[1]:
        raise ValueError("n_components must be between 1 and the number of features")

    mean = X.mean(axis=0)
    X_centered = X - mean

    U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
    components = Vt[:n_components, :].T
    transformed_data = X_centered @ components
    explained_variance_ratio = (S ** 2) / np.sum(S ** 2)

    return transformed_data, components, explained_variance_ratio[:n_components]


if __name__ == "__main__":
    X = np.array([
        [2, 1],
        [3, 2],
        [4, 3],
        [5, 4],
        [6, 5]
    ])

    X_reduced, components, variance = pca_numpy(X, n_components=2)
    print("Eigen-based PCA:")
    print(X_reduced)
    print("Components:")
    print(components)
    print("Explained variance:")
    print(variance)

    X_reduced_svd, components_svd, variance_svd = pca_svd(X, n_components=2)
    print("\nSVD-based PCA:")
    print(X_reduced_svd)
    print("Components:")
    print(components_svd)
    print("Explained variance:")
    print(variance_svd)
