import numpy as np


def select_components(explained_variance_ratio, threshold):
    """Return the minimum number of components needed to exceed a variance threshold."""
    if not 0 < threshold <= 1:
        raise ValueError("threshold must be in the range (0, 1]")

    explained_variance_ratio = np.asarray(explained_variance_ratio, dtype=float)
    cumulative_variance = np.cumsum(explained_variance_ratio)

    n_components = np.searchsorted(cumulative_variance, threshold) + 1
    return int(n_components)


def pca_summary(pca):
    """Return a simple summary of PCA component statistics."""
    if pca.explained_variance_ratio_ is None:
        raise ValueError("PCA has not been fitted")

    cumulative = np.cumsum(pca.explained_variance_ratio_)
    summary = []

    for i, (variance, ratio, cum) in enumerate(
        zip(pca.explained_variance_, pca.explained_variance_ratio_, cumulative),
        start=1,
    ):
        summary.append((i, variance, ratio, cum))

    return summary


if __name__ == "__main__":
    variance_ratio = np.array([0.45, 0.25, 0.15, 0.10, 0.05])
    print("Selected components for 90% variance:", select_components(variance_ratio, 0.90))

    rng = np.random.default_rng(42)
    X = rng.normal(size=(500, 6))
    centered = X - X.mean(axis=0)
    covariance = np.cov(centered, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)
    eigenvalues = eigenvalues[::-1]
    eigenvectors = eigenvectors[:, ::-1]
    ratio = eigenvalues / eigenvalues.sum()

    print("Variance ratio:", ratio)
    print("Cumulative variance:", np.cumsum(ratio))
    print("Automatic selection at 95%:", select_components(ratio, 0.95))
