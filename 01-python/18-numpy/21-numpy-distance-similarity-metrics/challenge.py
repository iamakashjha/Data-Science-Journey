import numpy as np

from implementation import (
    cosine_similarity,
    euclidean_distance,
    manhattan_distance,
    chebyshev_distance,
    pairwise_euclidean,
)


X = np.array([
    [1, 2],
    [2, 3],
    [3, 5],
    [8, 9],
])

print("Pairwise Euclidean Distance:")
print(pairwise_euclidean(X))

print("\nDistances from first observation:")
for i in range(1, len(X)):
    print(i, euclidean_distance(X[0], X[i]))

print("\nCosine Similarity:")
for i in range(1, len(X)):
    print(i, cosine_similarity(X[0], X[i]))

print("\nOther sample distances:")
print("Manhattan:", manhattan_distance(X[0], X[1]))
print("Chebyshev:", chebyshev_distance(X[0], X[1]))
