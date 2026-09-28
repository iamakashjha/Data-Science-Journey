# Exercises - NumPy Boolean Masking, Filtering & Conditional Selection

## Exercise 1

Given:

```python
ages = np.array([18, 22, 27, 31, 16, 40])
```

What is `ages[ages > 25]`?

## Exercise 2

What is `ages[(ages >= 20) & (ages <= 35)]`?

## Exercise 3

What is `ages[(ages < 20) | (ages > 35)]`?

## Exercise 4

What is `ages[~(ages > 25)]`?

## Exercise 5

Given:

```python
scores = np.array([45, 72, 88, 55, 91])
```

What does `np.where(scores >= 60, "Pass", "Fail")` return?

## Exercise 6

What does `np.where(scores >= 80)` return?

## Exercise 7

What does `np.any(scores > 90)` return?

## Exercise 8

What does `np.all(scores > 40)` return?

## Exercise 9

Given:

```python
scores[scores < 60] = 0
```

What does the array become?

## Exercise 10

If `X.shape = (5000, 10)`, what is the shape of the mask created by `X[:, 4] > 100`?

## Answer key

1. `[27 31 40]`
2. `[22 27 31]`
3. `[18 16 40]`
4. `[18 22 16]`
5. `['Fail' 'Pass' 'Pass' 'Fail' 'Pass']`
6. `(array([2, 4]),)`
7. `True`
8. `True`
9. `[0 72 88 0 91]`
10. `(5000,)`
