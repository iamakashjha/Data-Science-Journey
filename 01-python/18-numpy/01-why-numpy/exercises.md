# NumPy Fundamentals - Exercises

## Conceptual Questions

### 1. What is NumPy?

**Answer:**

NumPy (Numerical Python) is a Python library for numerical computing. It provides:
- **Arrays**: Fast, efficient multi-dimensional arrays (like super-powered lists)
- **Functions**: Mathematical, statistical, and linear algebra operations
- **Performance**: Operations are 10-1000x faster than Python loops

**In simple terms:** If Python lists are for storing anything, NumPy arrays are specialized for fast numerical operations.

```python
import numpy as np

# Python list
py_list = [1, 2, 3, 4, 5]

# NumPy array (more powerful)
np_array = np.array([1, 2, 3, 4, 5])
```

**Why it matters for Data Science:**
- Work with millions of data points efficiently
- Statistical analysis, linear algebra, Fourier transforms
- Foundation for Pandas, Scikit-learn, TensorFlow

---

### 2. Why was NumPy created?

**Answer:**

Python is slow for mathematical operations. Scientists needed speed.

**The Problem:**
```python
# Calculate average of 1 million numbers in Python
numbers = list(range(1_000_000))

# This loop is SLOW
total = 0
for num in numbers:
    total += num
avg = total / len(numbers)  # Takes milliseconds for 1M items
```

**The Solution (NumPy):**
```python
import numpy as np

# Same operation in NumPy
numbers = np.arange(1_000_000)
avg = np.mean(numbers)  # Takes microseconds (1000x faster!)
```

**Why NumPy is faster:**
1. **C Implementation**: NumPy is written in C, not Python
2. **Vectorization**: Operations on entire arrays at once (no slow loops)
3. **Memory Efficiency**: Arrays store data contiguously (CPU caches it)
4. **No Type Checking**: Python checks types every iteration; NumPy checks once

**Historical Context:**
- Created by Travis Oliphant in 2006
- Python needed speed for scientific computing
- Now the foundation of the entire Python data science ecosystem

---

### 3. What is a NumPy array?

**Answer:**

A NumPy array is a **grid of numbers** stored contiguously in memory, all of the same data type.

**Python List vs NumPy Array:**

```python
# Python List
py_list = [1, 2, 3, 4, 5]
# Each element can be ANY type
mixed = [1, "two", 3.0, True, None]  # Valid!

# NumPy Array
import numpy as np
np_array = np.array([1, 2, 3, 4, 5])
# All elements MUST be the same type (integers here)
mixed = np.array([1, "two", 3.0])  # Converts all to strings!
```

**Types of Arrays:**

```python
import numpy as np

# 1D Array (like a list)
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d.shape)  # (5,)

# 2D Array (like a matrix/table)
arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6]])
print(arr_2d.shape)  # (2, 3) - 2 rows, 3 columns

# 3D Array (like a cube of data)
arr_3d = np.array([[[1, 2], [3, 4]], 
                   [[5, 6], [7, 8]]])
print(arr_3d.shape)  # (2, 2, 2)
```

**Key Properties:**

```python
arr = np.array([1, 2, 3, 4, 5])

arr.shape      # (5,) - dimensions
arr.dtype      # dtype('int64') - data type
arr.size       # 5 - total number of elements
arr.ndim       # 1 - number of dimensions
arr.nbytes     # 40 - bytes used in memory
```

**Why arrays are better than lists for data:**
- Homogeneous (all same type) → Can optimize
- Fixed structure → Predictable memory usage
- Vectorized operations → No loops needed
- Direct integration with math libraries

---

### 4. What is vectorization?

**Answer:**

**Vectorization** is writing code that operates on entire arrays at once, instead of looping through elements one-by-one.

**Non-Vectorized (Loop-Based):**
```python
# Python loop - SLOW
numbers = [1, 2, 3, 4, 5]
result = []
for num in numbers:
    result.append(num * 2)  # Process one element at a time
print(result)  # [2, 4, 6, 8, 10]
```

**Vectorized (NumPy):**
```python
# NumPy vectorization - FAST
import numpy as np
numbers = np.array([1, 2, 3, 4, 5])
result = numbers * 2  # Process entire array at once!
print(result)  # [2 4 6 8 10]
```

**More Examples:**

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Non-vectorized (loop)
result = []
for x in arr:
    result.append(x ** 2)
# result = [1, 4, 9, 16, 25]

