import numpy as np


# ---------------------------------
# 1. BASIC STATISTICS
# ---------------------------------

scores = np.array([70, 80, 90, 60, 100])

print("Scores:", scores)
print("Sum:", np.sum(scores))
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Minimum:", np.min(scores))
print("Maximum:", np.max(scores))
print("Variance:", np.var(scores))
print("Standard deviation:", np.std(scores))


# ---------------------------------
# 2. RANGE
# ---------------------------------

data_range = np.max(scores) - np.min(scores)
print("Range:", data_range)


# ---------------------------------
# 3. ARGMIN / ARGMAX
# ---------------------------------

print("Index of minimum:", np.argmin(scores))
print("Index of maximum:", np.argmax(scores))


# ---------------------------------
# 4. 2D DATA
# ---------------------------------

X = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nDataset:")
print(X)

print("\nSum of columns:")
print(np.sum(X, axis=0))

print("\nSum of rows:")
print(np.sum(X, axis=1))

print("\nMean of columns:")
print(np.mean(X, axis=0))

print("\nMean of rows:")
print(np.mean(X, axis=1))

print("\nMinimum of columns:")
print(np.min(X, axis=0))

print("\nMaximum of columns:")
print(np.max(X, axis=0))

print("\nStandard deviation of columns:")
print(np.std(X, axis=0))


# ---------------------------------
# 5. KEEP DIMENSIONS
# ---------------------------------

mean = np.mean(X, axis=0, keepdims=True)
print("\nMean with keepdims:")
print(mean)
print("Shape:", mean.shape)


# ---------------------------------
# 6. DEMONSTRATE ARGMAX ON A 2D ARRAY
# ---------------------------------

Y = np.array([
    [10, 90, 30],
    [40, 50, 60],
    [70, 80, 20]
])

print("\nY:")
print(Y)
print("Global argmax:", np.argmax(Y))
print("Argmax per column:", np.argmax(Y, axis=0))
print("Argmax per row:", np.argmax(Y, axis=1))
