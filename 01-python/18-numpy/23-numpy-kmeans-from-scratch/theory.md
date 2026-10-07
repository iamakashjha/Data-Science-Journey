# Day 69 — K-Means Clustering Theory

## Definition
K-Means is an unsupervised learning algorithm that groups data into `k` clusters by minimizing the within-cluster sum of squared distances.

## Objective
The optimization target is:

J = sum(||x_i - mu_{c_i}||^2)

This quantity is called inertia or WCSS.

## Steps
1. Initialize `k` centroids.
2. Assign each sample to the nearest centroid.
3. Recompute each centroid as the mean of its assigned samples.
4. Repeat until convergence or max iterations.

## Assignment Step
We compute squared distances between each observation and every centroid, then choose the smallest distance.

## Update Step
Each centroid becomes the average of the observations assigned to that cluster.

## Empty Clusters
If a cluster has no assigned points, we keep the previous centroid to avoid undefined means.

## Inertia
Inertia measures how tightly observations are grouped around their centroids. Lower inertia usually means tighter clusters.

## Important Considerations
- K-Means is sensitive to initialization.
- `k` must be chosen carefully.
- Feature scaling matters because Euclidean distance depends on feature scale.
- K-Means works best for compact, roughly spherical clusters.