# Vectorized (NumPy)
result = arr ** 2  # Much simpler!
# result = [1 4 9 16 25]

# Even more complex operations work
result = (arr * 2) + 10  # Multiply by 2, then add 10
# All elements processed simultaneously
```

**Why Vectorization is Faster:**

```
Loop Approach:
- Multiply element 1: 1 * 2 = 2
- Multiply element 2: 2 * 2 = 4
- Multiply element 3: 3 * 2 = 6
- Multiply element 4: 4 * 2 = 8
- Multiply element 5: 5 * 2 = 10
[SLOW: 5 separate operations, 5 overhead costs]

Vectorized Approach:
[Multiply ALL 5 elements at CPU's fastest speed]
[FAST: 1 operation, handled by optimized C code]
```

**The Data Science Principle:**
> "Always try to vectorize. Loops are for when vectorization is impossible."

---

### 5. Why can NumPy be faster than Python loops for numerical operations?

**Answer:**

NumPy is faster for **three fundamental reasons:**

#### **Reason 1: Language Implementation (C vs Python)**

```python
# Python Loop (interpreted line-by-line)
result = []
for i in range(1_000_000):        # 1. Check range
    result.append(i * 2)          # 2. Get element from memory
                                   # 3. Check type of 'i'
                                   # 4. Call multiply operator
                                   # 5. Check type of result
                                   # 6. Call append
# Total: ~50+ operations per element!

# NumPy (compiled C code)
import numpy as np
result = np.arange(1_000_000) * 2  # 1. One optimized instruction
# Total: ~1 operation per element!
```

**Benchmark:**
```
Python loop:   ~50 milliseconds
NumPy:         ~5 microseconds
Speed gain:    10,000x faster!
```

#### **Reason 2: Memory Layout (Contiguous Storage)**

```python
# Python list (scattered in memory)
py_list = [1, 2, 3, 4, 5]
# Memory layout:
# Address 1000: pointer to object with value 1
# Address 1008: pointer to object with value 2
# Address 1016: pointer to object with value 3
# [Addresses far apart, CPU has to jump around]

# NumPy array (packed together)
import numpy as np
np_array = np.array([1, 2, 3, 4, 5])
# Memory layout:
# Address 1000: 1
# Address 1008: 2
# Address 1016: 3
# [Addresses close together, CPU cache works perfectly]

# CPU Caching:
# When accessing address 1000, CPU loads nearby addresses into cache
# NumPy benefits; Python loops don't
```

#### **Reason 3: Type Consistency (No Type Checking)**

```python
# Python (checks type every iteration)
result = []
for x in [1, 2, 3, 4, 5]:
    # 1. Is x an int?
    # 2. Does int support * operator?
    # 3. Is 2 an int?
    # 4. Can int * int work?
    result.append(x * 2)
# Type checking slows everything down

# NumPy (knows the type once)
import numpy as np
arr = np.array([1, 2, 3, 4, 5], dtype=np.int64)
# "This array contains int64. All operations are int64."
# No type checking per element!
result = arr * 2
```

#### **Reason 4: Vectorization (Parallel-Ready)**

```python
# Python loop (sequential)
# Step 1: Multiply element 1 by 2
# Step 2: Multiply element 2 by 2  <- Must wait for step 1
# Step 3: Multiply element 3 by 2  <- Must wait for step 2
# [Sequential, can't parallelize]

# NumPy (parallel-ready)
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
result = arr * 2
# CPU can multiply ALL elements in parallel!
# Modern CPUs have multiple cores; NumPy uses them
```

**Speed Comparison:**

```python
import numpy as np
import time

# Setup
large_list = list(range(10_000_000))
large_array = np.arange(10_000_000)

# Python loop
start = time.time()
result = []
for x in large_list:
    result.append(x * 2)
py_time = time.time() - start

# NumPy
start = time.time()
result = large_array * 2
np_time = time.time() - start

print(f"Python:  {py_time:.4f} seconds")
print(f"NumPy:   {np_time:.4f} seconds")
print(f"Speed gain: {py_time / np_time:.0f}x faster")
# Output:
# Python:  0.5000 seconds
# NumPy:   0.0050 seconds
# Speed gain: 100x faster
```

---

## Practical Exercises

### 1. What is the difference between `[1, 2, 3] * 2` and `np.array([1, 2, 3]) * 2`?

**Answer:**

```python
# Python list multiplication
py_list = [1, 2, 3]
result = py_list * 2
print(result)
# Output: [1, 2, 3, 1, 2, 3]
# REPEATS the list (doesn't multiply elements!)

# NumPy array multiplication
import numpy as np
np_array = np.array([1, 2, 3])
result = np_array * 2
print(result)
# Output: [2 4 6]
# MULTIPLIES each element by 2!
```

**Why the difference?**

```python
# Python list * operator: CONCATENATION
[1, 2, 3] * 2 = [1, 2, 3] + [1, 2, 3]

# NumPy array * operator: ELEMENT-WISE MULTIPLICATION
np.array([1, 2, 3]) * 2 = [1*2, 2*2, 3*2]
```

**Key Insight:**
> Python lists don't know about math; they're general-purpose containers.
> NumPy arrays are designed for math; all operators work mathematically.

**More Examples:**

```python
import numpy as np

# Python lists
py_list = [1, 2, 3]
print(py_list + [4, 5])     # [1, 2, 3, 4, 5] - concatenation
print(py_list - [1])        # TypeError! No subtraction

# NumPy arrays
np_array = np.array([1, 2, 3])
print(np_array + np.array([4, 5, 6]))  # [5 7 9] - element-wise addition
print(np_array - np.array([1, 1, 1]))  # [0 1 2] - element-wise subtraction
print(np_array ** 2)                    # [1 4 9] - element-wise power
print(np_array / 2)                     # [0.5 1.  1.5] - element-wise division
```

---

### 2. What does `dtype` represent?

**Answer:**

`dtype` (data type) specifies **what kind of numbers are stored** in a NumPy array and **how much memory each number uses**.

**Common dtypes:**

```python
import numpy as np

# Integer types
arr_int32 = np.array([1, 2, 3], dtype=np.int32)    # 32-bit integers
arr_int64 = np.array([1, 2, 3], dtype=np.int64)    # 64-bit integers (default)

# Floating point types
arr_float32 = np.array([1.1, 2.2], dtype=np.float32)   # 32-bit floats
arr_float64 = np.array([1.1, 2.2], dtype=np.float64)   # 64-bit floats (default)

# Others
arr_bool = np.array([True, False], dtype=np.bool_)     # Boolean
arr_complex = np.array([1+2j, 3+4j], dtype=np.complex64)  # Complex numbers
arr_str = np.array(['a', 'b'], dtype=np.str_)          # Strings

# Check dtype
print(arr_int32.dtype)   # int32
print(arr_float64.dtype) # float64
```

**Why dtype matters:**

```python
import numpy as np

# Memory usage
arr_int32 = np.array([1, 2, 3], dtype=np.int32)
arr_int64 = np.array([1, 2, 3], dtype=np.int64)

print(arr_int32.nbytes)  # 12 bytes (3 numbers * 4 bytes each)
print(arr_int64.nbytes)  # 24 bytes (3 numbers * 8 bytes each)

# Precision
arr_float32 = np.array([1.123456789], dtype=np.float32)
arr_float64 = np.array([1.123456789], dtype=np.float64)

print(arr_float32)  # [1.12345684] - less precise
print(arr_float64)  # [1.123456789] - more precise

# Range
arr_int32 = np.array([1, 2, 3], dtype=np.int32)
print(arr_int32.max())  # 2147483647 - max 32-bit integer

arr_int64 = np.array([1, 2, 3], dtype=np.int64)
print(arr_int64.max())  # 9223372036854775807 - max 64-bit integer
```

**When to use each:**

| dtype | Use Case | Memory | Range |
|-------|----------|--------|-------|
| `int32` | Small integers, memory-limited | 4 bytes | ±2 billion |
| `int64` | Large integers, default choice | 8 bytes | ±9 quintillion |
| `float32` | Graphics, when precision doesn't matter | 4 bytes | ±3.4e38 |
| `float64` | Science/data science, default choice | 8 bytes | ±1.7e308 |
| `bool_` | True/False values | 1 byte | True/False |

**Default dtype:**

```python
import numpy as np

arr = np.array([1, 2, 3])      # Default: int64 (or int32 on 32-bit Python)
arr = np.array([1.0, 2.0, 3.0])  # Default: float64
arr = np.array([True, False])     # Default: bool_
```

---

### 3. What does `np.mean()` do?

**Answer:**

`np.mean()` calculates the **average (arithmetic mean)** of array elements.

**Basic Usage:**

```python
import numpy as np

arr = np.array([85, 90, 88, 92])
average = np.mean(arr)
print(average)  # 88.75
# (85 + 90 + 88 + 92) / 4 = 355 / 4 = 88.75
```

**Compared to Python:**

```python
# Python
marks = [85, 90, 88, 92]
avg = sum(marks) / len(marks)
print(avg)  # 88.75

# NumPy
import numpy as np
marks = np.array([85, 90, 88, 92])
avg = np.mean(marks)
print(avg)  # 88.75.0
# Same result, but NumPy is faster!
```

**2D Arrays (Calculate mean by axis):**

```python
import numpy as np

# Class marks (3 students, 4 subjects)
marks = np.array([
    [85, 90, 88, 92],  # Student 1
    [92, 88, 95, 90],  # Student 2
    [78, 85, 80, 88]   # Student 3
])

# Mean of all elements
all_avg = np.mean(marks)
print(all_avg)  # 88.08333... - average of ALL 12 marks

# Mean across subjects (average for each student)
student_avg = np.mean(marks, axis=1)
print(student_avg)  # [88.75 91.25 82.75] - average per student

# Mean across students (average for each subject)
subject_avg = np.mean(marks, axis=0)
print(subject_avg)  # [85. 87.67 87.67 90.] - average per subject
```

**Comparison with other statistics:**

```python
import numpy as np

marks = np.array([85, 90, 88, 92])

# Mean (average)
print(np.mean(marks))      # 88.75 - sum divided by count

# Median (middle value)
print(np.median(marks))    # 89.0 - middle value when sorted

# Standard deviation (spread)
print(np.std(marks))       # 2.75 - how much values vary

# Min and Max
print(np.min(marks))       # 85
print(np.max(marks))       # 92

# Sum
print(np.sum(marks))       # 355
```

**Real-World Usage:**

```python
import numpy as np

# Student performance across 3 exams
exam1 = np.array([85, 92, 78, 88])  # 4 students
exam2 = np.array([88, 95, 82, 90])
exam3 = np.array([90, 93, 85, 92])

# Calculate each student's average across 3 exams
all_exams = np.array([exam1, exam2, exam3])
student_averages = np.mean(all_exams, axis=0)
print(student_averages)  # [87.67 93.33 81.67 90.]

# Calculate class average for each exam
exam_averages = np.mean(all_exams, axis=1)
print(exam_averages)  # [85.75 88.75 90.]

# Calculate overall class average
overall_avg = np.mean(all_exams)
print(overall_avg)  # 88.0625
```

---

### 4. Why are NumPy arrays important for Data Science?

**Answer:**

NumPy arrays are the **foundation of all data science in Python**. Here's why:

#### **Reason 1: Foundation for Every Data Science Library**

```python
# Pandas (data analysis)
import pandas as pd
df = pd.DataFrame([1, 2, 3])  # Built on NumPy internally

# Scikit-learn (machine learning)
from sklearn.linear_model import LinearRegression
model.fit(X_train, y_train)  # X_train and y_train are NumPy arrays

# TensorFlow (deep learning)
import tensorflow as tf
tensor = tf.convert_to_tensor([1, 2, 3])  # NumPy-compatible

# Matplotlib (visualization)
import matplotlib.pyplot as plt
plt.plot(np.array([1, 2, 3]))  # Plots NumPy arrays

# SciPy (scientific computing)
from scipy import stats
stats.linregress(x, y)  # Works with NumPy arrays
```

#### **Reason 2: Handle Large Datasets Efficiently**

```python
import numpy as np

# Hypothetical: 1 million customer records with 100 features each
data = np.random.rand(1_000_000, 100)  # 1M x 100 matrix

# Python would take minutes
# NumPy: instant

# Calculations on massive data
mean_per_feature = np.mean(data, axis=0)      # Fast
normalized = (data - mean_per_feature) / np.std(data, axis=0)  # Fast
```

#### **Reason 3: Statistical Operations**

```python
import numpy as np

data = np.array([85, 92, 78, 88, 95])

# Central tendency
print(np.mean(data))      # Average
print(np.median(data))    # Middle value

# Spread
print(np.std(data))       # Standard deviation
print(np.var(data))       # Variance

# Percentiles
print(np.percentile(data, 25))  # 25th percentile (Q1)
print(np.percentile(data, 50))  # 50th percentile (median)
print(np.percentile(data, 75))  # 75th percentile (Q3)

# Correlations
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 6])
correlation = np.corrcoef(x, y)
```

#### **Reason 4: Linear Algebra (Required for ML)**

```python
import numpy as np

