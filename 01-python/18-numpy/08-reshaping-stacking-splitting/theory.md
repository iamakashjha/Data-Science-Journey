# Day 53 - NumPy Reshaping, Flattening, Stacking & Splitting

## 1. Shape is data structure

An array's shape describes how its data is arranged.

```python
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6])
print(x.shape)  # (6,)
```

The same six values can be arranged differently:

```python
y = x.reshape(2, 3)
print(y)
# [[1 2 3]
#  [4 5 6]]
```

The values are the same; only the arrangement changes.

## 2. `reshape()`

```python
x = np.arange(6)
y = x.reshape(2, 3)
print(y)
```

The total number of elements must remain the same.

```python
x.reshape(4, 2)  # invalid if x has 6 elements
```

This fails because `4 * 2 = 8`, but there are only 6 values.

### Valid examples

```python
x = np.arange(24)

x.reshape(4, 6)
x.reshape(2, 12)
x.reshape(2, 3, 4)
```

## 3. `-1` in `reshape()`

```python
x = np.arange(12)
print(x.reshape(3, -1))
print(x.reshape(-1, 3))
```

`-1` tells NumPy to infer the missing dimension automatically.

Only one dimension can be inferred this way.

## 4. Why reshape matters

Data often needs to be reorganized for models or algorithms:

- `(1000,)` -> `(1000, 1)`
- image data -> `(n_images, height, width)`
- tabular data -> `(n_samples, n_features)`

## 5. Flattening arrays

Flattening converts a multi-dimensional array into a 1D array.

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(X.flatten())
# [1 2 3 4 5 6]
```

## 6. `flatten()` vs `ravel()`

```python
X.flatten()
X.ravel()
```

Both produce a 1D view of the data, but:

- `flatten()` returns a copy
- `ravel()` usually returns a view when possible

This matters for memory use and side effects.

## 7. `transpose()` / `.T`

```python
X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(X.T)
# [[1 4]
#  [2 5]
#  [3 6]]
```

Transpose swaps rows and columns.

This is frequently useful when data is oriented the wrong way for an algorithm.

## 8. Concatenating arrays

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate([a, b])
# [1 2 3 4 5 6]
```

For 2D arrays:

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
```

### `axis=0`

```python
np.concatenate([A, B], axis=0)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
```

This adds rows.

### `axis=1`

```python
np.concatenate([A, B], axis=1)
# [[1 2 5 6]
#  [3 4 7 8]]
```

This adds columns.

## 9. `vstack()` and `hstack()`

```python
np.vstack([A, B])
# vertical stack

np.hstack([A, B])
# horizontal stack
```

`vstack` adds rows. `hstack` adds columns.

## 10. `stack()`

`stack()` creates a new axis.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.stack([a, b], axis=0)
# [[1 2 3]
#  [4 5 6]]

np.stack([a, b], axis=1)
# [[1 4]
#  [2 5]
#  [3 6]]
```

The key difference is:

- `concatenate` -> join along an existing axis
- `stack` -> create a new dimension

## 11. Splitting arrays

```python
x = np.arange(6)
print(np.split(x, 3))
# [array([0, 1]), array([2, 3]), array([4, 5])]
```

Split positions can be specified:

```python
x = np.arange(10)
print(np.split(x, [3, 7]))
# [array([0, 1, 2]), array([3, 4, 5, 6]), array([7, 8, 9])]
```

## 12. `vsplit()` and `hsplit()`

```python
X = np.arange(12).reshape(4, 3)

np.vsplit(X, 2)
np.hsplit(X, 3)
```

- `vsplit` splits along rows
- `hsplit` splits along columns

## 13. Machine learning `X` and `y`

For a dataset with features and a target:

```python
data = np.array([
    [25, 50000, 700, 1],
    [32, 65000, 720, 0],
    [41, 80000, 750, 1],
    [29, 55000, 690, 0]
])
```

Features are the first three columns:

```python
X = data[:, :3]
```

Target is the last column:

```python
y = data[:, 3]
```

Then:

- `X.shape` is `(n_samples, n_features)`
- `y.shape` is `(n_samples,)`

This is the standard shape for many supervised-learning problems.

## 14. Why shape matters in ML

The shape tells you:

- how many observations there are
- how many features each observation has
- whether a target is a vector or a column

This is critical because some ML and linear-algebra functions require exact shapes.

## 15. `(n,)` vs `(n, 1)`

```python
(4,)     # 1D vector
(4, 1)   # 2D column vector
```

These are not the same. Many algorithms expect one shape or the other, so always check `shape` carefully.

## 16. Data-science habit

When you work with arrays, always inspect shape:

```python
print(X.shape)
print(y.shape)
```

This prevents confusion between:

- rows as observations
- columns as features
- target values as 1D or 2D output

## 17. Summary

Key operations:

- `reshape()`: change structure without changing elements
- `flatten()`: make 1D copy
- `ravel()`: make 1D view when possible
- `.T`: transpose rows and columns
- `concatenate()`: join along an existing axis
- `stack()`: add a new axis
- `split()`: divide arrays into parts
- `vsplit()` and `hsplit()`: split along rows or columns

The most important idea is:

- understand the current shape
- understand the target shape
- choose the correct operation to transform between them
