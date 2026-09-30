# Day 60 Notes

## Eigenvector

A vector whose direction remains unchanged under a matrix transformation, apart from scaling.

## Eigenvalue

The scaling factor associated with an eigenvector.

## Core Equation

```python
A v = λ v
```

## NumPy

```python
np.linalg.eig(A)
```

Important: eigenvectors are returned as columns.
Therefore:

```python
eigenvectors[:, i]
```

corresponds to:

```python
eigenvalues[i]
```

## Numerical Verification

Use:

```python
np.allclose()
```

instead of exact equality for floating-point calculations.

## SVD

```python
A = U Σ Vᵀ
```

NumPy:

```python
U, S, Vt = np.linalg.svd(A)
```

## Singular Values

Stored in:

```python
S
```

Convert to diagonal matrix:

```python
np.diag(S)
```

## Reconstruction

```python
U @ np.diag(S) @ Vt
```

## Low-Rank Approximation

Keep the largest singular values.

## Important Difference

### Eigenvalue decomposition

- standard form applies to square matrices
- works with eigenvectors/eigenvalues

### SVD

- works with rectangular matrices
- produces U, singular values, and Vᵀ
- widely used in Data Science

## Data Science Connection

Eigenvectors and eigenvalues are central to PCA.

SVD is useful for dimensionality reduction and matrix approximation.
