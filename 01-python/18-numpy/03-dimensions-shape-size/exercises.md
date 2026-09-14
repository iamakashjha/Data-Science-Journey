# NumPy: Dimensions, Shape, and Size

## Exercises

### Exercise 1
Create a 1D array:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
```

Find:

- `arr.ndim`
- `arr.shape`
- `arr.size`

---

### Exercise 2
Create a 3 × 4 matrix.

Then find:

- `ndim`
- `shape`
- `size`

---

### Exercise 3
What is the shape of the following array?

```python
import numpy as np

arr = np.zeros((5, 8))
```

---

### Exercise 4
How many elements are in the following array?

```python
import numpy as np

arr = np.ones((4, 5, 2))
```

---

### Exercise 5
Reshape the following array:

```python
import numpy as np

arr = np.arange(12)
```

into a `3 × 4` array.

---

### Exercise 6
Reshape 20 elements into a `4 × 5` array.

```python
import numpy as np

arr = np.arange(20)
```

---

### Exercise 7
Create the following array:

```python
import numpy as np

x = np.arange(15)
```

Convert it into a column vector.

---

### Exercise 8
Given:

```python
X.shape == (500, 12)
```

What does this mean in a machine learning dataset?

---

### Exercise 9
Given:

```python
X.shape == (10000, 30)
y.shape == (10000,)
```

Explain what each dimension represents.

---

### Exercise 10 — Think Like a Data Scientist
A model expects the input shape:

```python
(samples, features)
```

You have:

```python
X.shape == (1000,)
```

You intended this to represent 1000 samples with one feature.

What should the shape be?