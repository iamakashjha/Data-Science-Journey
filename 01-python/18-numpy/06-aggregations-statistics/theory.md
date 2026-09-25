# Day 51 - NumPy Aggregations & Statistics

## 1. What is aggregation?

An aggregation takes multiple values and summarizes them into fewer values.

```python
import numpy as np

scores = np.array([70, 80, 90, 60, 100])

np.mean(scores)
# 80.0
```

We reduce a list like `[70, 80, 90, 60, 100]` into a single summary value such as `80`.

## 2. Sum

```python
scores = np.array([70, 80, 90, 60, 100])

total = np.sum(scores)
print(total)  # 400
```

You can also write `scores.sum()`.

## 3. Mean

The mean is the arithmetic average.

```python
print(np.mean(scores))
# 80.0
```

Mathematically:

$$
\frac{70 + 80 + 90 + 60 + 100}{5} = 80
$$

## 4. Median

The median is the middle value after sorting.

```python
scores = np.array([70, 80, 90, 60, 100])
print(np.median(scores))  # 80.0
```

The median is less sensitive to outliers than the mean.

```python
income = np.array([30000, 35000, 40000, 45000, 1000000])
print(np.mean(income))
print(np.median(income))
```

The mean is strongly affected by the extreme value `1000000`, while the median is not.

## 5. Minimum and maximum

```python
print(np.min(scores))  # 60
print(np.max(scores))  # 100
```

Or:

```python
print(scores.min())
print(scores.max())
```

## 6. Range

NumPy does not have a built-in `range` statistic, but you can compute it directly:

```python
data_range = np.max(scores) - np.min(scores)
print(data_range)  # 40
```

## 7. Variance and standard deviation

Variance measures how spread out values are around the mean.

```python
print(np.var(scores))
# 200.0
```

Standard deviation is the square root of variance:

```python
print(np.std(scores))
# 14.14...
```

Standard deviation is often easier to interpret because it uses the same units as the original data.

## 8. Why standard deviation matters

```python
a = np.array([49, 50, 51, 50, 50])
b = np.array([10, 30, 50, 70, 90])

print(np.mean(a), np.std(a))
print(np.mean(b), np.std(b))
```

Both arrays have mean `50`, but `b` is much more spread out.

## 9. The important concept: axis

Consider:

```python
X = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

This matrix has shape `(3, 3)`.

### axis=0

```python
np.sum(X, axis=0)
# array([120, 150, 180])
```

This sums down the rows for each column:

- `10 + 40 + 70 = 120`
- `20 + 50 + 80 = 150`
- `30 + 60 + 90 = 180`

Interpretation: one value per column.

### axis=1

```python
np.sum(X, axis=1)
# array([ 60, 150, 240])
```

This sums across each row:

- `10 + 20 + 30 = 60`
- `40 + 50 + 60 = 150`
- `70 + 80 + 90 = 240`

Interpretation: one value per row.

## 10. Mental model for axis

A useful rule is:

- `axis=0` collapses rows and keeps one result for each column.
- `axis=1` collapses columns and keeps one result for each row.

For tabular data:

- rows = observations
- columns = features

Then:

- `np.mean(X, axis=0)` gives one statistic per feature.
- `np.mean(X, axis=1)` gives one statistic per observation.

## 11. Mean by feature

```python
X = np.array([
    [20, 50000, 700],
    [30, 60000, 720],
    [40, 70000, 740],
    [50, 80000, 760]
])

np.mean(X, axis=0)
# array([ 3.5000e+01, 6.5000e+04, 7.3000e+02])
```

This gives:

- average age = 35
- average income = 65000
- average credit score = 730

## 12. Mean per observation

```python
np.mean(X, axis=1)
```

This produces one average per row, but it may not be meaningful if the columns have different units. A mathematically valid average is not always a statistically meaningful one.

## 13. Min and max by feature

```python
np.min(X, axis=0)
np.max(X, axis=0)
```

This shows the smallest and largest values for each feature.

## 14. Standard deviation by feature

```python
np.std(X, axis=0)
```

This tells us how spread out each feature is individually.

## 15. `argmin()` and `argmax()`

Sometimes we want the position of an extreme value rather than the value itself.

```python
scores = np.array([70, 80, 55, 90, 65])

print(np.argmin(scores))  # 2
print(np.argmax(scores))  # 3
```

`np.argmin` returns the index of the minimum value. `np.argmax` returns the index of the maximum value.

With 2D arrays:

```python
X = np.array([
    [10, 90, 30],
    [40, 50, 60],
    [70, 80, 20]
])

print(np.argmax(X))
print(np.argmax(X, axis=0))
print(np.argmax(X, axis=1))
```

By default, `np.argmax(X)` uses a flattened index. `axis=0` and `axis=1` are more useful for row-wise and column-wise maxima.

## 16. `keepdims=True`

```python
X.mean(axis=0)
# shape: (3,)

X.mean(axis=0, keepdims=True)
# shape: (1, 3)
```

This preserves dimensions, which is useful in numerical computing and broadcasting.

```python
mean = X.mean(axis=0, keepdims=True)
X_centered = X - mean
```

## 17. Real data-science example

```python
X = np.array([
    [25, 50000, 700],
    [32, 65000, 720],
    [41, 80000, 750],
    [29, 55000, 690],
    [35, 72000, 730]
])

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)
minimum = np.min(X, axis=0)
maximum = np.max(X, axis=0)
```

This produces a statistical summary of each feature and is an essential part of exploratory data analysis (EDA).

## 18. Data shape and axis choice

If `X.shape = (1000, 20)`, then:

- `np.mean(X, axis=0)` returns `20` values, one for each feature.
- `np.mean(X, axis=1)` returns `1000` values, one for each observation.

This is a key habit for data science: always check the shape of the array before applying an aggregation.

## 19. Summary

For `X.shape = (samples, features)`:

- `axis=0` → feature-wise statistics
- `axis=1` → observation-wise statistics

This distinction is important for Pandas, feature engineering, preprocessing, and machine learning.
