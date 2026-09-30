# Day 63 — PCA From Scratch

## Goal

Build PCA as a reusable component using NumPy.

## Fit/Transform Pattern

### fit()

Learns:

- feature mean
- covariance matrix
- eigenvalues
- principal components
- explained variance

### transform()

Applies learned PCA parameters to new data.

### fit_transform()

Equivalent to:

```python
fit()
transform()
```

## Reconstruction

```python
X_centered = X - mean_
X_transformed = X_centered @ components_.T

X_centered = X_transformed @ components_
X_reconstructed = X_centered + mean_
```

## Whitening

```python
X_transformed = X_transformed / np.sqrt(explained_variance_)
```

Inverse whitening:

```python
X_transformed = X_transformed * np.sqrt(explained_variance_)
```

## Data Leakage

PCA must be fitted using training data only.

Correct:

```python
X_train -> fit PCA
X_train -> transform
X_test  -> transform
```

Incorrect:

```python
X_train -> fit
X_test  -> fit
```

## Machine Learning Pipeline

```text
Raw Data
   ↓
Scaling
   ↓
PCA
   ↓
Model
```

The PCA transformation learned from training data must be reused for validation and test data.
