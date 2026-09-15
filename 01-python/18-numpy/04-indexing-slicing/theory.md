# NumPy Indexing & Slicing: Key Takeaways

These are the patterns you should memorize.

## Basic Indexing

```python
arr[0]
```

- returns the first element

```python
arr[-1]
```

- returns the last element

```python
arr[start:stop]
```

- returns a range of elements

---

## 2D Array Access

```python
X[row, column]
```

- selects a specific element in a 2D array

```python
X[0, :]
```

- selects the first row

```python
X[:, 0]
```

- selects the first column

```python
X[:10]
```

- selects the first 10 rows

```python
X[:, :3]
```

- selects the first 3 columns

```python
X[2:7, 1:4]
```

- selects a subset of rows and columns

---

## Data Science Pattern

```python
X[:, feature_index]
```

This means:

- select one feature across all observations

This is one of the most important patterns in machine learning and data analysis because it allows you to isolate a variable or feature column from a dataset.

---

## Quick Rule

- `arr[i]` → single element
- `arr[start:stop]` → slice/range
- `X[row, col]` → 2D element
- `X[:, col]` → whole feature column
- `X[row_slice, col_slice]` → submatrix selection

Master these patterns and indexing will become much more intuitive.