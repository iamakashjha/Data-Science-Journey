# Day 50 Quick Notes

## Core ideas

- Element-wise operation: corresponding array elements are combined.
- Vectorization: apply an operation to a whole array without a Python loop.
- Broadcasting: operate on compatible arrays with different shapes.
- Boolean mask: a Boolean array used to select matching values.

## Common patterns

```python
x * 2
sales - costs
scores[scores > 60]
(scores >= 60) & (scores <= 90)
X + np.array([1, 2, 3])
X + np.array([[1], [2], [3]])
```

## Shape checklist

1. Compare dimensions from the rightmost side.
2. Dimensions must match, or one must be `1`, or be missing.
3. A shape such as `(rows, features)` usually works with a feature vector of
   shape `(features,)`.
4. Use `.reshape(-1, 1)` when values should be broadcast down columns.

## Important warning

Use `&`, `|`, and `~` for NumPy Boolean logic, and parenthesize each comparison.
Do not use `and`, `or`, or `not` with NumPy arrays.
