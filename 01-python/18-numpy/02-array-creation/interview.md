### 1. What is the difference between np.arange() and np.linspace()?

**Answer:**

`np.arange()` generates values based on a specified step size, while `np.linspace()` generates a specified number of evenly spaced values between two endpoints.

Example:

```
np.arange(0, 10, 2)
```

uses a step of 2.
```
np.linspace(0, 10, 5)
```
generates exactly 5 values.

### 2. What is dtype in NumPy?

**Answer:**

`dtype` specifies the data type of elements stored in a NumPy array, such as `int32`, `float32`, or `float64`.

It affects how data is represented in memory and can influence memory usage and computation.

### 3. Why are NumPy arrays usually homogeneous?

**Answer:**

NumPy arrays are designed for efficient numerical computation. Storing elements with a consistent data type allows NumPy to store and process the data efficiently and perform vectorized operations.

### 4. What is the purpose of a random seed?

**Answer:**

A random seed initializes the random-number generator in a reproducible way. Using the same seed with the same generator produces the same sequence of pseudo-random values.

This is important for:

- Experiments
- Testing
- Debugging
- Machine Learning reproducibility

### 5. Coding Question

Create a NumPy array containing 10 evenly spaced values between 0 and 1.

Solution

```python
import numpy as np

arr = np.linspace(0, 1, 10)

print(arr)
```

Notice that we specify 10 values, not the step size.