# Day 61 Notes

## PCA

Principal Component Analysis reduces dimensionality while attempting to preserve important variance in the data.

## Core Idea

Find directions where the dataset has maximum variance.

## Step 1 — Center

```python
X_centered = X - X.mean(axis=0)
```

## Step 2 — Covariance

```python
covariance = np.cov(X_centered, rowvar=False)
```

## Step 3 — Eigen Decomposition

```python
eigenvalues, eigenvectors = np.linalg.eigh(covariance)
```

## Step 4 — Sort

Sort eigenvalues from largest to smallest and reorder eigenvectors accordingly.

## Step 5 — Explained Variance

```python
eigenvalues / eigenvalues.sum()
```

## Step 6 — Transform

```python
X_centered @ eigenvectors
```

## Principal Component

A principal component is a direction in the transformed feature space.

## Eigenvalue

Represents the variance associated with the corresponding principal direction.

## Important Relationship

Largest eigenvalue
↓
First principal component

Second-largest eigenvalue
↓
Second principal component

## SVD Approach

```python
U, S, Vt = np.linalg.svd(X_centered)
```

Principal directions:

```python
Vt
```

Projection:

```python
X_centered @ Vt.T
```

## Important

- PCA is sensitive to feature scale.
- Centering is fundamental.
- Standardization may also be required depending on the dataset.
