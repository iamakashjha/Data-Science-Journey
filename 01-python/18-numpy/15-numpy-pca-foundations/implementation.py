import numpy as np


# ============================================================
# 1. CREATE DATASET
# ============================================================

X = np.array([
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 4],
    [6, 5]
])

print("Original Dataset:")
print(X)
print("\nShape:")
print(X.shape)


# ============================================================
# 2. CALCULATE MEAN
# ============================================================

mean = X.mean(axis=0)

print("\nFeature Means:")
print(mean)


# ============================================================
# 3. CENTER DATA
# ============================================================

X_centered = X - mean

print("\nCentered Data:")
print(X_centered)

print("\nCentered Means:")
print(X_centered.mean(axis=0))


# ============================================================
# 4. COVARIANCE MATRIX
# ============================================================

covariance_matrix = np.cov(X_centered, rowvar=False)

print("\nCovariance Matrix:")
print(covariance_matrix)


# ============================================================
# 5. EIGENVALUES AND EIGENVECTORS
# ============================================================

eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


# ============================================================
# 6. SORT BY EIGENVALUES
# ============================================================

indices = np.argsort(eigenvalues)[::-1]

eigenvalues = eigenvalues[indices]
eigenvectors = eigenvectors[:, indices]

print("\nSorted Eigenvalues:")
print(eigenvalues)

print("\nSorted Eigenvectors:")
print(eigenvectors)


# ============================================================
# 7. EXPLAINED VARIANCE RATIO
# ============================================================

explained_variance_ratio = eigenvalues / eigenvalues.sum()

print("\nExplained Variance Ratio:")
print(explained_variance_ratio)


# ============================================================
# 8. CUMULATIVE EXPLAINED VARIANCE
# ============================================================

cumulative_variance = np.cumsum(explained_variance_ratio)

print("\nCumulative Explained Variance:")
print(cumulative_variance)


# ============================================================
# 9. PROJECT DATA
# ============================================================

X_transformed = X_centered @ eigenvectors

print("\nPCA Transformed Data:")
print(X_transformed)


# ============================================================
# 10. PCA USING SVD
# ============================================================

U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

print("\nSVD Singular Values:")
print(S)

print("\nSVD Components:")
print(Vt)


# ============================================================
# 11. PROJECT DATA USING SVD
# ============================================================

X_svd = X_centered @ Vt.T

print("\nSVD-Based PCA Projection:")
print(X_svd)


# ============================================================
# 12. COMPARE EIGENVALUE METHOD AND SVD
# ============================================================

print("\nEigenvalue-Based PCA:")
print(X_transformed)

print("\nSVD-Based PCA:")
print(X_svd)


# ============================================================
# 13. VERIFY ORTHOGONALITY
# ============================================================

print("\nComponents Transpose × Components:")
print(eigenvectors.T @ eigenvectors)


# ============================================================
# 14. KEEP ONLY FIRST PRINCIPAL COMPONENT
# ============================================================

first_component = eigenvectors[:, :1]
X_reduced = X_centered @ first_component

print("\nOne-Dimensional PCA Representation:")
print(X_reduced)

print("\nReduced Shape:")
print(X_reduced.shape)