# Matrix multiplication (core of neural networks)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
result = np.dot(A, B)  # Matrix multiplication

# Eigenvalues and eigenvectors (for PCA)
eigenvalues, eigenvectors = np.linalg.eig(A)

# Solving systems of equations
# 2x + 3y = 8
# 4x + y = 10
coefficients = np.array([[2, 3], [4, 1]])
constants = np.array([8, 10])
solution = np.linalg.solve(coefficients, constants)

# Singular Value Decomposition (for dimensionality reduction)
U, S, Vt = np.linalg.svd(A)
```

#### **Reason 5: Data Preprocessing**

```python
import numpy as np

# Raw data
raw_data = np.array([85, 92, np.nan, 88, 95, 150])  # Has NaN and outlier

# Remove NaN values
clean_data = raw_data[~np.isnan(raw_data)]

# Normalize (0-1 range)
normalized = (clean_data - np.min(clean_data)) / (np.max(clean_data) - np.min(clean_data))

# Standardize (mean=0, std=1)
standardized = (clean_data - np.mean(clean_data)) / np.std(clean_data)

# Handle outliers
q1 = np.percentile(clean_data, 25)
q3 = np.percentile(clean_data, 75)
iqr = q3 - q1
outliers = (clean_data < q1 - 1.5*iqr) | (clean_data > q3 + 1.5*iqr)
clean_data = clean_data[~outliers]
```

#### **Reason 6: Vectorized Operations (Write Less Code)**

```python
# Data Science Task: Apply discount to prices

