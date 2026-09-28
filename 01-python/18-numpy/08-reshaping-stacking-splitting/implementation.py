import numpy as np


# ---------------------------------
# 1. RESHAPE
# ---------------------------------

x = np.arange(12)
print("Original:")
print(x)

print("\nReshaped to (3, 4):")
print(x.reshape(3, 4))

print("\nReshaped with -1:")
print(x.reshape(3, -1))


# ---------------------------------
# 2. FLATTEN
# ---------------------------------

X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nFlatten:")
print(X.flatten())

print("\nRavel:")
print(X.ravel())


# ---------------------------------
# 3. TRANSPOSE
# ---------------------------------

print("\nOriginal X:")
print(X)

print("\nTranspose:")
print(X.T)


# ---------------------------------
# 4. CONCATENATE
# ---------------------------------

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("\nConcatenate axis=0:")
print(np.concatenate([A, B], axis=0))

print("\nConcatenate axis=1:")
print(np.concatenate([A, B], axis=1))


# ---------------------------------
# 5. VSTACK / HSTACK
# ---------------------------------

print("\nVertical stack:")
print(np.vstack([A, B]))

print("\nHorizontal stack:")
print(np.hstack([A, B]))


# ---------------------------------
# 6. STACK
# ---------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nStack axis=0:")
print(np.stack([a, b], axis=0))

print("\nStack axis=1:")
print(np.stack([a, b], axis=1))


# ---------------------------------
# 7. SPLIT
# ---------------------------------

numbers = np.arange(12)
parts = np.split(numbers, 3)

print("\nSplit:")
for p in parts:
    print(p)


# ---------------------------------
# 8. VSPLIT / HSPLIT
# ---------------------------------

matrix = np.arange(12).reshape(4, 3)

print("\nMatrix:")
print(matrix)

print("\nVertical split:")
print(np.vsplit(matrix, 2))

print("\nHorizontal split:")
print(np.hsplit(matrix, 3))


# ---------------------------------
# 9. MACHINE LEARNING DATA
# ---------------------------------

data = np.array([
    [25, 50000, 700, 1],
    [32, 65000, 720, 0],
    [41, 80000, 750, 1],
    [29, 55000, 690, 0]
])

X = data[:, :3]
y = data[:, 3]

print("\nFeatures X:")
print(X)

print("\nTarget y:")
print(y)

print("\nX shape:")
print(X.shape)

print("\ny shape:")
print(y.shape)
