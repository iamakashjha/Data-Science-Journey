# NumPy Indexing & Slicing Exercises

## Deep Challenge

Given:

```python
import numpy as np

X = np.arange(60).reshape(12, 5)
```

Use only NumPy indexing and slicing to answer the following.

> Before running the code, predict the shape of each result.

### 1. First 5 samples

```python
X[:5]
```

### 2. Last 3 samples

```python
X[-3:]
```

### 3. First feature

```python
X[:, 0]
```

### 4. Last feature

```python
X[:, -1]
```

### 5. Features 2–4

Remember that indexing starts at `0`.

```python
X[:, 1:4]
```

### 6. Samples 3–7 and features 2–4

```python
X[2:7, 1:4]
```

---

## Tip

Do not just run the code immediately.

First, predict the shape and the meaning of the slice. This is how you build strong NumPy intuition and become more comfortable working with real machine learning datasets.