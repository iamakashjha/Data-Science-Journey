### Day 47 — NumPy Array Creation

**Goal:** Become comfortable creating arrays from real data, ranges, zeros, ones, and evenly spaced values.

### Learning Objectives

By the end of today, you should be able to:

- Create NumPy arrays using np.array()
- Create arrays of zeros and ones
- Generate numerical sequences
- Generate evenly spaced values
- Control array data types using dtype
- Understand when each array-creation method is useful
- Inspect basic array properties

### 1️⃣ Creating an Array with np.array()

The most basic approach is converting an existing Python sequence into a NumPy array.

```python
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers)
```

Output:
```
[10 20 30 40 50]
```
You can also create arrays from tuples:
```
values = np.array((10, 20, 30))

print(values)
```

### 2️⃣ Creating a 2D Array

NumPy isn't limited to one-dimensional data.

You can create a matrix-like structure:

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
```

Output:

```
[[1 2 3]
 [4 5 6]]
```

Conceptually:
```
        Columns
       1   2   3
     ┌───────────
Row 1│ 1   2   3
Row 2│ 4   5   6
```

We'll study dimensions and shape in detail later.


### 3️⃣ np.zeros()

Creates an array filled with zeros.

```python
zeros = np.zeros(5)

print(zeros)
```

Output:
```
[0. 0. 0. 0. 0.]
```

Notice that these are floating-point values.

You can also create a 2D array:
```python
zeros = np.zeros((3, 4))

print(zeros)
```

This creates:
```
3 rows × 4 columns
```

### 4️⃣ np.ones()

Creates an array filled with ones.

```python
ones = np.ones(5)

print(ones)
```

Output:

```
[1. 1. 1. 1. 1.]
```

2D:

```python
ones = np.ones((2, 3))

print(ones)
```

Output:

```
[[1. 1. 1.]
 [1. 1. 1.]]
```

### 5️⃣ np.full()

Sometimes you want every element to contain the same value.

Use:

```python
arr = np.full(5, 7)

print(arr)
```

Output:

```
[7 7 7 7 7]
```

2D:

```python
arr = np.full((2, 3), 10)

print(arr)
```

Output:

```
[[10 10 10]
 [10 10 10]]
```

This is useful when initializing arrays with a known constant.

### 6️⃣ np.arange()

`np.arange()` creates evenly spaced values based on a step size.

```python
numbers = np.arange(0, 10)

print(numbers)
```

Output:

```
[0 1 2 3 4 5 6 7 8 9]
```

The endpoint is excluded.

### Start, Stop, Step

```python
numbers = np.arange(2, 11, 2)

print(numbers)
```

Output:
```
[ 2  4  6  8 10]
```
Think:
```
start → stop → step
```
```
2 → 11 → 2
```

### 7️⃣ np.linspace()

`np.linspace()` creates a specified number of evenly spaced values between two endpoints.

```python
numbers = np.linspace(0, 10, 5)

print(numbers)
```

Output:

```
[ 0.   2.5  5.   7.5 10. ]
```

There are exactly 5 values.

This is the key difference:

`arange()`

You specify the step.

```
np.arange(0, 10, 2)
linspace()
```

You specify the number of values.

```
np.linspace(0, 10, 5)
```

Remember this distinction


### 8️⃣ Why linspace() Matters in Data Science

Suppose you're creating values for plotting a mathematical function.

You might want:
```
0
0.1
0.2
0.3
...
10
```

Instead of manually calculating the spacing, you can use:
```
x = np.linspace(0, 10, 101)
```

Now you have 101 evenly spaced points.

This becomes very useful when you start working with **visualization, mathematical functions, and ML concepts.**


### 9️⃣ Specifying dtype

You can control the data type.

```python
arr = np.array(
    [1, 2, 3, 4],
    dtype=np.float64
)

print(arr)
print(arr.dtype)
```

Output will look like:
```
[1. 2. 3. 4.]
float64
```
You can also use:
```
dtype=np.int32
```
or:
```
dtype=np.float32
```


### 🔟 Why Does dtype Matter?

Data Scientists often work with millions or billions of numerical values.

Consider:
```
float64
```
versus:
```
float32
```
They use different amounts of memory.

For many machine learning workloads, choosing an appropriate dtype can significantly affect:

- Memory usage
- Computation
- Storage
- Model performance

You don't need to optimize this prematurely, but you should understand why dtype exists.


### 1️⃣1️⃣ Random Arrays

NumPy also provides random-number generation.

```python
rng = np.random.default_rng(42)

numbers = rng.random(5)

print(numbers)
```

The values will be between 0 and 1.

The 42 is a **seed.**

Using the same seed makes the generated sequence reproducible.

This concept will become very important when you start Machine Learning experiments.

### Data Science Connection

Array creation isn't just about learning syntax.

Think about different situations:

```
| Situation                                     | NumPy function            |
| --------------------------------------------- | ------------------------- |
| Convert existing data                         | `np.array()`              |
| Initialize with zeros                         | `np.zeros()`              |
| Initialize with ones                          | `np.ones()`               |
| Initialize with constant                      | `np.full()`               |
| Generate sequence using step                  | `np.arange()`             |
| Generate fixed number of evenly spaced values | `np.linspace()`           |
| Generate random values                        | `np.random.default_rng()` |
```

You'll encounter these constantly in:

- Data preprocessing
- Numerical simulations
- Machine Learning
- Deep Learning
- Statistics
- Visualization
- Testing

### Today's Key Takeaway

You should now be able to look at a problem and think:
```
I need an array...
       ↓
What kind?
       ↓
Existing data → np.array()
Zeros         → np.zeros()
Ones          → np.ones()
Constant      → np.full()
Step-based    → np.arange()
Fixed count   → np.linspace()
Random data   → random generator
```

That's the beginning of NumPy thinking.

