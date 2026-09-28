# Exercises - NumPy Reshaping, Flattening, Stacking & Splitting

## Exercise 1

What is the shape of:

```python
x = np.arange(24)
x.reshape(4, 6)
```

## Exercise 2

What does this produce?

```python
x.reshape(2, -1)
```

## Exercise 3

Why does this fail?

```python
x.reshape(5, 5)
```

## Exercise 4

What is the difference between `flatten()` and `ravel()`?

## Exercise 5

What does `.T` do to a 2D array?

## Exercise 6

Given:

```python
A.shape = (5, 3)
B.shape = (5, 2)
```

Can you concatenate them using:

```python
np.concatenate([A, B], axis=1)
```

What will the resulting shape be?

## Exercise 7

What is the difference between:

```python
np.concatenate([a, b])
and:
np.stack([a, b])
```

## Exercise 8

What does `np.vstack()` do?

## Exercise 9

What does `np.hsplit()` do?

## Exercise 10

Suppose:

```python
X.shape = (5000, 20)
```

What would you expect from:

```python
X.T.shape
```

## Answer key

1. `(4, 6)`
2. `(2, 12)` if the original length is 24
3. Because `5 * 5 = 25`, while the original array has 24 values
4. `flatten()` returns a copy; `ravel()` usually returns a view
5. It swaps rows and columns
6. Yes; result shape is `(5, 5)`
7. `concatenate` joins along an existing axis; `stack` creates a new axis
8. Vertically stacks arrays
9. Horizontally splits an array into sections by columns
10. `(20, 5000)`
