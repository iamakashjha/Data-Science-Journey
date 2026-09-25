import numpy as np


# ---------------------------------
# 1. BASIC RANDOM NUMBERS
# ---------------------------------

print("Random float:")
print(np.random.random())


# ---------------------------------
# 2. RANDOM ARRAY
# ---------------------------------

print("\nRandom array:")
print(np.random.random(5))


# ---------------------------------
# 3. RANDOM INTEGERS
# ---------------------------------

print("\nRandom integers:")
print(np.random.randint(1, 10, size=5))


# ---------------------------------
# 4. UNIFORM DISTRIBUTION
# ---------------------------------

print("\nUniform values:")
print(np.random.uniform(10, 20, size=5))


# ---------------------------------
# 5. NORMAL DISTRIBUTION
# ---------------------------------

print("\nNormal values:")
normal_data = np.random.normal(loc=100, scale=15, size=10)
print(normal_data)


# ---------------------------------
# 6. RANDOM CHOICE
# ---------------------------------

colors = np.array(["red", "blue", "green", "yellow"])

print("\nRandom choice:")
print(np.random.choice(colors))


# ---------------------------------
# 7. RANDOM CHOICE WITHOUT REPLACEMENT
# ---------------------------------

print("\nChoice without replacement:")
print(np.random.choice(colors, size=3, replace=False))


# ---------------------------------
# 8. REPRODUCIBILITY
# ---------------------------------

np.random.seed(42)
a = np.random.random(5)

np.random.seed(42)
b = np.random.random(5)

print("\nSame seed:")
print(a)
print(b)
print("Equal:", np.array_equal(a, b))


# ---------------------------------
# 9. MODERN GENERATOR API
# ---------------------------------

rng = np.random.default_rng(42)

print("\nGenerator random:")
print(rng.random(5))

print("\nGenerator integers:")
print(rng.integers(1, 101, size=5))

print("\nGenerator normal:")
print(rng.normal(loc=70, scale=10, size=5))


# ---------------------------------
# 10. SYNTHETIC DATASET
# ---------------------------------

n_students = 1000

math = rng.normal(70, 12, n_students)
science = rng.normal(72, 10, n_students)
python = rng.normal(75, 15, n_students)

math = np.clip(math, 0, 100)
science = np.clip(science, 0, 100)
python = np.clip(python, 0, 100)

scores = np.column_stack([math, science, python])

print("\nDataset shape:")
print(scores.shape)

print("\nSubject means:")
print(np.mean(scores, axis=0))

print("\nSubject standard deviations:")
print(np.std(scores, axis=0))

print("\nSubject minimum:")
print(np.min(scores, axis=0))

print("\nSubject maximum:")
print(np.max(scores, axis=0))
