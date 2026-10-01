# Day 66 Notes

## Core Concepts

- Euclidean distance
- Covariance
- Covariance matrix
- Inverse covariance
- Pseudoinverse
- Mahalanobis distance
- Multivariate anomaly detection
- Thresholding
- Vectorization

## Key Formula

D_M(x) = sqrt((x - μ)^T Σ^-1 (x - μ))

## NumPy

np.mean()
np.cov()
np.linalg.inv()
np.linalg.pinv()
np.linalg.norm()
np.einsum()
np.percentile()

## Important Insight

Mahalanobis distance accounts for feature relationships,
while Euclidean distance does not.

## Numerical Stability

Prefer np.linalg.pinv() when covariance may be singular
or poorly conditioned.
