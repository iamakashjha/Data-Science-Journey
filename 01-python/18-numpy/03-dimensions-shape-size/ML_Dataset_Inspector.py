import numpy as np

X = np.random.default_rng(42).random((1000, 10))

print("Dataset:")

print("Data Analysis")
print("----------------")
print("Dimensions:", X.ndim)
print("Shape:", X.shape)
print("Total elements:", X.size)
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])



feature = X[:, 0]
print("Feature 1:")
print(feature)


print("\nFeature 1 Analysis")
print("------------------")
print("Minimum value:", feature.min())
print("Maximum value:", feature.max())
print("Mean value:", feature.mean())
print("Standard deviation:", feature.std())


print("\nFeature 1 Shape:")
print(feature.shape)

feature_column = feature.reshape(-1, 1)
print("\nFeature 1 Column Shape:")
print(feature_column.shape)