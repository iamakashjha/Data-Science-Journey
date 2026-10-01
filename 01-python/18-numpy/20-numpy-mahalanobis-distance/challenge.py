import numpy as np

from implementation import MahalanobisDetector

X_train = np.array([
    [10, 20],
    [11, 22],
    [12, 24],
    [13, 26],
    [14, 28],
    [15, 30],
    [16, 32],
])

X_test = np.array([
    [12, 24],
    [14, 28],
    [15, 30],
    [50, 5],
])

detector = MahalanobisDetector()
detector.fit(X_train)

scores = detector.score_samples(X_test)
predictions = detector.predict(X_test)

print("Mahalanobis Scores:")
print(scores)

print("\nPredictions:")
print(predictions)

print("\nDecision Function:")
print(detector.decision_function(X_test))
