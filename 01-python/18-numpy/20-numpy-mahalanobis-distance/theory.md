# Mahalanobis Distance Theory

## Definition

Mahalanobis distance measures the distance between an observation
and a multivariate distribution while accounting for covariance.

## Formula

D_M(x) = sqrt((x - μ)^T Σ^-1 (x - μ))

## Components

- x = observation
- μ = mean vector
- Σ = covariance matrix
- Σ^-1 = inverse covariance matrix

## Squared Distance

D_M²(x) = (x - μ)^T Σ^-1 (x - μ)

## Why It Matters

Unlike Euclidean distance, Mahalanobis distance accounts for:

- feature scale
- variance
- covariance
- correlation

## Anomaly Detection

Large Mahalanobis distances can indicate observations
that are unusual relative to the learned multivariate distribution.

## Numerical Stability

When covariance matrices are singular or nearly singular,
the pseudoinverse can be used:

np.linalg.pinv()

## Important Assumption

Statistical threshold interpretations based on the chi-square
distribution generally rely on assumptions such as approximate
multivariate normality.
