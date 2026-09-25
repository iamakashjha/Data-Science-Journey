import numpy as np

# ---------------------------------
# 1. Generate synthetic employee dataset
# ---------------------------------

rng = np.random.default_rng(42)

n_employees = 1000

age = rng.normal(35, 8, n_employees)
experience = rng.normal(8, 5, n_employees)
salary = rng.normal(80000, 20000, n_employees)

# Apply sensible constraints
age = np.clip(age, 18, 80)
experience = np.clip(experience, 0, 40)
salary = np.clip(salary, 0, 200000)

employees = np.column_stack([age, experience, salary])

print("Dataset shape:")
print(employees.shape)

print("\nMean by feature:")
print(np.mean(employees, axis=0))

print("\nMedian by feature:")
print(np.median(employees, axis=0))

print("\nMinimum by feature:")
print(np.min(employees, axis=0))

print("\nMaximum by feature:")
print(np.max(employees, axis=0))

print("\nStandard deviation by feature:")
print(np.std(employees, axis=0))

feature_std = np.std(employees, axis=0)
feature_with_largest_std = np.argmax(feature_std)
print("\nFeature with largest standard deviation:")
print(feature_with_largest_std)

# ---------------------------------
# 2. Advanced challenge: independent generators
# ---------------------------------

rng1 = np.random.default_rng(42)
rng2 = np.random.default_rng(42)

a = rng1.normal(size=10)
b = rng2.normal(size=10)

print("\nArray equality with same seed:")
print(np.array_equal(a, b))

rng3 = np.random.default_rng(100)
c = rng3.normal(size=10)

print("\nArray equality with different seed:")
print(np.array_equal(a, c))
