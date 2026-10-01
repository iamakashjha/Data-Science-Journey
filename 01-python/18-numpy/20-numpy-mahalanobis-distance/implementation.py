import numpy as np


class MahalanobisDetector:
    """
    Multivariate anomaly detector using Mahalanobis distance.
    """

    def __init__(self, threshold=None):
        self.threshold = threshold
        self.mean_ = None
        self.covariance_ = None
        self.covariance_inv_ = None
        self.n_features_in_ = None

    def fit(self, X):
        X = np.asarray(X, dtype=float)

        if X.ndim != 2:
            raise ValueError("X must be a 2D array.")

        if X.shape[0] < 2:
            raise ValueError("At least two observations are required.")

        self.mean_ = np.mean(X, axis=0)
        self.covariance_ = np.cov(X, rowvar=False)
        self.covariance_inv_ = np.linalg.pinv(self.covariance_)
        self.n_features_in_ = X.shape[1]

        if self.threshold is None:
            train_scores = self.score_samples(X)
            self.threshold = float(np.percentile(train_scores, 95))

        return self

    def score_samples(self, X):
        if self.mean_ is None:
            raise RuntimeError("Detector must be fitted before scoring.")

        X = np.asarray(X, dtype=float)

        if X.ndim != 2:
            raise ValueError("X must be a 2D array.")

        if X.shape[1] != self.n_features_in_:
            raise ValueError("Feature count does not match training data.")

        centered = X - self.mean_

        squared_distance = np.einsum(
            "ij,jk,ik->i",
            centered,
            self.covariance_inv_,
            centered,
        )

        return np.sqrt(np.maximum(squared_distance, 0.0))

    def decision_function(self, X):
        scores = self.score_samples(X)
        return scores - self.threshold

    def predict(self, X):
        scores = self.score_samples(X)
        return scores > self.threshold
