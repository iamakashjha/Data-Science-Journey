import numpy as np

X = np.arange(100).reshape(20, 5)


print("Dataset Analysis:")
print("----------------")
print("Dimensions:", X.ndim)
print("Shape:", X.shape)
print("Total elements:", X.size)
print("Number of samples:", X.shape[0])
print("Number of features:", X.shape[1])


X_train = X[:15]
X_test = X[15:]


print("\nTraining Set Analysis:")
print("----------------")
print("Training Set:")
print(X_train)
print("\nTest Set:")
print(X_test)


print(X_train.shape)
print(X_test.shape)