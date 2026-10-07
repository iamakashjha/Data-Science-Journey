import numpy as np

__all__ = [
    "initialize_centroids",
    "calculate_distances",
    "calculate_inertia",
    "KMeans",
]


def initialize_centroids(X, n_clusters, rng):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2:
        raise ValueError("X must be a 2D array.")
    if n_clusters < 1:
        raise ValueError("n_clusters must be at least 1.")
    if n_clusters > len(X):
        raise ValueError("n_clusters cannot exceed the number of samples.")

    indices = rng.choice(len(X), size=n_clusters, replace=False)
    return X[indices].copy()


def calculate_distances(X, centroids):
    X = np.asarray(X, dtype=float)
    centroids = np.asarray(centroids, dtype=float)

    if X.ndim != 2:
        raise ValueError("X must be a 2D array.")
    if centroids.ndim != 2:
        raise ValueError("centroids must be a 2D array.")
    if X.shape[1] != centroids.shape[1]:
        raise ValueError("X and centroids must have the same number of features.")

    diff = X[:, np.newaxis, :] - centroids[np.newaxis, :, :]
    return np.sum(diff ** 2, axis=2)


def calculate_inertia(X, labels, centroids):
    X = np.asarray(X, dtype=float)
    labels = np.asarray(labels)
    centroids = np.asarray(centroids, dtype=float)

    if X.ndim != 2:
        raise ValueError("X must be a 2D array.")
    if labels.ndim != 1:
        raise ValueError("labels must be a 1D array.")
    if len(X) != len(labels):
        raise ValueError("X and labels must have the same number of rows.")
    if centroids.ndim != 2:
        raise ValueError("centroids must be a 2D array.")

    distances_squared = np.sum((X - centroids[labels]) ** 2, axis=1)
    return float(np.sum(distances_squared))


class KMeans:
    def __init__(self, n_clusters=3, max_iter=100, tol=1e-4, random_state=None, n_init=10):
        if n_clusters < 1:
            raise ValueError("n_clusters must be at least 1.")
        if max_iter < 1:
            raise ValueError("max_iter must be at least 1.")
        if tol < 0:
            raise ValueError("tol must be non-negative.")
        if n_init < 1:
            raise ValueError("n_init must be at least 1.")

        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state
        self.n_init = n_init
        self.cluster_centers_ = None
        self.labels_ = None
        self.inertia_ = None
        self.n_iter_ = None

    def _update_centroids(self, X, labels, centroids):
        new_centroids = np.zeros_like(centroids)

        for cluster_id in range(self.n_clusters):
            points = X[labels == cluster_id]
            if len(points) == 0:
                new_centroids[cluster_id] = centroids[cluster_id]
            else:
                new_centroids[cluster_id] = np.mean(points, axis=0)

        return new_centroids

    def fit(self, X):
        X = np.asarray(X, dtype=float)
        if X.ndim != 2:
            raise ValueError("X must be a 2D array.")
        if len(X) == 0:
            raise ValueError("X cannot be empty.")
        if self.n_clusters > len(X):
            raise ValueError("n_clusters cannot exceed the number of samples.")

        rng = np.random.default_rng(self.random_state)
        best_centers = None
        best_labels = None
        best_inertia = np.inf
        best_n_iter = 0

        for _ in range(self.n_init):
            centroids = initialize_centroids(X, self.n_clusters, rng)
            labels = np.zeros(len(X), dtype=int)

            for _ in range(self.max_iter):
                distances = calculate_distances(X, centroids)
                labels = np.argmin(distances, axis=1)

                new_centroids = self._update_centroids(X, labels, centroids)
                if np.allclose(centroids, new_centroids, atol=self.tol):
                    centroids = new_centroids
                    break

                centroids = new_centroids

            inertia = calculate_inertia(X, labels, centroids)
            if inertia < best_inertia:
                best_inertia = inertia
                best_centers = centroids.copy()
                best_labels = labels.copy()
                best_n_iter = self.max_iter if _ == self.max_iter - 1 else _ + 1

        self.cluster_centers_ = best_centers
        self.labels_ = best_labels
        self.inertia_ = float(best_inertia)
        self.n_iter_ = best_n_iter
        return self

    def fit_predict(self, X):
        self.fit(X)
        return self.labels_

    def predict(self, X):
        if self.cluster_centers_ is None:
            raise RuntimeError("Call fit() before predict().")

        X = np.asarray(X, dtype=float)
        if X.ndim == 1:
            X = X.reshape(1, -1)
        if X.ndim != 2:
            raise ValueError("X must be a 2D array.")

        distances = calculate_distances(X, self.cluster_centers_)
        return np.argmin(distances, axis=1)
