# Notes - NumPy Advanced Indexing, Sorting & Ranking

## Quick reference

```python
# Integer-array indexing
x[[4, 1, 3]]

# Sort values
np.sort(x)

# Sorting indices
np.argsort(x)

# Descending
np.argsort(x)[::-1]

# Maximum value
np.max(x)

# Maximum index
np.argmax(x)

# Minimum value
np.min(x)

# Minimum index
np.argmin(x)

# Top N values
order = np.argsort(x)[::-1]
x[order[:N]]

# Top N rows by a column
order = np.argsort(X[:, col])[::-1]
X[order[:N]]

# Bottom N rows
order = np.argsort(X[:, col])
X[order[:N]]

# Partial ordering
np.partition(x, k)

# Indices for partial ordering
np.argpartition(x, k)
```

## Key ideas

- `sort()` returns sorted values.
- `argsort()` returns the positions that produce the sorted order.
- `argmax()` returns the position of the largest value.
- `argmin()` returns the position of the smallest value.
- Integer indexing is useful when exact positions are known.
- `argsort()` is often more useful than `sort()` because it preserves row relationships.
- `partition()` and `argpartition()` are useful when you only need a cutoff rather than complete ordering.

## Mental model

Metric → Sort/Rank → Select

## Axis reminder

- `axis=0` → down rows, column-wise
- `axis=1` → across columns, row-wise

## Common patterns

### Find the highest-value row

```python
idx = np.argmax(X[:, col])
row = X[idx]
```

### Find the top 3 rows

```python
order = np.argsort(X[:, col])[::-1]
top_3 = X[order[:3]]
```

### Keep related arrays aligned

```python
order = np.argsort(revenue)[::-1]
customer_ids = customer_ids[order]
revenue = revenue[order]
orders = orders[order]
```
