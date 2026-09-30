import numpy as np


# ============================================================
# 1. EIGENVALUES AND EIGENVECTORS
# ============================================================

A = np.array([
    [2, 0],
    [0, 3]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)


# ============================================================
# 2. VERIFY EIGENVECTOR
# ============================================================

value = eigenvalues[0]
vector = eigenvectors[:, 0]

left_side = A @ vector
right_side = value * vector

print("\nEigenvector Verification:")
print("A @ v:")
print(left_side)

print("\nlambda * v:")
print(right_side)

print("\nValid eigenvector:")
print(np.allclose(left_side, right_side))


# ============================================================
# 3. VERIFY ALL EIGENVECTORS
# ============================================================

print("\nVerify All Eigenvectors:")

for i in range(len(eigenvalues)):
    value = eigenvalues[i]
    vector = eigenvectors[:, i]

    valid = np.allclose(A @ vector, value * vector)

    print(f"Eigenvalue {value}: {valid}")


# ============================================================
# 4. DETERMINANT AND EIGENVALUES
# ============================================================

determinant = np.linalg.det(A)

print("\nDeterminant:")
print(determinant)

print("\nProduct of Eigenvalues:")
print(np.prod(eigenvalues))


# ============================================================
# 5. SVD
# ============================================================

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

U, S, Vt = np.linalg.svd(B)

print("\nOriginal Matrix:")
print(B)

print("\nU:")
print(U)

print("\nSingular Values:")
print(S)

print("\nV Transpose:")
print(Vt)


# ============================================================
# 6. SVD SHAPES
# ============================================================

print("\nSVD Shapes:")
print("B shape:", B.shape)
print("U shape:", U.shape)
print("S shape:", S.shape)
print("Vt shape:", Vt.shape)


# ============================================================
# 7. RECONSTRUCT MATRIX
# ============================================================

Sigma = np.diag(S)
B_reconstructed = U[:, :len(S)] @ Sigma @ Vt[:len(S), :]

print("\nReconstructed Matrix:")
print(B_reconstructed)

print("\nReconstruction Successful:")
print(np.allclose(B, B_reconstructed))


# ============================================================
# 8. ORTHOGONALITY
# ============================================================

print("\nU.T @ U:")
print(U.T @ U)


# ============================================================
# 9. LOW-RANK APPROXIMATION
# ============================================================

# Keep only the largest singular value
U_reduced = U[:, :1]
S_reduced = S[:1]
Vt_reduced = Vt[:1, :]

Sigma_reduced = np.diag(S_reduced)
B_approx = U_reduced @ Sigma_reduced @ Vt_reduced

print("\nRank-1 Approximation:")
print(B_approx)

print("\nOriginal Matrix:")
print(B)

print("\nApproximation Error:")
print(np.linalg.norm(B - B_approx))
