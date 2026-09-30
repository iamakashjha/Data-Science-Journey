# Day 62 Notes

## PCA Reconstruction

PCA can reduce dimensionality and then approximately reconstruct the original data.

## Transformation

```python
X_reduced = X_centered @ components
```

## Reconstruction

```python
X_centered_reconstructed = X_reduced @ components.T
X_reconstructed = X_centered_reconstructed + mean
```

## Reconstruction Error

```python
mse = np.mean((X - X_reconstructed) ** 2)
```

## Important Relationship

- More components → more information retained
- More components → lower reconstruction error

## Whitening

Whitening scales PCA components so their variances are approximately equal to one.

```python
X_white = X_reduced / np.sqrt(eigenvalues + epsilon)
```

## PCA vs Whitening

### PCA

- centers
- rotates
- produces uncorrelated components
- retains different component variances

### Whitening

- centers
- rotates
- normalizes variance
- produces approximately identity covariance

## Important

Whitening changes the scale of the PCA features. It should be used when appropriate for the downstream task.
