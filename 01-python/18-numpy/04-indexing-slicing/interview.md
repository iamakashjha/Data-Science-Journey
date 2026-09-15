# NumPy Indexing & Slicing Interview Questions

## Q1. What is NumPy indexing?

**Answer:**

Indexing is the process of selecting a specific element or position from an array.

For a 1D array:

```python
arr[2]
```

For a 2D array:

```python
arr[row, column]
```

NumPy uses zero-based indexing, so the first element is at index `0`.

---

## Q2. How do you select an entire column from a 2D NumPy array?

**Answer:**

Use:

```python
X[:, column_index]
```

For example:

```python
X[:, 2]
```

This means: select all rows and only column `2`.

This is commonly used for feature extraction in data science.

---

## Q3. What does `X[1:4, 2:5]` mean?

**Answer:**

It selects:

- rows: `1, 2, 3`
- columns: `2, 3, 4`

The stopping index is exclusive, so the slice ends before `4` and `5`.

This extracts a rectangular submatrix from the larger array.

---

## Q4. What is the difference between indexing and slicing?

**Answer:**

Indexing selects a specific element or a single position:

```python
X[2, 3]
```

Slicing selects a range of values:

```python
X[2:5, 1:4]
```

So:

- indexing → specific location
- slicing → subset or range

---

## Q5. Coding / Data Science Question

Given:

```python
import numpy as np

X = np.array([
    [25, 50000, 700],
    [30, 60000, 720],
    [35, 70000, 750]
])
```

You want to select only income and credit score.

What would you write?

**Answer:**

```python
X_selected = X[:, 1:3]
```

Result:

```python
[[50000   700]
 [60000   720]
 [70000   750]]
```

Shape:

```python
(3, 2)
```

This is a basic example of feature selection in machine learning.