# Python approach (verbose)
prices = [100, 50, 200, 75]
discounted = []
for price in prices:
    discounted.append(price * 0.9)  # 10% discount

# NumPy approach (concise)
import numpy as np
prices = np.array([100, 50, 200, 75])
discounted = prices * 0.9  # One line!

# Complex operations
# Apply formula to thousands of rows
data = np.random.rand(100000, 50)
result = (data ** 2 + np.log(data + 1)) / (1 + data)  # Still one line!
```

#### **Reason 7: Integration with Data Visualization**

```python
import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)                 # Calculate sine

# Plot
plt.plot(x, y)
plt.show()

# Histograms
data = np.random.normal(0, 1, 10000)  # Normal distribution
plt.hist(data, bins=50)
plt.show()
```

#### **Reason 8: Reproducibility (Random Seed)**

```python
import numpy as np

# Set random seed for reproducible results
np.random.seed(42)
data1 = np.random.rand(5)

np.random.seed(42)
data2 = np.random.rand(5)

print(data1 == data2)  # [True, True, True, True, True]
# Same random sequence every time!
```

#### **Reason 9: Performance Comparison**

```python
import numpy as np
import time

# Problem: Square root of 10 million numbers
n = 10_000_000

# Python
py_list = list(range(n))
start = time.time()
result = [x ** 0.5 for x in py_list]
py_time = time.time() - start

