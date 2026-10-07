# Day 69 Notes

## Core Concepts
- unsupervised learning
- clustering
- centroids
- assignment step
- update step
- convergence
- inertia
- empty clusters
- initialization sensitivity

## NumPy Functions
- np.asarray()
- np.random.default_rng()
- np.argmin()
- np.mean()
- np.allclose()
- np.sum()
- broadcasting with newaxis

## Important Insight
K-Means does not use labels. It discovers groups by minimizing distance to cluster centers.

## Common Risks
- poor initialization
- choosing the wrong `k`
- ignoring scaling
- assuming clusters are spherical and well separated
