# Day 61 — PCA Foundations

## Principal Component Analysis

PCA is a dimensionality-reduction technique.

It transforms the original features into a new set of orthogonal directions called principal components.

## Main Idea

PC1 captures the greatest variance.

PC2 captures the greatest remaining variance while being orthogonal to PC1.

## PCA Workflow

Original Data
    ↓
Center Data
    ↓
Covariance Matrix
    ↓
Eigenvalues + Eigenvectors
    ↓
Sort Components
    ↓
Select Components
    ↓
Project Data

## Centering

```python
X_centered = X - X.mean(axis=0)
```

## Covariance

```python
covariance = np.cov(X_centered, rowvar=False)
```

## Eigen Decomposition

```python
eigenvalues, eigenvectors = np.linalg.eigh(covariance)
```

For covariance matrices, `eigh()` is appropriate because the covariance matrix is symmetric.

## Principal Components

Eigenvectors of the covariance matrix represent principal directions.

The largest eigenvalue corresponds to the first principal component.

## Explained Variance

```python
explained_variance_ratio = eigenvalues / eigenvalues.sum()
```

## Cumulative Variance

```python
np.cumsum(explained_variance_ratio)
```

## Projection

```python
X_transformed = X_centered @ eigenvectors
```

## SVD-Based PCA

```python
U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)
```

The rows of `Vt` contain the principal directions.

## PCA and SVD

PCA can be computed using either:

- covariance matrix + eigen decomposition
- centered data + SVD

SVD is often numerically preferable.

## Scaling

PCA is sensitive to feature scale.

Depending on the problem, features may need to be standardized before PCA.

## Data Science Applications

- dimensionality reduction
- visualization
- feature extraction
- noise reduction
- preprocessing
- exploratory data analysis
