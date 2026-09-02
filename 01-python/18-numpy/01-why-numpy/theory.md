### 1. What is NumPy?

NumPy = Numerical Python

It is a Python library designed primarily for **fast numerical computing.**

It provides:

- Multidimensional arrays
- Mathematical operations
- Statistical operations
- Linear algebra
- Random number generation
- Efficient numerical computation

Install it if necessary:
```
pip install numpy
```
Then:
```
import numpy as np
```
`np` is the standard alias used for NumPy.

### 2. Python List vs NumPy Array

You've already learned lists.
```
numbers = [1, 2, 3, 4, 5]
```
NumPy:
```
import numpy as np


numbers = np.array([1, 2, 3, 4, 5])
```
They may look similar.

But internally, they are fundamentally different.

### 3. Why Not Just Use Python Lists?

Suppose we want to multiply every number by 2.

With a list:
```python
numbers = [1, 2, 3, 4, 5]


result = []


for number in numbers:
    result.append(number * 2)


print(result)
```

Output:
```
[2, 4, 6, 8, 10]
```
NumPy:
```
import numpy as np


numbers = np.array([1, 2, 3, 4, 5])


result = numbers * 2


print(result)
```
Output:
```
[ 2  4  6  8 10]
```
No explicit loop.

This is called **vectorization.**


### 4. What is Vectorization?

Vectorization means performing an operation on an entire collection of values at once instead of explicitly writing a Python loop.

Instead of:

```python
for x in numbers:
    result.append(x * 2)
```

NumPy lets you write:

```python
numbers * 2
```

This isn't just shorter syntax.

NumPy can perform many operations using highly optimized compiled code rather than executing each numerical operation through the Python interpreter.

That is one reason NumPy is so useful for numerical workloads.


### 5. NumPy Arrays

The fundamental object you'll work with is:

```
numpy.ndarray
```

Example:

```python
import numpy as np


arr = np.array([10, 20, 30, 40])


print(arr)

```

Check its type:

```python
print(type(arr))
```

You'll see something similar to:

```python
<class 'numpy.ndarray'>
```

### 6. Arrays Are Designed for Numerical Data

A Python list can contain completely different types:

```python
data = [10, "Python", 3.14, True]
```

NumPy arrays are generally designed to contain elements of a compatible numerical/data type.

For example:

```python
arr = np.array([10, 20, 30, 40])
```

NumPy stores this data in a structured, efficient way.

This is particularly important when working with large numerical datasets.


### 7. Array Data Type

You can inspect the data type:

```python
arr = np.array([10, 20, 30])

print(arr.dtype)
```

You might see:
```
int64
```
The exact dtype can depend on your platform and NumPy version.

You can also explicitly specify one:

```python
arr = np.array([1, 2, 3], dtype=np.float64)

print(arr)
print(arr.dtype)
```

### 8. Basic Mathematical Operations

This is where NumPy becomes powerful.

```python
import numpy as np


prices = np.array([100, 200, 300, 400])
```

Addition:
```
prices + 10
```
Multiplication:
```
prices * 2
```
Division:
```
prices / 2
```
Power:
```
prices ** 2
```
Each operation is applied element-by-element.


### 9. Array vs List: An Important Difference

Consider:
```
numbers = [1, 2, 3]


print(numbers * 2)
```

Output:
```
[1, 2, 3, 1, 2, 3]
```
Why?

Because Python list multiplication means repeat the list.

Now:
```
numbers = np.array([1, 2, 3])


print(numbers * 2)
```
Output:
```
[2 4 6]
```
NumPy interprets multiplication numerically.

This distinction is extremely important.


### 10. Basic Aggregations

NumPy provides common numerical operations.
```
scores = np.array([85, 90, 78, 92, 88])
```
Total:
```
np.sum(scores)
```
Average:
```
np.mean(scores)
```
Maximum:
```
np.max(scores)
```
Minimum:
```
np.min(scores)
```
Standard deviation:
```
np.std(scores)
```
You'll study these properly later.

For today, understand the idea:

NumPy provides optimized operations for numerical data.


### 🎯 Today's Most Important Concept

Don't memorize 30 NumPy functions today.

Understand this transformation:

```
Python List
     ↓
NumPy Array
     ↓
Vectorized Operations
     ↓
Efficient Numerical Computing
```

For example:

```python
scores = np.array([80, 90, 70, 85])

adjusted_scores = scores + 5
```

You're beginning to think in terms of operations on data, rather than manually processing one value at a time.

That change in thinking is extremely important for your Data Science journey.