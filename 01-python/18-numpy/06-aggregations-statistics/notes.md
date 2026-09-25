# Day 51 Notes

## Core NumPy aggregation functions

```python
import numpy as np

x = np.array([10, 20, 30, 40])

np.sum(x)
np.mean(x)
np.median(x)
np.min(x)
np.max(x)
np.std(x)
np.var(x)
np.argmin(x)
np.argmax(x)
```

## Axis rules

For a 2D array `X` with shape `(samples, features)`:

- `np.sum(X, axis=0)` → one result per feature
- `np.sum(X, axis=1)` → one result per sample
- `np.mean(X, axis=0)` → mean of each feature
- `np.mean(X, axis=1)` → mean of each sample

## Quick mental model

- `axis=0` collapses rows.
- `axis=1` collapses columns.

## Data-science interpretation

- mean tells you the center of the data
- median is robust to extreme values
- std/var tell you spread
- argmin/argmax tell you where the minimum and maximum occur

## Important reminder

A valid mathematical operation is not always a meaningful statistical one when features have different units. Always inspect the data and the shape before interpreting results.
