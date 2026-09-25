# Exercises - NumPy Aggregations & Statistics

Use NumPy to solve the following problems.

## Exercise 1

Given:

```python
x = np.array([10, 20, 30, 40, 50])
```

Find:

- sum
- mean
- median
- minimum
- maximum
- standard deviation

## Exercise 2

Given:

```python
X = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
```

What is:

```python
np.sum(X, axis=0)
```

## Exercise 3

What is:

```python
np.sum(X, axis=1)
```

## Exercise 4

What is:

```python
np.mean(X, axis=0)
```

## Exercise 5

What is:

```python
np.mean(X, axis=1)
```

## Exercise 6

Given:

```python
scores = np.array([45, 90, 67, 88, 52])
```

Find the index of the highest score.

## Exercise 7

Find the index of the lowest score in the same array.

## Exercise 8

Given:

```python
X = np.arange(20).reshape(4, 5)
```

What is the shape of:

```python
np.mean(X, axis=0)
```

## Exercise 9

What is the shape of:

```python
np.mean(X, axis=1)
```

## Exercise 10

Given:

```python
X.shape = (5000, 10)
```

What does:

```python
np.mean(X, axis=0)
```

represent? How many values does it contain?

## Answer key

1. `sum = 150`, `mean = 30.0`, `median = 30.0`, `min = 10`, `max = 50`, `std ≈ 15.81`
2. `array([90, 120])`
3. `array([30, 70, 110])`
4. `array([30., 40.])`
5. `array([15., 35., 55.])`
6. `1`
7. `4`
8. `(5,)`
9. `(4,)`
10. One mean value per feature, so 10 values total.
