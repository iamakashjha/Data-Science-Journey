# Day 61 Exercises

## Exercise 1 — Center the Data

Given:

```python
X = np.array([
    [10, 20],
    [20, 30],
    [30, 40],
    [40, 50]
])
```

Calculate:

```python
X.mean(axis=0)
```

Then center the data.

Verify:

```python
X_centered.mean(axis=0)
```

is approximately zero.

---

## Exercise 2 — Covariance Matrix

Using the centered data:

```python
covariance = np.cov(X_centered, rowvar=False)
```

Answer:

- What is the shape?
- What does each diagonal value represent?
- What does each off-diagonal value represent?

---

## Exercise 3 — Principal Components

Calculate:

```python
eigenvalues, eigenvectors = np.linalg.eigh(covariance)
```

Sort the eigenvalues from largest to smallest.

Then reorder the eigenvectors accordingly.

---

## Exercise 4 — Explained Variance

Calculate:

```python
explained_variance_ratio = eigenvalues / eigenvalues.sum()
```

Then:

```python
np.cumsum(explained_variance_ratio)
```

Determine how much variance is retained by:

- 1 component
- 2 components

---

## Exercise 5 — PCA Projection

Project the centered dataset:

```python
X_transformed = X_centered @ eigenvectors
```

Compare:

```python
X.shape
```

with:

```python
X_transformed.shape
```

---

## Challenge

Build a reusable function:

```python
def pca_numpy(X, n_components):
    ...
```

It should:

- calculate feature means
- center the dataset
- calculate covariance
- calculate eigenvalues/eigenvectors
- sort components
- calculate explained variance ratio
- select n_components
- transform the data
- return transformed_data, components, explained_variance_ratio

Example:

```python
X_reduced, components, variance = pca_numpy(X, n_components=2)
```

---

## Bonus Challenge — PCA from SVD

Build a function:

```python
def pca_svd(X, n_components):
    ...
```

This version should:

- center the data
- calculate SVD
- extract principal components from Vt
- calculate explained variance
- transform the data
- return the reduced representation

Then compare:

```python
pca_numpy()
vs
pca_svd()
```

The resulting component directions may differ by sign, but they should represent the same underlying principal subspaces.

---

## 5 Interview Questions

### Q1. What is PCA?
PCA is a dimensionality-reduction technique that transforms correlated features into a smaller set of orthogonal principal components ordered by the amount of variance they explain.

### Q2. Why do we center data before PCA?
Centering subtracts the mean of each feature so that the data is represented relative to its mean. This is important because PCA analyzes the covariance/variance structure of the centered data.

### Q3. What is the relationship between eigenvectors and PCA?
The eigenvectors of the covariance matrix represent the principal directions. The eigenvector associated with the largest eigenvalue corresponds to the first principal component.

### Q4. What does explained variance ratio mean?
It represents the proportion of total variance captured by each principal component.

### Q5. How can SVD be used for PCA?
After centering the dataset:

```python
U, S, Vt = np.linalg.svd(X_centered)
```

The rows of `Vt` correspond to the principal directions. The data can then be projected onto those directions.

---

## Interview Follow-Up

Why might PCA be performed after standardization instead of only centering?

Because PCA is sensitive to feature scale. If features are measured on very different scales, the larger-scale feature can dominate the covariance structure. Standardization puts features on comparable scales before PCA.
