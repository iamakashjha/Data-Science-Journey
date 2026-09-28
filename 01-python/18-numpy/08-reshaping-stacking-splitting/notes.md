# Day 53 Notes

## Core shape operations

```python
import numpy as np

x = np.arange(12)

x.reshape(3, 4)
x.reshape(3, -1)

X = np.array([[1, 2, 3], [4, 5, 6]])
X.flatten()
X.ravel()
X.T
```

## Combining arrays

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

np.concatenate([A, B], axis=0)
np.concatenate([A, B], axis=1)
np.vstack([A, B])
np.hstack([A, B])

np.stack([A, B], axis=0)
np.stack([A, B], axis=1)
```

## Splitting arrays

```python
numbers = np.arange(12)
parts = np.split(numbers, 3)

X = np.arange(12).reshape(4, 3)
np.vsplit(X, 2)
np.hsplit(X, 3)
```

## Machine learning data

```python
data = np.array([
    [25, 50000, 700, 1],
    [32, 65000, 720, 0],
    [41, 80000, 750, 1],
])

X = data[:, :3]
y = data[:, 3]
```

## Important reminder

- `reshape` changes structure while preserving elements.
- `flatten` and `ravel` create a 1D representation.
- `stack` creates a new axis.
- `concatenate` joins along an existing axis.
- `split` divides arrays into segments.
- Always check `X.shape` and `y.shape` when building ML-ready data.
