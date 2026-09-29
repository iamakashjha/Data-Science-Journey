# Day 58 — NumPy Performance & Memory Efficiency

## Why NumPy Is Fast

NumPy performs many numerical operations using optimized lower-level implementations rather than Python-level loops over individual elements.

## dtype

Specifies how array elements are represented.

Examples:

- int8
- int32
- int64
- float32
- float64

## itemsize

Number of bytes used by one element.

## nbytes

Total bytes used by the array's element data.

Formula:

nbytes = size × itemsize

## Views

A view can provide access to existing underlying data without creating a complete independent copy.

## Copies

A copy creates independent data.

## Memory Sharing

Use:

```python
np.shares_memory(a, b)
```

to investigate whether arrays share memory.

## Basic Slicing

Basic slicing often produces views.

## Advanced Indexing

Advanced indexing generally produces copies.

## Vectorization

Apply operations to arrays rather than manually iterating over individual elements in Python.

## Performance

Use benchmarking tools such as timeit rather than assuming that one implementation is faster.

## Important Tradeoff

Smaller dtype:

- less memory
- potentially less precision/range

Larger dtype:

- more memory
- potentially greater precision/range

## Key Principle

Performance is not only about CPU speed.

It is also about:

- memory
- allocations
- copies
- data representation
- algorithm choice
