import numpy as np


def analyze_matrix(A):
    A = np.asarray(A)
    print("Shape:", A.shape)

    if A.ndim == 2 and A.shape[0] == A.shape[1]:
        print("Determinant:", np.linalg.det(A))
        eigenvalues, eigenvectors = np.linalg.eig(A)
        print("Eigenvalues:", eigenvalues)
        print("Eigenvectors:")
        print(eigenvectors)
    else:
        print("Matrix is not square; eigen decomposition not computed.")

    U, S, Vt = np.linalg.svd(A)
    print("Singular values:", S)

    Sigma = np.diag(S)
    A_reconstructed = U[:, :len(S)] @ Sigma @ Vt[:len(S), :]
    reconstruction_error = np.linalg.norm(A - A_reconstructed)
    print("SVD reconstruction error:", reconstruction_error)
    print("Rank:", np.linalg.matrix_rank(A))


A = np.array([
    [4, 2],
    [1, 3]
])

B = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("=== A ===")
analyze_matrix(A)
print("\n=== B ===")
analyze_matrix(B)


# Bonus PCA preview
X = np.array([
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 4],
    [6, 5]
])
X_centered = X - X.mean(axis=0)
covariance = np.cov(X_centered, rowvar=False)
print("\n=== PCA Preview ===")
print("Centered data mean:", X_centered.mean(axis=0))
print("Covariance matrix:\n", covariance)

eigenvalues, eigenvectors = np.linalg.eig(covariance)
print("Covariance eigenvalues:", eigenvalues)
print("Covariance eigenvectors:\n", eigenvectors)
