import numpy as np

__all__ = [
    "euclidean_distance",
    "get_neighbors",
    "majority_vote",
    "KNNClassifier",
    "KNNRegressor",
    "accuracy_score",
    "confusion_matrix",
]


X_train = np.array([
    [1.0, 1.0],
    [1.5, 2.0],
    [2.0, 1.5],
    [6.0, 6.0],
    [6.5, 7.0],
    [7.0, 6.5],
])

y_train = np.array([
    "A", "A", "A",
    "B", "B", "B",
])

X_test = np.array([
    [1.8, 1.7],
    [6.2, 6.4],
])


def euclidean_distance(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.shape != y.shape:
        raise ValueError("x and y must have the same shape.")

    return np.sqrt(np.sum((x - y) ** 2))


def get_neighbors(X_train, x, k=3):
    X_train = np.asarray(X_train, dtype=float)
    x = np.asarray(x, dtype=float)

    if X_train.ndim != 2:
        raise ValueError("X_train must be a 2D array.")
    if x.ndim != 1:
        raise ValueError("x must be a 1D array.")
    if X_train.shape[1] != x.shape[0]:
        raise ValueError("Feature dimensions of X_train and x must match.")
    if k < 1:
        raise ValueError("k must be at least 1.")
    if k > len(X_train):
        raise ValueError("k cannot exceed the number of training samples.")

    distances = np.sqrt(np.sum((X_train - x) ** 2, axis=1))
    nearest_indices = np.argsort(distances)[:k]
    return nearest_indices, distances[nearest_indices]


def majority_vote(labels):
    labels = np.asarray(labels)
    if labels.size == 0:
        raise ValueError("labels cannot be empty.")

    values, counts = np.unique(labels, return_counts=True)
    return values[np.argmax(counts)]


class KNNClassifier:
    def __init__(self, k=3):
        if k < 1:
            raise ValueError("k must be at least 1.")
        self.k = k
        self.X_train = None
        self.y_train = None
        self.classes_ = None

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y)

        if X.ndim != 2:
            raise ValueError("X must be a 2D array.")
        if y.ndim != 1:
            raise ValueError("y must be a 1D array.")
        if len(X) != len(y):
            raise ValueError("X and y must have the same number of rows.")
        if len(X) == 0:
            raise ValueError("Training data cannot be empty.")
        if self.k > len(X):
            raise ValueError("k cannot exceed the number of training samples.")
        if not np.all(np.isfinite(X)):
            raise ValueError("X must contain only finite values.")

        self.X_train = X.copy()
        self.y_train = y.copy()
        self.classes_ = np.unique(y)
        return self

    def predict(self, X):
        if self.X_train is None or self.y_train is None:
            raise RuntimeError("Call fit() before predict().")

        X = np.asarray(X, dtype=float)
        if X.ndim == 1:
            X = X.reshape(1, -1)
        if X.ndim != 2:
            raise ValueError("X must be a 2D array.")

        predictions = []
        for sample in X:
            distances = np.sqrt(np.sum((self.X_train - sample) ** 2, axis=1))
            nearest_indices = np.argsort(distances)[: self.k]
            neighbor_labels = self.y_train[nearest_indices]
            predictions.append(majority_vote(neighbor_labels))

        return np.asarray(predictions)


class KNNRegressor:
    def __init__(self, k=3):
        if k < 1:
            raise ValueError("k must be at least 1.")
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)

        if X.ndim != 2 or y.ndim != 1:
            raise ValueError("Invalid X or y dimensions.")
        if len(X) != len(y) or len(X) == 0:
            raise ValueError("Invalid training data lengths.")
        if self.k > len(X):
            raise ValueError("k exceeds training sample count.")
        if not np.all(np.isfinite(X)):
            raise ValueError("X must contain finite values.")
        if not np.all(np.isfinite(y)):
            raise ValueError("y must contain finite values.")

        self.X_train = X.copy()
        self.y_train = y.copy()
        return self

    def predict(self, X):
        if self.X_train is None:
            raise RuntimeError("Call fit() before predict().")

        X = np.asarray(X, dtype=float)
        if X.ndim == 1:
            X = X.reshape(1, -1)
        if X.ndim != 2:
            raise ValueError("X must be a 2D array.")

        predictions = []
        for sample in X:
            distances = np.sqrt(np.sum((self.X_train - sample) ** 2, axis=1))
            nearest_indices = np.argsort(distances)[: self.k]
            predictions.append(np.mean(self.y_train[nearest_indices]))

        return np.asarray(predictions)


def accuracy_score(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.shape != y_pred.shape:
        raise ValueError("Shapes must match.")
    if y_true.size == 0:
        raise ValueError("Inputs cannot be empty.")

    return np.mean(y_true == y_pred)


def confusion_matrix(y_true, y_pred, labels=None):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    if y_true.ndim != 1 or y_pred.ndim != 1:
        raise ValueError("Inputs must be 1D arrays.")
    if y_true.shape != y_pred.shape:
        raise ValueError("Shapes must match.")
    if y_true.size == 0:
        raise ValueError("Inputs cannot be empty.")

    if labels is None:
        labels = np.unique(np.concatenate((y_true, y_pred)))
    else:
        labels = np.asarray(labels)

    label_to_index = {label: i for i, label in enumerate(labels)}
    matrix = np.zeros((len(labels), len(labels)), dtype=int)

    for actual, predicted in zip(y_true, y_pred):
        if actual not in label_to_index:
            raise ValueError("Unknown actual label.")
        if predicted not in label_to_index:
            raise ValueError("Unknown predicted label.")
        row = label_to_index[actual]
        col = label_to_index[predicted]
        matrix[row, col] += 1

    return matrix


if __name__ == "__main__":
    x = np.array([1.0, 2.0])
    y = np.array([4.0, 6.0])
    print("Euclidean distance:", euclidean_distance(x, y))

    indices, distances = get_neighbors(X_train, X_test[0], k=3)
    print("Neighbor indices:", indices)
    print("Neighbor distances:", distances)
    print("Neighbor labels:", y_train[indices])

    labels = np.array(["A", "B", "A"])
    print("Majority vote:", majority_vote(labels))

    model = KNNClassifier(k=3)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Predictions:", predictions)

    regressor = KNNRegressor(k=3)
    X = np.array([[1], [2], [3], [4], [5]], dtype=float)
    y_values = np.array([10, 20, 30, 40, 50], dtype=float)
    regressor.fit(X, y_values)
    print("Regression predictions:", regressor.predict(np.array([[2.5], [4.5]])))

    y_true = np.array(["A", "B", "B", "A"])
    y_pred = np.array(["A", "B", "A", "A"])
    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Confusion matrix:\n", confusion_matrix(y_true, y_pred))