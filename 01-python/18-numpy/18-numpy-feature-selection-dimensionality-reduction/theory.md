# Day 64 — Feature Selection and Dimensionality Reduction

## Feature Selection

Feature selection keeps a subset of the original features.

Example:

```text
A
B
C
D
E

↓

A
C
E
```

## Feature Extraction

Feature extraction creates new features.

PCA is feature extraction.

```text
A
B
C
D
E

↓

PC1
PC2
PC3
```

## Explained Variance Ratio

Each PCA component explains some proportion of the total variance.

```python
pca.explained_variance_ratio_
```

## Cumulative Explained Variance

```python
np.cumsum(pca.explained_variance_ratio_)
```

This tells us how much variance is retained when progressively adding components.

## Component Selection

A threshold can be used:

```python
cumulative = np.cumsum(variance_ratio)

n_components = (
    np.searchsorted(cumulative, threshold)
    + 1
)
```

## Important Metrics

### Explained Variance

How much variation is retained.

### Reconstruction Error

How different the reconstructed data is from the original data.

### Compression Ratio

```python
reduced_dimensions / original_dimensions
```

### Dimensionality Reduction

```python
(1 - compression_ratio) * 100
```

## Important Warning

95% explained variance does not mean 95% prediction accuracy.

## PCA Interpretation

PCA components are combinations of original features.

Therefore PCA can reduce dimensionality while reducing interpretability.

## PCA vs Feature Selection

Feature selection keeps original variables.

PCA creates new variables.
