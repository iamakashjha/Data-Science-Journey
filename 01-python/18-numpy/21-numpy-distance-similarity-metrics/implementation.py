import numpy as np


def euclidean_distance(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    return np.linalg.norm(x - y)


def manhattan_distance(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    return np.sum(np.abs(x - y))


def minkowski_distance(x, y, p=2):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if p <= 0:
        raise ValueError("p must be greater than 0.")

    return np.sum(np.abs(x - y) ** p) ** (1 / p)


def chebyshev_distance(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    return np.max(np.abs(x - y))


def cosine_similarity(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)

    if norm_x == 0 or norm_y == 0:
        return 0.0

    return np.dot(x, y) / (norm_x * norm_y)


def cosine_distance(x, y):
    return 1 - cosine_similarity(x, y)


def hamming_distance(x, y):
    x = np.asarray(x)
    y = np.asarray(y)

    if x.shape != y.shape:
        raise ValueError("Vectors must have the same shape.")

    return np.sum(x != y)


def pairwise_euclidean(X):
    X = np.asarray(X, dtype=float)

    squared_norms = np.sum(X ** 2, axis=1)

    distances_squared = (
        squared_norms[:, None]
        + squared_norms[None, :]
        - 2 * X @ X.T
    )

    distances_squared = np.maximum(distances_squared, 0)

    return np.sqrt(distances_squared)


def pairwise_distance(X, metric="euclidean"):
    X = np.asarray(X, dtype=float)

    if X.ndim == 1:
        X = X.reshape(1, -1)

    if metric == "euclidean":
        return pairwise_euclidean(X)

    if metric == "manhattan":
        diff = X[:, np.newaxis, :] - X[np.newaxis, :, :]
        return np.sum(np.abs(diff), axis=2)

    if metric == "chebyshev":
        diff = X[:, np.newaxis, :] - X[np.newaxis, :, :]
        return np.max(np.abs(diff), axis=2)

    if metric == "cosine":
        norms = np.linalg.norm(X, axis=1)
        similarity = np.zeros((len(X), len(X)), dtype=float)

        for i in range(len(X)):
            for j in range(len(X)):
                if norms[i] == 0 or norms[j] == 0:
                    similarity[i, j] = 0.0
                else:
                    similarity[i, j] = np.dot(X[i], X[j]) / (norms[i] * norms[j])

        return 1 - similarity

    raise ValueError(f"Unsupported metric: {metric}")


def get_nearest_neighbors(X, index, k, metric="euclidean"):
    X = np.asarray(X, dtype=float)

    if not 0 <= index < len(X):
        raise IndexError("index out of bounds")

    distances = pairwise_distance(X, metric=metric)[index]
    distances[index] = np.inf

    nearest_indices = np.argsort(distances)[:k]
    return nearest_indices


if __name__ == "__main__":
    x = np.array([1, 2, 3])
    y = np.array([4, 6, 8])

    print("Euclidean:", euclidean_distance(x, y))
    print("Manhattan:", manhattan_distance(x, y))
    print("Minkowski:", minkowski_distance(x, y, p=3))
    print("Chebyshev:", chebyshev_distance(x, y))
    print("Cosine Similarity:", cosine_similarity(x, y))
    print("Cosine Distance:", cosine_distance(x, y))

    X = np.array([
        [1, 2],
        [3, 4],
        [6, 8],
    ])

    print("\nPairwise Euclidean Matrix:")
    print(pairwise_euclidean(X))

    print("\nNearest neighbors for index 0:")
    print(get_nearest_neighbors(X, index=0, k=2))
