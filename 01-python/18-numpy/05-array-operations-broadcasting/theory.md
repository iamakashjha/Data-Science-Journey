# Day 50 - NumPy Array Operations and Broadcasting

## 1. Element-wise operations

NumPy applies arithmetic to corresponding array elements:

```python
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

a + b  # [11 22 33]
```

Scalar arithmetic is also applied to every element:

```python
a + 5       # [15 25 35]
a - 5       # [ 5 15 25]
a * 2       # [20 40 60]
a / 10      # [1. 2. 3.]
a ** 2      # [100 400 900]
```

Array operations are concise and operate on numeric data efficiently. A complete
vectorized transformation can be written as `y = 2 * x + 10`.

## 2. Vectorization

Vectorization means operating on a whole array instead of explicitly iterating over
each value with a Python loop:

```python
values = np.array([100, 200, 300, 400])
discounted = values * 0.9
```

The expression applies a 10 percent discount to every value. NumPy can use optimized
low-level implementations for these operations.

## 3. Comparisons and Boolean masks

Comparisons return one Boolean value per element:

```python
scores = np.array([45, 67, 89, 32, 95])
mask = scores > 60
scores[mask]  # [67 89 95]
```

For multiple conditions, use parentheses with NumPy's element-wise operators:

```python
between = (scores >= 60) & (scores <= 90)
scores[between]  # [67 89]
```

Use `&`, `|`, and `~` rather than Python's `and`, `or`, and `not` for array
conditions.

## 4. Broadcasting

Broadcasting lets NumPy operate on arrays with compatible shapes without manually
copying values. A scalar is conceptually repeated across the array:

```python
X = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
X + 10
```

This produces:

```text
[[ 20  30  40]
 [ 50  60  70]
 [ 80  90 100]]
```

A one-dimensional array is broadcast across rows when its length matches the last
dimension:

```python
offset = np.array([1, 2, 3])
X + offset
# [[11 22 33]
#  [41 52 63]
#  [71 82 93]]
```

To broadcast values down columns, use a column-shaped array:

```python
column = np.array([[1], [2], [3]])
X + column
# [[11 21 31]
#  [42 52 62]
#  [73 83 93]]
```

## 5. Broadcasting rules

NumPy compares dimensions from right to left. Two dimensions are compatible when:

1. They are equal.
2. One of them is `1`.
3. One array has no dimension at that position.

Examples:

| Shapes | Compatible? | Result |
| --- | --- | --- |
| `(5, 3)` and `(3,)` | Yes | `(5, 3)` |
| `(5, 3)` and `(1, 3)` | Yes | `(5, 3)` |
| `(5, 3)` and `(5, 1)` | Yes | `(5, 3)` |
| `(5, 3)` and `(2,)` | No | Error |

For `(5, 3)` and `(2,)`, the final dimensions are `3` and `2`. They are unequal,
and neither is `1`, so the operation cannot be broadcast.

## 6. Data-science application

Suppose `X.shape` is `(10000, 20)`, where rows are observations and columns are
features. If `mean.shape` and `std.shape` are both `(20,)`, then preprocessing can
be expressed as:

```python
X_centered = X - mean
X_scaled = (X - mean) / std
```

The feature vectors are broadcast across all observations. This pattern appears in
centering, standardization, feature adjustment, and machine-learning calculations.

Always inspect `.shape` when debugging a broadcasting error. The shape tells you
which axis each value belongs to and whether the intended operation is row-wise or
column-wise.
