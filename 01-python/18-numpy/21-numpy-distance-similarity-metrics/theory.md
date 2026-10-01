# Day 67 — Distance Metrics Theory

## Euclidean Distance

Measures straight-line distance.

D(x, y) = sqrt(sum((x_i - y_i)^2))

## Manhattan Distance

Measures absolute coordinate differences.

D(x, y) = sum(|x_i - y_i|)

## Minkowski Distance

Generalized distance metric.

D(x, y) = (sum(|x_i - y_i|^p))^(1/p)

p = 1 → Manhattan
p = 2 → Euclidean

## Chebyshev Distance

Maximum coordinate difference.

D(x, y) = max(|x_i - y_i|)

## Cosine Similarity

Measures the angle between vectors.

cos(theta) = (x · y) / (||x|| ||y||)

## Hamming Distance

Counts positions where vectors differ.

## Pairwise Distance

For N observations, pairwise distances form an N × N distance matrix.

## Important Consideration

Distance-based methods are sensitive to feature scale.

Standardization may therefore be necessary before calculating distances.

## Applications

Distance metrics are used in:

- KNN
- K-Means
- DBSCAN
- clustering
- recommendation systems
- anomaly detection
- information retrieval
