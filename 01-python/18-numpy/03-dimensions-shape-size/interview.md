# NumPy: Dimensions, Shape, and Size

## Interview Questions

### Q1. What is the difference between `ndim`, `shape`, and `size`?

**Answer:**

- `ndim` returns the number of dimensions.
- `shape` returns the size of each dimension.
- `size` returns the total number of elements in the array.

Example:

```python
import numpy as np

arr = np.zeros((3, 4))
```

Result:

- `arr.ndim` → `2`
- `arr.shape` → `(3, 4)`
- `arr.size` → `12`

---

### Q2. What does `(1000, 20)` mean for a machine learning dataset?

**Answer:**

This usually means:

- `1000` = samples or observations
- `20` = features

So the dataset contains 1000 rows, and each row has 20 feature values.

---

### Q3. What is the difference between `(1000,)` and `(1000, 1)`?

**Answer:**

- `(1000,)` is a 1D array with 1000 elements.
- `(1000, 1)` is a 2D array with 1000 rows and 1 column.

This matters because many ML APIs treat a 1D feature vector differently from a 2D feature matrix.

---

### Q4. Can you reshape an array from `(2, 3)` to `(4, 3)`?

**Answer:**

No.

The total number of elements must remain the same.

- Original shape: `(2, 3)` → `2 × 3 = 6` elements
- New shape: `(4, 3)` → `4 × 3 = 12` elements

Since `6 ≠ 12`, this reshape is invalid.

A valid example would be:

```python
(2, 3) -> (3, 2)
```

because both shapes contain 6 elements.

---

### Q5. Coding Question

Given:

```python
import numpy as np

x = np.array([10, 20, 30, 40, 50])
```

Convert it into shape `(5, 1)`.

**Answer:**

```python
import numpy as np

x = np.array([10, 20, 30, 40, 50])
x = x.reshape(-1, 1)

print(x)
print(x.shape)
```

Output shape:

```python
(5, 1)
```

