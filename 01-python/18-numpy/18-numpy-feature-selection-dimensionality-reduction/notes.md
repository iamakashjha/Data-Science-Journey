# Day 64 Notes

## Main Concept

Today I learned how to choose the number of PCA components instead of selecting the number arbitrarily.

## Cumulative Variance

```python
np.cumsum(pca.explained_variance_ratio_)
```

## Threshold-Based Selection

```python
np.searchsorted(cumulative_variance, threshold) + 1
```

## Important Concepts

Feature selection:

- keeps original features

Feature extraction:

- creates new features

PCA:

- feature extraction
- unsupervised
- creates principal components

## Important Metrics

- explained variance
- cumulative explained variance
- reconstruction error
- compression ratio
- dimensionality reduction

## Important Warning

Explained variance is not model accuracy.

## PCA Loadings

```python
pca.components_
```

The values indicate how original features contribute to principal components.

## Interpretation Warning

High loading does not mean high predictive importance because PCA is not optimizing a target variable.

## Workflow

```text
Dataset
   ↓
Fit PCA
   ↓
Explained Variance
   ↓
Cumulative Variance
   ↓
Choose Threshold
   ↓
Select Components
   ↓
Transform
   ↓
Measure Compression
   ↓
Measure Reconstruction Error
```