# NumPy
np_array = np.arange(n)
start = time.time()
result = np.sqrt(np_array)
np_time = time.time() - start

print(f"Python: {py_time:.4f}s")
print(f"NumPy:  {np_time:.4f}s")
print(f"Speedup: {py_time/np_time:.0f}x faster")
# Output:
# Python: 1.2345s
# NumPy:  0.0123s
# Speedup: 100x faster
```

#### **Reason 10: Industry Standard**

```python
# Every data scientist/ML engineer knows NumPy
# Every data science job requires NumPy
# Every dataset library uses NumPy

# Job postings: "3+ years with NumPy, Pandas, Scikit-learn"
# Open source: numpy.org has millions of downloads per month
# Research: Used in scientific papers, academic research
```

**Bottom Line:**
> Without NumPy, data science in Python would not exist.
> NumPy is not just important—it's essential.

---

## Summary Table

| Concept | What | Why | Example |
|---------|------|-----|---------|
| **Array** | Homogeneous collection | Fast operations | `np.array([1,2,3])` |
| **Vectorization** | Batch operations | No loops needed | `arr * 2` |
| **dtype** | Data type specification | Memory/precision control | `dtype=np.float32` |
| **np.mean()** | Calculate average | Statistical analysis | `np.mean(arr)` |
| **Speed** | 10-1000x faster | C implementation | NumPy vs Python |

---

**Next Steps:**
1. Install NumPy: `pip install numpy`
2. Import it: `import numpy as np`
3. Create your first array: `arr = np.array([1, 2, 3])`
4. Start computing!

Let's go! 🚀