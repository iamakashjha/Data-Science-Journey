# Day 52 Notes

## Random generation basics

```python
import numpy as np

np.random.random()                 # float in [0, 1)
np.random.random(5)                # 5 random floats
np.random.randint(1, 10)           # random integer in [1, 10)
np.random.randint(1, 10, size=5)   # 5 random integers
np.random.uniform(10, 20, size=5)  # values in [10, 20)
np.random.normal(loc=70, scale=10, size=100)
```

## Sampling

```python
colors = np.array(["red", "blue", "green", "yellow"])

np.random.choice(colors)
np.random.choice(colors, size=3)
np.random.choice(colors, size=3, replace=False)
```

## Reproducibility

```python
np.random.seed(42)
a = np.random.random(5)

np.random.seed(42)
b = np.random.random(5)

print(a)
print(b)
print(np.array_equal(a, b))  # True
```

## Modern API

```python
rng = np.random.default_rng(42)

rng.random(5)
rng.integers(1, 101, size=5)
rng.normal(70, 10, size=5)
rng.choice(["A", "B", "C"], size=3, replace=False)
```

## Key reminders

- same seed => same sequence
- different seed => different sequence
- reproducibility helps debugging and experimentation
- generated data may need clipping or constraints
- separate generators make large projects easier to reason about
