# Day 60 — Eigenvalues, Eigenvectors and Matrix Decompositions

## Eigenvalue Equation

A vector v is an eigenvector of A if:

```python
A v = λ v
```

where:

- A = matrix
- v = eigenvector
- λ = eigenvalue

## NumPy

```python
eigenvalues, eigenvectors = np.linalg.eig(A)
```

Eigenvectors are stored as columns.

## Verification

```python
np.allclose(
    A @ vector,
    eigenvalue * vector
)
```

## Determinant

The determinant of a square matrix equals the product of its eigenvalues, counting algebraic multiplicity.

If:

```python
det(A) = 0
```

then at least one eigenvalue is zero.

## SVD

A matrix can be decomposed as:

```python
A = U Σ Vᵀ
```

where:

- U = left singular vectors
- Σ = singular values
- Vᵀ = transpose of right singular vectors

NumPy:

```python
U, S, Vt = np.linalg.svd(A)
```

## Reconstruction

```python
Sigma = np.diag(S)
A_reconstructed = U @ Sigma @ Vt
```

## Low-Rank Approximation

Keep only the largest singular values to create a lower-rank approximation of the original matrix.

## Orthogonality

An orthogonal matrix Q satisfies:

```python
QᵀQ = I
```

## Machine Learning Connection

Eigenvectors and eigenvalues are important in PCA.

SVD is widely used for:

- dimensionality reduction
- compression
- recommendation systems
- matrix approximation
- latent feature extraction
