# Day 58 Exercises

## Exercise 1 — Memory Calculation

Create:

```python
arr = np.zeros(5_000_000, dtype=np.float64)
```

Calculate:

- number of elements
- bytes per element
- total bytes
- total MB

Do the calculation manually first. Then verify using:

```python
arr.nbytes
```

## Exercise 2 — Dtype Comparison

Create arrays containing the same values using:

- int8
- int16
- int32
- int64

Compare:

- dtype
- itemsize
- nbytes

Write down what you observe.

## Exercise 3 — View or Copy?

Given:

```python
arr = np.arange(20)

a = arr[5:10]
b = arr[[5, 6, 7, 8, 9]]
```

Determine:

- Which one shares memory?
- Which one creates a copy?

Verify with:

```python
np.shares_memory()
```

## Exercise 4 — Performance

Compare:

```python
[x * 2 for x in range(1_000_000)]
```

against:

```python
np.arange(1_000_000) * 2
```

Use `timeit`.

Don't just report the numbers. Explain why the approaches behave differently.

## Exercise 5 — In-Place Operations

Compare:

```python
arr = arr * 2
```

with:

```python
arr *= 2
```

Think about:

- memory
- object identity
- shared views
- side effects
