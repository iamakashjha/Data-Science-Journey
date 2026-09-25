# Day 52 - NumPy Random Numbers & Reproducibility

## 1. Why randomness matters

Randomness is used in many data-science tasks:

- training/validation/test splits
- initializing neural-network weights
- sampling observations
- experiments and simulations
- generating synthetic datasets for testing

## 2. Your first random number

```python
import numpy as np

print(np.random.random())
```

This produces a random float between 0 and 1.

Example output:

```python
0.72638491
```

Each call produces a new random value.

## 3. Range of `random()`

`np.random.random()` produces values in the range:

- `0 <= x < 1`

This is an important convention. It never returns exactly 1.0.

## 4. Generate multiple random numbers

```python
np.random.random(5)
```

Example:

```python
array([0.12, 0.83, 0.41, 0.67, 0.29])
```

You can also create a 2D array:

```python
np.random.random((3, 4))
```

## 5. `rand()`

```python
np.random.rand(3, 4)
```

This is a historic NumPy pattern that produces random floats in `[0, 1)`. It is common in older code, but modern code often uses the `Generator` API instead.

## 6. Random integers

```python
np.random.randint(1, 10)
```

This returns one random integer in the range:

- `1 <= value < 10`

Example output:

```python
7
```

Generate several at once:

```python
np.random.randint(1, 10, size=5)
# e.g. [3, 8, 1, 5, 7]
```

## 7. Random integer matrices

```python
np.random.randint(1, 101, size=(3, 4))
```

This creates a 3x4 matrix with values from 1 to 100.

## 8. Uniform distribution

If you want continuous random values in a custom interval:

```python
np.random.uniform(10, 20, size=5)
```

Example:

```python
array([12.4, 17.8, 10.9, 19.2, 14.6])
```

The values lie between 10 and 20.

## 9. Normal distribution

A normal distribution is a bell-shaped distribution.

```python
np.random.normal()
```

This produces a single value drawn from a standard normal distribution, centered at 0 with standard deviation 1.

You can control the parameters:

```python
np.random.normal(loc=100, scale=15, size=10)
```

Where:

- `loc` = mean
- `scale` = standard deviation
- `size` = number of values

## 10. Why normal distribution matters

Normal distributions appear frequently in:

- statistics
- measurement modeling
- noise
- simulations
- machine learning

Example:

```python
scores = np.random.normal(loc=70, scale=10, size=1000)
```

This simulates exam-like scores centered around 70 with a spread of about 10.

## 11. `np.random.choice()`

```python
colors = np.array(["red", "blue", "green", "yellow"])
```

Pick a single item:

```python
np.random.choice(colors)
```

Pick multiple items:

```python
np.random.choice(colors, size=3)
```

This may repeat values by default, because sampling is done with replacement.

## 12. Sampling without replacement

```python
np.random.choice(colors, size=3, replace=False)
```

This ensures each item is selected at most once.

## 13. Sampling with probabilities

```python
choices = np.array(["A", "B", "C"])
probabilities = [0.7, 0.2, 0.1]

np.random.choice(choices, size=10, p=probabilities)
```

This uses weighted random selection.

## 14. Random seeds and reproducibility

When you run random code without control, you get different outputs each time.

```python
np.random.random()
```

This is often useful, but sometimes you need reproducibility. That is where a seed matters.

```python
np.random.seed(42)
print(np.random.random())
print(np.random.random())
```

Running the same seed again reproduces the same sequence.

```python
np.random.seed(42)
print(np.random.random())
print(np.random.random())
```

The output will be identical.

## 15. What a seed does

A seed initializes the pseudo-random generator's internal state.

- Same seed -> same sequence
- Different seed -> different sequence

The number `42` is just a convention, not magic.

## 16. Reproducibility in data science

Reproducibility is crucial because experiments can change due to randomness in:

- data splits
- model initialization
- sampling
- optimization
- augmentation

If a result cannot be reproduced, it is harder to verify, debug, and trust.

## 17. Modern NumPy random API

NumPy recommends using a dedicated generator object instead of relying on the global random state:

```python
rng = np.random.default_rng(42)
```

Then:

```python
rng.random()
rng.integers(1, 10)
rng.normal(100, 15, size=10)
```

This is cleaner and makes experiments easier to control.

## 18. Why `default_rng()` is better

Using one global random state can make different parts of a project interfere with one another.

Instead:

```python
data_rng = np.random.default_rng(42)
model_rng = np.random.default_rng(100)
```

You have separate random streams for different tasks.

## 19. Synthetic data

Random data is often used to build synthetic examples for testing and experiments.

```python
rng = np.random.default_rng(42)

scores = rng.normal(loc=70, scale=10, size=100)
```

Then you can analyze:

```python
print(np.mean(scores))
print(np.median(scores))
print(np.std(scores))
print(np.min(scores))
print(np.max(scores))
```

## 20. Realistic constraints

Normal distributions are unbounded, so they can produce impossible values such as negative ages or scores above 100.

This is a common issue in synthetic data.

```python
scores = np.clip(scores, 0, 100)
```

This keeps values within a realistic range.

## 21. Synthetic data vs reality

A generated dataset is not automatically a realistic model of the real world.

It is only an assumption-based simulation.

Data scientists must distinguish:

- a distributional assumption
- from observed evidence in the real world

## 22. Synthetic student dataset example

```python
rng = np.random.default_rng(42)

n_students = 1000

math = rng.normal(loc=70, scale=12, size=n_students)
science = rng.normal(loc=72, scale=10, size=n_students)
python = rng.normal(loc=75, scale=15, size=n_students)

math = np.clip(math, 0, 100)
science = np.clip(science, 0, 100)
python = np.clip(python, 0, 100)

scores = np.column_stack([math, science, python])
```

This creates a 2D array with shape `(1000, 3)`.

It represents 1000 students and 3 subjects.

## 23. Day 52 core workflow

The overall workflow is:

1. Generate random data
2. Inspect it
3. Transform it if needed
4. Summarize it
5. Analyze it

Example:

```python
rng = np.random.default_rng(42)

data = rng.normal(70, 10, 1000)

print(data.shape)
print(np.mean(data))
print(np.median(data))
print(np.std(data))
print(np.min(data))
print(np.max(data))
```

This is a miniature data-science workflow.

## 24. Summary

Key ideas to remember:

- randomness is useful in data science and ML
- random seeds make results reproducible
- `np.random.random()` gives floats in `[0, 1)`
- `np.random.randint()` gives random integers
- `np.random.normal()` gives values from a normal distribution
- `np.random.choice()` samples from arrays
- `np.random.default_rng()` is the modern recommended API
- generated data should respect realistic constraints
