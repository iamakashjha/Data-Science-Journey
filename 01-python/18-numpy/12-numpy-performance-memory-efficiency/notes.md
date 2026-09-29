# Day 58 Notes

## Important Attributes

```python
array.dtype
array.itemsize
array.size
array.nbytes
array.shape
array.ndim
```

### Memory Formula

```python
Total memory = number of elements × bytes per element
```

## View

```python
view = array[1:5]
```

May share memory with the original.

## Copy

```python
copy = array[1:5].copy()
```

Creates independent data.

## Check Memory Sharing

```python
np.shares_memory(a, b)
```

## Vectorization

```python
result = array * 2
```

instead of:

```python
for x in array:
    ...
```

## Benchmarking

Use:

```python
timeit
```

rather than relying on assumptions.

## Important Question

Before working with a large dataset ask:

- How large is it?
- What dtype am I using?
- Am I creating copies?
- Can I use a view?
- Can I vectorize?
- Can I reduce unnecessary allocations?

---

## Quick Summary

- `dtype` tells NumPy how each element is represented.
- `itemsize` tells how many bytes each element uses.
- `nbytes` tells the total memory used by the array data.
- Slices often create views, which can be memory-efficient.
- Advanced indexing usually creates copies.
- Choosing a smaller valid dtype saves memory but may reduce precision.
- Vectorized NumPy operations are often faster than Python loops.
- Always benchmark on your actual workload.
