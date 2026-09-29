# Day 59 Exercises

## Exercise 1 — Vector Operations

Create:

```python
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
```

Calculate:

- a + b
- a - b
- a * b
- a / b
- 2 * a
- np.dot(a, b)

Explain the difference between:

```python
a * b
```

and:

```python
a @ b
```

## Exercise 2 — Matrix Multiplication

Create:

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])
```

Determine the shapes before multiplying. Then calculate:

```python
A @ B
```

What is the resulting shape?

## Exercise 3 — Transpose

Create a 3 × 4 matrix. Find:

```python
matrix.T
```

Record:

- original shape
- transposed shape

## Exercise 4 — Determinant

Create:

```python
A = np.array([
    [4, 7],
    [2, 6]
])
```

Calculate:

```python
np.linalg.det(A)
```

Then calculate its inverse. Verify:

```python
A @ inverse
```

is approximately the identity matrix.

## Exercise 5 — Linear System

Solve:

```python
3x + 2y = 12
x + 4y = 10
```

Represent it as:

```python
A × x = b
```

Then solve using:

```python
np.linalg.solve()
```

Finally substitute your answer back into the original equations to verify it.
