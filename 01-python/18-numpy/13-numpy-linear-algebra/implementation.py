import numpy as np


# ============================================================
# 1. SCALAR
# ============================================================

scalar = 5

print("Scalar:")
print(scalar)


# ============================================================
# 2. VECTOR
# ============================================================

vector = np.array([1, 2, 3])

print("\nVector:")
print(vector)

print("Shape:", vector.shape)
print("Dimensions:", vector.ndim)


# ============================================================
# 3. MATRIX
# ============================================================

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nMatrix:")
print(matrix)

print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)


# ============================================================
# 4. VECTOR ADDITION
# ============================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nVector Addition:")
print(a + b)


# ============================================================
# 5. SCALAR MULTIPLICATION
# ============================================================

print("\nScalar Multiplication:")
print(3 * a)


# ============================================================
# 6. DOT PRODUCT
# ============================================================

dot_product = np.dot(a, b)

print("\nDot Product:")
print(dot_product)


# ============================================================
# 7. @ OPERATOR
# ============================================================

print("\n@ Operator:")
print(a @ b)


# ============================================================
# 8. MATRIX MULTIPLICATION
# ============================================================

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("\nMatrix Multiplication:")
print(A @ B)


# ============================================================
# 9. ELEMENT-WISE MULTIPLICATION
# ============================================================

print("\nElement-wise Multiplication:")
print(A * B)


# ============================================================
# 10. TRANSPOSE
# ============================================================

print("\nOriginal Matrix:")
print(matrix)

print("\nTranspose:")
print(matrix.T)


# ============================================================
# 11. IDENTITY MATRIX
# ============================================================

identity = np.eye(3)

print("\nIdentity Matrix:")
print(identity)


# ============================================================
# 12. DIAGONAL MATRIX
# ============================================================

diagonal = np.diag([2, 4, 6])

print("\nDiagonal Matrix:")
print(diagonal)


# ============================================================
# 13. DETERMINANT
# ============================================================

C = np.array([
    [1, 2],
    [3, 4]
])

determinant = np.linalg.det(C)

print("\nDeterminant:")
print(determinant)


# ============================================================
# 14. INVERSE
# ============================================================

inverse = np.linalg.inv(C)

print("\nInverse:")
print(inverse)


# ============================================================
# 15. VERIFY INVERSE
# ============================================================

print("\nC @ C_inverse:")
print(C @ inverse)


# ============================================================
# 16. SOLVE LINEAR SYSTEM
# ============================================================

A = np.array([
    [2, 1],
    [1, 3]
])

b = np.array([5, 6])

solution = np.linalg.solve(A, b)

print("\nLinear System Solution:")
print(solution)


# ============================================================
# 17. DATA SCIENCE EXAMPLE
# ============================================================

X = np.array([
    [2, 3],
    [4, 5],
    [6, 7]
])

weights = np.array([0.5, 2.0])

predictions = X @ weights

print("\nPredictions:")
print(predictions)
