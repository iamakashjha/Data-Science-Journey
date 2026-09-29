import numpy as np


X = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6]
])

weights = np.array([2, 3])

predictions = X @ weights
print("Predictions with weights only:")
print(predictions)

bias = 5
predictions_with_bias = X @ weights + bias
print("\nPredictions with bias:")
print(predictions_with_bias)


def linear_prediction(X, weights, bias):
    X = np.asarray(X)
    weights = np.asarray(weights)

    if X.shape[1] != weights.shape[0]:
        raise ValueError(
            f"Feature dimension mismatch: X has {X.shape[1]} features, but weights has length {weights.shape[0]}."
        )

    return X @ weights + bias


print("\nFunction output:")
print(linear_prediction(X, weights, bias))
