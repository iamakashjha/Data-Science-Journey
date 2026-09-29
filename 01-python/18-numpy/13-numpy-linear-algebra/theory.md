# Day 59 — NumPy Linear Algebra

## Scalar

A single numerical value.

Example:

```python
5
```

## Vector

A one-dimensional collection of values.

```python
np.array([1, 2, 3])
```

## Matrix

A two-dimensional collection of values.

```python
np.array([
    [1, 2],
    [3, 4]
])
```

## Vector Addition

Performed element by element.

## Scalar Multiplication

Every vector element is multiplied by the scalar.

## Dot Product

For vectors:

```python
a · b = sum(a_i × b_i)
```

NumPy:

```python
np.dot(a, b)
```

or:

```python
a @ b
```

## Matrix Multiplication

```python
A @ B
```

If:

```python
A = (m × n)
B = (n × p)
```

Then:

```python
A @ B = (m × p)
```

## Element-Wise Multiplication

```python
A * B
```

## Transpose

```python
A.T
```

Rows become columns and columns become rows.

## Identity Matrix

```python
np.eye(n)
```

Identity behaves like 1 in matrix multiplication.

## Diagonal Matrix

```python
np.diag(values)
```

## Determinant

```python
np.linalg.det(A)
```

## Inverse

```python
np.linalg.inv(A)
```

Only invertible matrices have a standard inverse.

## Solve Linear System

```python
np.linalg.solve(A, b)
```

Solves:

```python
A × x = b
```

## Data Science Connection

Many Machine Learning calculations use:

```python
prediction = XW + b
```

where X, W, and b are represented using vectors and matrices.
