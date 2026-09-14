## Theory

### 3.1 What is a dimension?

Think of dimensions as the levels of structure inside your data.
```
0D — Scalar
```
A single number:
```
5
```
Conceptually:
```
5
```
There are no rows or columns.

### 3.2 1D Array

A sequence of values:
```python
import numpy as np

arr = np.array([10, 20, 30, 40])
```
Visually:
```
[10 20 30 40]
```
This is a 1-dimensional array.
```
print(arr.ndim)
```
Output:
```
1
```
Its shape is:
```
print(arr.shape)
```
Output:
```
(4,)
```
Meaning:

There are 4 elements along the only axis.


### 4. 2D Arrays

Now consider:
```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```
Visually:
```
10  20  30
40  50  60
```
This has:
```
2 rows
3 columns
```
Therefore:
```
print(arr.ndim)
```
Output:
```
2
```
And:
```
print(arr.shape)
```
Output:
```
(2, 3)
```
Think:
```
(rows, columns)
```
So:
```
(2, 3)
```
means:
```
2 rows × 3 columns
```

### 5. ndim

ndim tells you:

How many dimensions does this array have?

Example:
```python
a = np.array([1, 2, 3])

print(a.ndim)
```
Output:
```
1
```
2D:
```python
b = np.array([
    [1, 2],
    [3, 4]
])

print(b.ndim)
```
Output:
```
2
```

### 6. shape

shape tells you:

How many elements exist along each dimension?

Example:
```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.shape)
```
Output:
```
(2, 3)
```
Interpretation:
```
2 rows
3 columns
```

### 7. size

size tells you:

The total number of elements in the array.

Example:
```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(a.size)
```
Output:
```
6
```
Because:
```
2 × 3 = 6
```

### 8. ndim vs shape vs size

This distinction is extremely important.

Given:
```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

| Property    |   Result | Meaning                 |
| ----------- | -------: | ----------------------- |
| `arr.ndim`  |      `2` | Number of dimensions    |
| `arr.shape` | `(2, 3)` | Rows × columns          |
| `arr.size`  |      `6` | Total elements          |
| `len(arr)`  |      `2` | Size of first dimension |


So remember:

```
ndim  → How many dimensions?
shape → What is the structure?
size  → How many elements?
len   → How long is the first axis?
```

### 9. The len() Difference

Consider:
```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
```
Then:
```
print(len(arr))
```
Output:
```
3
```
Because the first dimension contains 3 rows.

But:
```
print(arr.size)
```
gives:
```
9
```
And:
```
print(arr.shape)
```
gives:
```
(3, 3)
```
So don't confuse:
```
len(arr)
```
with:
```
arr.size
```


### 10. 3D Arrays

Now we move one level deeper.
```python
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
Check:
```
print(arr.ndim)
```
Output:
```
3
```
Shape:
```
print(arr.shape)
```
Output:
```
(2, 2, 2)
```
You can think of it as:
```
2 blocks
×
2 rows
×
2 columns
```
And:
```
print(arr.size)
```
Output:
```
8
``
Because:
```
2 × 2 × 2 = 8
```


### 11. Real-World Data Interpretation

Dimensions become much more meaningful when you connect them to Data Science.

Student marks
```
Students × Subjects
```
Example:

```python
marks = np.array([
    [80, 90, 85],
    [70, 75, 80],
    [95, 92, 96]
])
```
Shape:
```
marks.shape

(3, 3)
```
Interpretation:
```
3 students
3 subjects
```


### 12. Machine Learning Connection

This is where today's lesson becomes extremely important.

Suppose you have:
```
1000 customers
```
and for every customer you have:
```
age
income
credit_score
account_balance
```
You have:
```
1000 rows
4 features
```
Therefore:
```
X.shape
```
would typically be:
```
(1000, 4)
```
Meaning:
```
1000 samples
4 features
```
This is one of the most important patterns in Machine Learning:
```
X.shape = (number_of_samples, number_of_features)
```


### 13. 🎯 Why X.shape Matters

Suppose:
```
X.shape
```
returns:
```
(5000, 20)
```
You immediately know:
```
5000 → observations/samples
20   → features
```
If:
```
y.shape
```
returns:
```
(5000,)
```
then:
```
X → 5000 samples × 20 features
y → 5000 target values
```
This is foundational knowledge for:
```
train/test splitting
feature engineering
model training
neural networks
matrix multiplication
debugging ML pipelines
```


### 14. Reshaping Arrays

NumPy allows you to change the structure of an array.

Suppose:
```
arr = np.array([1, 2, 3, 4, 5, 6])
```
Current shape:
```
print(arr.shape)

(6,)
```
We can reshape it:
```
reshaped = arr.reshape(2, 3)

print(reshaped)
```
Output:
```
[[1 2 3]
 [4 5 6]]
```
Now:
```
print(reshaped.shape)
```
Output:
```
(2, 3)
```

### 15. The Golden Rule of Reshaping

The total number of elements must remain the same.

Original:
```
6 elements
```
Valid:
```
(2, 3) → 6
(3, 2) → 6
(1, 6) → 6
(6, 1) → 6
```
Invalid:
```
(4, 2) → 8
```
because you cannot turn 6 elements into 8.

Example:
```
arr.reshape(4, 2)
```
will raise an error.


### 16. reshape(-1, 1)

You will frequently encounter this in Machine Learning.

Suppose:
```
x = np.array([10, 20, 30, 40, 50])
```
Shape:
```
(5,)
```
Convert it into a column:
```
x_column = x.reshape(-1, 1)
```
Result:
```
[[10]
 [20]
 [30]
 [40]
 [50]]
```
Shape:
```
(5, 1)
```
Here -1 means:

**NumPy should automatically calculate this dimension.**

This is extremely common when preparing data for ML libraries.

