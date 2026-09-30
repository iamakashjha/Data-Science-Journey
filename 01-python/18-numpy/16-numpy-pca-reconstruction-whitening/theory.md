# Day 62 — PCA Reconstruction and Whitening

## PCA Transformation

Given centered data:

```python
X_centered
```

and principal components:

```python
components
```

The PCA representation is:

```python
X_reduced = X_centered @ components
```

## PCA Reconstruction

Approximate centered data:

```python
X_centered_reconstructed = X_reduced @ components.T
```

Original scale:

```python
X_reconstructed = X_centered_reconstructed + mean
```

## Reconstruction Error

Mean squared error:

```python
mse = np.mean((X - X_reconstructed) ** 2)
```

Frobenius error:

```python
np.linalg.norm(X - X_reconstructed)
```

## Information Loss

If only a subset of components is retained, some information is discarded.

Generally:

- more components
- more variance retained
- lower reconstruction error

## Whitening

Whitening scales PCA scores by the inverse square root of the corresponding eigenvalues:

```python
X_white = X_reduced / np.sqrt(eigenvalues)
```

A small epsilon can be added to avoid division by zero.

## PCA

Center + Rotate

## PCA Whitening

Center + Rotate + Scale

## Covariance After Whitening

The covariance matrix of whitened PCA features is approximately the identity matrix.

Therefore:

- variance ≈ 1
- covariance ≈ 0
