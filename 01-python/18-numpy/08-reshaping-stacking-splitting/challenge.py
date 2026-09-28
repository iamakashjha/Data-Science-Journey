import numpy as np

# ---------------------------------
# 1. Feature matrix and target vector
# ---------------------------------

data = np.array([
    [25, 50000, 700, 1],
    [32, 65000, 720, 0],
    [41, 80000, 750, 1],
    [29, 55000, 690, 0],
    [35, 72000, 730, 1],
    [45, 90000, 780, 1]
])

X = data[:, :3]
y = data[:, 3]

print("X shape:", X.shape)
print("y shape:", y.shape)
print("\nX:")
print(X)
print("\ny:")
print(y)

# ---------------------------------
# 2. Add a new feature
# ---------------------------------

debt_ratio = np.array([0.30, 0.40, 0.25, 0.50, 0.35, 0.20])
X = np.column_stack([X, debt_ratio])

print("\nUpdated X shape:", X.shape)
print(X)

# ---------------------------------
# 3. Transpose
# ---------------------------------

X_T = X.T
print("\nTransposed shape:", X_T.shape)
print(X_T)

# ---------------------------------
# 4. Flatten
# ---------------------------------

X_flat = X.flatten()
print("\nFlattened size:", X_flat.size)
print(X_flat)

# ---------------------------------
# 5. Split dataset into two parts
# ---------------------------------

first, second = np.split(X, [4])
print("\nFirst 4 rows:")
print(first)

print("\nLast 2 rows:")
print(second)

# ---------------------------------
# 6. Advanced pipeline challenge
# ---------------------------------

rng = np.random.default_rng(42)

original = rng.integers(1, 100, size=(100, 5))
original_X = original[:, :4]
original_y = original[:, 4]

print("\nOriginal X shape:", original_X.shape)
print("Original y shape:", original_y.shape)

transposed_X = original_X.T
reconstructed_X = transposed_X.T

X_group_1, X_group_2 = np.split(reconstructed_X, [50])
combined_X = np.concatenate([X_group_1, X_group_2], axis=0)

print("\nReconstructed matches original:", np.array_equal(original_X, combined_X))
