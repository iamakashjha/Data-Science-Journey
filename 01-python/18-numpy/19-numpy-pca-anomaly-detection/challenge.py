import importlib.util
from pathlib import Path

import numpy as np


current_dir = Path(__file__).resolve().parent
pca_path = current_dir.parent / "17-numpy-pca-from-scratch" / "implementation.py"

spec = importlib.util.spec_from_file_location("pca_day63", pca_path)
pca_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pca_module)
PCA = pca_module.PCA


class PCAAnomalyDetector:
    def __init__(self, n_components=1, percentile=99):
        self.n_components = n_components
        self.percentile = percentile
        self.threshold_ = None
        self.pca_ = None

    def fit(self, X):
        X = np.asarray(X, dtype=float)
        if X.ndim != 2:
            raise ValueError("X must be a 2D array")

        self.pca_ = PCA(n_components=self.n_components)
        self.pca_.fit(X)

        X_reduced = self.pca_.transform(X)
        X_reconstructed = self.pca_.inverse_transform(X_reduced)
        residuals = X - X_reconstructed
        scores = np.sum(residuals ** 2, axis=1)

        self.threshold_ = np.percentile(scores, self.percentile)
        return self

    def score_samples(self, X):
        if self.pca_ is None:
            raise RuntimeError("Detector must be fitted before scoring samples.")

        X = np.asarray(X, dtype=float)
        if X.ndim != 2:
            raise ValueError("X must be a 2D array")

        X_reduced = self.pca_.transform(X)
        X_reconstructed = self.pca_.inverse_transform(X_reduced)
        residuals = X - X_reconstructed
        return np.sum(residuals ** 2, axis=1)

    def decision_function(self, X):
        return self.score_samples(X) - self.threshold_

    def predict(self, X):
        return (self.score_samples(X) > self.threshold_).astype(int)


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    x = rng.normal(size=500)
    y = 2 * x + rng.normal(scale=0.2, size=500)
    X_normal = np.column_stack([x, y])

    anomalies = np.array([
        [3, -6],
        [-4, 8],
        [5, 0],
        [-5, -1],
        [0, 8],
    ])

    X = np.vstack([X_normal, anomalies])

    detector = PCAAnomalyDetector(n_components=1, percentile=99)
    detector.fit(X_normal)

    scores = detector.score_samples(X)
    predictions = detector.predict(X)

    print("Scores shape:", scores.shape)
    print("Predictions shape:", predictions.shape)
    print("Threshold:", detector.threshold_)
    print("Last anomaly flags:", predictions[-len(anomalies):])
