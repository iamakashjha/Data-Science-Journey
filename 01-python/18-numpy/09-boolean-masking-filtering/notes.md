# Day 54 Notes

## Basic boolean filtering

```python
import numpy as np

ages = np.array([18, 22, 27, 31, 16, 40])

ages > 25
ages[ages > 25]
```

## Combined conditions

```python
mask = (ages >= 20) & (ages <= 35)
ages[mask]
```

## OR / NOT

```python
mask = (ages < 20) | (ages > 35)
ages[mask]

mask = ~(ages > 25)
ages[mask]
```

## `np.where()`

```python
scores = np.array([45, 72, 88, 55, 91])

np.where(scores >= 60, "Pass", "Fail")
np.where(scores >= 80)
```

## `np.any()` / `np.all()`

```python
np.any(scores > 90)
np.all(scores > 40)
```

## Conditional replacement

```python
scores[scores < 60] = 0
```

## Dataset filtering

```python
data = np.array([
    [25, 50000, 700],
    [32, 65000, 720],
    [41, 80000, 750],
])

mask = (data[:, 0] > 30) & (data[:, 1] > 60000)
filtered = data[mask]
```

## Important reminder

- use `&`, `|`, `~` for NumPy arrays
- use parentheses around each condition
- `mask.sum()` counts how many rows match
