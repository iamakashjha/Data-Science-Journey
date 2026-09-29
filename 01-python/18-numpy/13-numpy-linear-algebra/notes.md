# Day 59 Notes

## Important Concepts

### Scalar

Single value.

### Vector

1-D array.

### Matrix

2-D array.

### Dot Product

```python
np.dot(a, b)
```

### Matrix Multiplication

```python
A @ B
```

### Element-Wise Multiplication

```python
A * B
```

### Transpose

```python
A.T
```

### Identity Matrix

```python
np.eye(n)
```

### Determinant

```python
np.linalg.det(A)
```

### Inverse

```python
np.linalg.inv(A)
```

### Solve

```python
np.linalg.solve(A, b)
```

## Critical Rule

For:

```python
(m × n) @ (n × p)
```

result:

```python
(m × p)
```

The inner dimensions must match.

## Machine Learning Connection

```python
prediction = XW + b
```

This is based on matrix multiplication.

## Most Important Distinction

```python
A * B
```

means element-wise multiplication.

```python
A @ B
```

means matrix multiplication.
