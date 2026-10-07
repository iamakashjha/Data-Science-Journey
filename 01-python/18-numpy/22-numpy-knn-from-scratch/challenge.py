import numpy as np

from implementation import KNNClassifier, accuracy_score

X_train = np.array([
    [1.0, 1.0],
    [1.5, 2.0],
    [2.0, 1.5],
    [6.0, 6.0],
    [6.5, 7.0],
    [7.0, 6.5],
])
y_train = np.array(["A", "A", "A", "B", "B", "B"])
X_test = np.array([
    [1.8, 1.7],
    [6.2, 6.4],
])
y_test = np.array(["A", "B"])

model = KNNClassifier(k=3)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Accuracy:", accuracy_score(y_test, predictions))
