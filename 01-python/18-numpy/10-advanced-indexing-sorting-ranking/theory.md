# Advanced Indexing, Sorting & Ranking

## Integer Array Indexing

Basic indexing and slicing are useful, but advanced indexing lets us select multiple arbitrary positions at once.

```python
import numpy as np

scores = np.array([72, 91, 65, 88, 95])
print(scores[0])
print(scores[2])
```

This gives:

```python
72
65
```

We can also select non-consecutive positions:

```python
scores[[0, 2, 4]]
# array([72, 65, 95])
```

This is called integer-array indexing or fancy indexing.

## `sort()` vs `argsort()`

`np.sort()` returns the sorted values.

```python
np.sort(scores)
# array([65, 72, 88, 91, 95])
```

`np.argsort()` returns the indices that would produce the sorted order.

```python
np.argsort(scores)
# array([2, 0, 3, 1, 4])
```

This is the most important distinction in this lesson:

- `sort()` → values
- `argsort()` → positions

## Why `argsort()` matters

Assume we have:

```python
names = np.array(["Akash", "Rahul", "Priya", "Neha", "Aman"])
scores = np.array([82, 95, 76, 91, 88])
```

We want to rank students by score while keeping the names attached to the scores.

```python
order = np.argsort(scores)[::-1]

print(names[order])
print(scores[order])
```

This yields the ordering in descending score rank while preserving name-score relationships.

## Descending order

By default, `np.argsort()` is ascending. To reverse it:

```python
order = np.argsort(scores)[::-1]
```

Then:

```python
scores[order]
```

returns the values in descending order.

## Top-N and bottom-N selection

```python
order = np.argsort(scores)[::-1]
top_3 = order[:3]
```

Then:

```python
scores[top_3]
```

gives the top 3 values. This is one of the most common patterns in data analysis.

## `argmax()` and `argmin()`

`np.argmax()` gives the index of the maximum value.

```python
np.argmax(scores)   # 1
```

`np.max(scores)` gives the maximum value itself.

```python
np.max(scores)      # 95
```

Similarly:

```python
np.argmin(scores)   # 2
np.min(scores)      # 65
```

The distinction is:

- `max()` → value
- `argmax()` → position
- `min()` → value
- `argmin()` → position

## Real data science example

```python
products = np.array(["Laptop", "Phone", "Tablet", "Monitor"])
sales = np.array([120, 450, 210, 180])

index = np.argmax(sales)
print(products[index])
print(sales[index])
```

This finds the product with the highest sales and retrieves the full product information.

## Advanced indexing with 2D arrays

```python
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

rows = np.array([0, 2])
print(data[rows])
```

This selects row 0 and row 2.

## Paired integer indexing

```python
rows = np.array([0, 1, 2])
cols = np.array([2, 0, 1])

data[rows, cols]
# array([30, 40, 80])
```

This pairs the row and column coordinates.

## Sorting 2D arrays

```python
marks = np.array([
    [80, 90, 70],
    [60, 85, 95],
    [75, 65, 88]
])
```

Sort each row:

```python
np.sort(marks, axis=1)
```

Sort each column:

```python
np.sort(marks, axis=0)
```

The axis determines the direction of sorting:

- `axis=0` → down the rows
- `axis=1` → across the columns

## `partition()` and `argpartition()`

`np.partition()` partially reorganizes the array around a position, which is useful when you only need the top few or bottom few values instead of a complete sort.

```python
values = np.array([91, 72, 88, 95, 65, 84, 79])
np.partition(values, 2)
```

`np.argpartition()` gives the indices that correspond to the partitioned layout.

Important idea:

- `argsort()` → complete ordering
- `argpartition()` → partial ordering around a cutoff

## Ranking data

Ranking is simply:

1. compute a metric
2. get the ordering indices with `argsort()`
3. apply those indices to related arrays
4. select top-k or bottom-k results

This pattern is extremely common in data science.

## Core data science pattern

```text
Metric
  ↓
argsort()
  ↓
indices
  ↓
reorder related arrays
  ↓
ranking / top-k selection
```

The important concept is not just sorting. The important idea is preserving the relationship between data and its attributes while ranking the rows.

