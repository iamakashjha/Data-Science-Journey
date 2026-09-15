# Day 49 — NumPy Indexing & Slicing

Welcome to Day 49 of your Data Science journey.

By this point, you already know how to create arrays and understand their dimensions, shape, and size. Today, we will focus on how to access and manipulate data inside arrays.

This skill is essential for:

- selecting features
- selecting observations
- filtering datasets
- preparing `X` and `y`
- feature engineering
- image data
- time-series data
- machine learning pipelines

---

## Learning Objectives

By the end of this lesson, you should be able to:

- access individual NumPy elements
- understand zero-based indexing
- index 1D arrays
- index 2D arrays
- select rows and columns
- select individual cells
- slice arrays
- use `start:stop:step`
- slice rows and columns simultaneously
- understand negative indexing
- work with 3D arrays
- apply indexing to machine learning datasets

---

## 1. What Is Indexing?

Indexing means selecting a specific element from an array.

NumPy uses zero-based indexing, which means:

- first element → index `0`
- second element → index `1`
- third element → index `2`

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
```

The positions look like this:

```text
Index:   0   1   2   3   4
Value:  10  20  30  40  50
```

---

## 2. 1D Array Indexing

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
print(arr[2])
print(arr[4])
```

Output:

```python
10
30
50
```

This returns the first, third, and last elements.

---

## 3. Negative Indexing

Negative indexing counts from the end of the array.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[-1])
print(arr[-2])
```

Output:

```python
50
40
```

This is useful when you want to access the last element without knowing the array length.

---

## 4. 2D Array Indexing

Consider this array:

```python
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
```

Think of it like this:

```text
        Column
        0   1   2

Row 0   10  20  30
Row 1   40  50  60
Row 2   70  80  90
```

To access an element, use:

```python
data[row, column]
```

---

## 5. Selecting Individual Elements

```python
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[0, 0])
print(data[1, 2])
print(data[2, 1])
```

Output:

```python
10
60
80
```

The general pattern is:

```python
array[row, column]
```

---

## 6. Selecting an Entire Row

```python
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[0])
print(data[1])
print(data[2])
```

Output:

```python
[10 20 30]
[40 50 60]
[70 80 90]
```

You can also write:

```python
print(data[0, :])
```

The `:` means "select everything along this dimension." So:

```python
data[0]
```

and:

```python
data[0, :]
```

both select the first row.

---

## 7. Selecting an Entire Column

This is especially important in data science.

```python
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[:, 0])
print(data[:, 1])
print(data[:, 2])
```

Output:

```python
[10 40 70]
[20 50 80]
[30 60 90]
```

`data[:, 0]` means:

- all rows
- column `0`

---

## 8. The Most Important Pattern

For a 2D NumPy array, the format is:

```python
array[rows, columns]
```

Examples:

```python
data[0, 1]   # row 0, column 1
data[2, :]   # row 2, all columns
data[:, 1]   # all rows, column 1
data[:, :]   # all rows, all columns
```

This indexing pattern becomes second nature with practice.

---

## 9. Slicing

Indexing selects a specific element, while slicing selects a range of elements.

The basic syntax is:

```python
array[start:stop]
```

Important: `stop` is exclusive.

Example:

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])
```

Output:

```python
[20 30 40]
```

This includes indices `1`, `2`, and `3`.

---

## 10. Slicing from the Beginning

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[:3])
```

Output:

```python
[10 20 30]
```

This means: start at the beginning and stop before index `3`.

---

## 11. Slicing to the End

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[2:])
```

Output:

```python
[30 40 50]
```

This means: start at index `2` and continue to the end.

---

## 12. Copying the Whole Array with Slicing

```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[:])
```

Output:

```python
[10 20 30 40 50]
```

This selects the entire array.

---

## 13. Step in Slicing

The full syntax is:

```python
array[start:stop:step]
```

Example:

```python
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[::2])
print(arr[::3])
```

Output:

```python
[0 2 4 6 8]
[0 3 6 9]
```

This selects every second or third element.

---

## 14. Reversing an Array

```python
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[::-1])
```

Output:

```python
[9 8 7 6 5 4 3 2 1 0]
```

This works because the step is `-1`, which moves backward through the array.

---

## 15. 2D Array Slicing

Consider:

```python
import numpy as np

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print(data.shape)
```

Output:

```python
(4, 4)
```

---

## 16. Selecting Multiple Rows

```python
print(data[:2])
print(data[1:3])
```

Output:

```python
[[10 20 30 40]
 [50 60 70 80]]

[[50 60 70 80]
 [90 100 110 120]]
```

This selects a range of rows.

---

## 17. Selecting Multiple Columns

```python
print(data[:, :2])
```

Output:

```python
[[ 10  20]
 [ 50  60]
 [ 90 100]
 [130 140]]
```

This means:

- all rows
- first two columns

---

## 18. Selecting a Submatrix

This is especially useful in data analysis.

```python
print(data[1:3, 1:3])
```

Output:

```python
[[ 60  70]
 [100 110]]
```

This selects:

- rows `1` to `2`
- columns `1` to `2`

The pattern is:

```python
data[row_slice, column_slice]
```

---

## 19. Data Science Connection

Now let’s apply this to a realistic dataset:

```python
import numpy as np

X = np.array([
    [25, 50000, 700],
    [32, 65000, 720],
    [41, 80000, 750],
    [29, 55000, 690],
    [35, 72000, 730]
])
```

Suppose the columns represent:

- column `0` → age
- column `1` → income
- column `2` → credit score

Then:

```python
ages = X[:, 0]
income = X[:, 1]
credit_score = X[:, 2]
```

This is the foundation of feature selection.

---

## 20. Selecting Features for Machine Learning

Suppose you want only age and income:

```python
X_selected = X[:, 0:2]
print(X_selected)
```

Output:

```python
[[25 50000]
 [32 65000]
 [41 80000]
 [29 55000]
 [35 72000]]
```

This keeps only the selected features and removes the rest.

---

## 21. Selecting Observations

Suppose you want the first three customers:

```python
X_first_three = X[:3]
print(X_first_three)
```

Output:

```python
[[25 50000 700]
 [32 65000 720]
 [41 80000 750]]
```

This selects the first three observations or rows.

So:

```python
X[:3]   # first 3 observations
X[:, 0] # first feature
```

---

## 22. 3D Indexing

Consider this 3D array:

```python
import numpy as np

arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
```

Its shape is:

```python
(2, 2, 2)
```

Access an element like this:

```python
print(arr[0, 1, 1])
```

Output:

```python
4
```

This structure is:

```python
array[block, row, column]
```

In other words, `arr[0, 1, 1]` means:

- block `0`
- row `1`
- column `1`

3D arrays are useful when working with image and video data.

---

## 23. Common Mistake

Consider:

```python
import numpy as np

X = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

This is valid and returns `20`:

```python
X[0, 1]
```

This also works:

```python
X[0][1]
```

However, the preferred NumPy style is:

```python
X[0, 1]
```

because multidimensional indexing is designed around:

```python
array[row, column]
```

---

## Summary

Indexing and slicing are how you extract data from NumPy arrays. They help you:

- access specific values
- select rows and columns
- slice ranges of data
- prepare datasets for machine learning
- work with multidimensional arrays efficiently

Understanding this pattern is a key step toward real-world data science work.
