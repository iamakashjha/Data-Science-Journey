# Exercises - NumPy Random Numbers & Reproducibility

Use NumPy to solve the following.

## Exercise 1

Generate 10 random numbers between 0 and 1.

## Exercise 2

Generate 20 random integers between 1 and 100.

## Exercise 3

Generate a 5 x 3 matrix of random integers between 10 and 50.

## Exercise 4

Generate 1,000 values from a normal distribution with:

- mean = 50
- std = 5

Then calculate the actual sample mean and standard deviation. Are they exactly 50 and 5? Why or why not?

## Exercise 5

Use `np.random.choice()` to randomly select 5 items from:

```python
["Python", "SQL", "Statistics", "ML", "Deep Learning"]
```

## Exercise 6

Select 3 unique items without replacement.

## Exercise 7

Create a reproducible random array using `np.random.default_rng()`.

## Exercise 8

Generate 1,000 random values between 20 and 30. Calculate:

- minimum
- maximum
- mean
- standard deviation

## Exercise 9

Generate synthetic student scores with:

- mean = 75
- std = 10
- n = 500

Constrain the scores to the range `[0, 100]`.

## Exercise 10

Explain why this is useful:

```python
rng = np.random.default_rng(42)
```

instead of generating random numbers without controlling the generator.

## Answer key (brief)

1. Use `rng.random(10)` or `np.random.random(10)`.
2. Use `rng.integers(1, 101, size=20)`.
3. Use `rng.integers(10, 51, size=(5, 3))`.
4. They will be close, not exactly equal, because random sampling is variable.
5. Use `rng.choice([...], size=5)`.
6. Use `rng.choice([...], size=3, replace=False)`.
7. `rng = np.random.default_rng(42)` then call `rng.random(...)`.
8. Use `rng.uniform(20, 30, size=1000)` and then compute statistics.
9. Use `rng.normal(75, 10, 500)` and `np.clip(scores, 0, 100)`.
10. It makes the random process reproducible and easier to debug and compare.
