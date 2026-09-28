# Day 57 Notes

## Key concepts

- Vectorization
- Parallel arrays
- Derived metrics
- Boolean filtering
- Multiple conditions
- Ranking
- Top-k selection
- Outlier detection
- Normalization
- Feature combination
- Analytical pipelines

## Important patterns

### Derived metric

```python
metric = array_a / array_b
```

### Boolean filter

```python
mask = values > threshold
filtered = values[mask]
```

### Multiple conditions

```python
mask = (
    (condition_1) &
    (condition_2)
)
```

### Ranking

```python
indices = np.argsort(values)[::-1]
```

### Top-k

```python
top_k = indices[:k]
```

### Maximum

```python
index = np.argmax(values)
```

### Minimum

```python
index = np.argmin(values)
```

## Key lesson

NumPy is not only about manipulating arrays.

It allows us to express numerical reasoning efficiently.
