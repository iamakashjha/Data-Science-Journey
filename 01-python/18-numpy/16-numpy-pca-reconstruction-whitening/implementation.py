import numpy as np


# ============================================================
# 1. CREATE DATA
# ============================================================

rng = np.random.default_rng(42)
X = rng.normal(size=(100, 5))

print("Original Shape:")
print(X.shape)


# ============================================================
# 2. FIT PCA
# ============================================================

mean = X.mean(axis=0)
X_centered = X - mean

covariance = np.cov(X_centered, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eigh(covariance)


# ============================================================
# 3. SORT COMPONENTS
# ============================================================

indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[indices]
eigenvectors = eigenvectors[:, indices]


# ============================================================
# 4. EXPLAINED VARIANCE
# ============================================================

explained_variance_ratio = eigenvalues / eigenvalues.sum()
cumulative_variance = np.cumsum(explained_variance_ratio)

print("\nExplained Variance:")
print(explained_variance_ratio)

print("\nCumulative Explained Variance:")
print(cumulative_variance)


# ============================================================
# 5. TEST DIFFERENT COMPONENT COUNTS
# ============================================================

for n_components in range(1, X.shape[1] + 1):
    components = eigenvectors[:, :n_components]

    X_reduced = X_centered @ components
    X_centered_reconstructed = X_reduced @ components.T
    X_reconstructed = X_centered_reconstructed + mean

    mse = np.mean((X - X_reconstructed) ** 2)

    print(f"\nComponents: {n_components}")
    print(f"Reduced Shape: {X_reduced.shape}")
    print(f"MSE: {mse:.6f}")


# ============================================================
# 6. FINAL REDUCTION
# ============================================================

n_components = 2
components = eigenvectors[:, :n_components]
X_reduced = X_centered @ components

print("\nReduced Dataset:")
print(X_reduced[:5])

print("\nReduced Shape:")
print(X_reduced.shape)


# ============================================================
# 7. RECONSTRUCTION
# ============================================================

X_centered_reconstructed = X_reduced @ components.T
X_reconstructed = X_centered_reconstructed + mean

print("\nOriginal First 5 Rows:")
print(X[:5])

print("\nReconstructed First 5 Rows:")
print(X_reconstructed[:5])


# ============================================================
# 8. RECONSTRUCTION ERROR
# ============================================================

mse = np.mean((X - X_reconstructed) ** 2)
frobenius_error = np.linalg.norm(X - X_reconstructed)

print("\nReconstruction MSE:")
print(mse)

print("\nFrobenius Error:")
print(frobenius_error)


# ============================================================
# 9. PCA WHITENING
# ============================================================

X_white = X_reduced / np.sqrt(eigenvalues[:n_components] + 1e-8)

print("\nWhitened Data:")
print(X_white[:5])

print("\nWhitened Variance:")
print(X_white.var(axis=0))

whitened_covariance = np.cov(X_white, rowvar=False)
print("\nWhitened Covariance:")
print(whitened_covariance)
