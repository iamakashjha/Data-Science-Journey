# Day 60 Exercises

## Exercise 1 — Eigenvalues

Given:

```python
A = np.array([
    [4, 0],
    [0, 7]
])
```

Find:

- eigenvalues
- eigenvectors

Then verify:

```python
Av = λv
```

for every eigenvector.

## Exercise 2 — Non-Diagonal Matrix

Use:

```python
A = np.array([
    [2, 1],
    [1, 2]
])
```

Calculate:

```python
eigenvalues, eigenvectors = np.linalg.eig(A)
```

Answer:

- What are the eigenvalues?
- What are the eigenvectors?
- Can you verify each eigenvector?

## Exercise 3 — Determinant

For:

```python
A = np.array([
    [2, 1],
    [1, 2]
])
```

calculate:

```python
np.linalg.det(A)
```

Then calculate:

```python
np.prod(np.linalg.eigvals(A))
```

Compare the results.

## Exercise 4 — SVD

Given:

```python
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
```

calculate:

```python
U, S, Vt = np.linalg.svd(A)
```

Record:

- A.shape
- U.shape
- S.shape
- Vt.shape

Then reconstruct the matrix.

## Exercise 5 — Low-Rank Approximation

Using the same matrix:

```python
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
```

Create a rank-1 approximation using only the largest singular value.

Compare:

- original matrix
- rank-1 approximation

Calculate the approximation error.
