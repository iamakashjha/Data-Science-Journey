import numpy as np


# 1. From Python list
numbers = np.array([10, 20, 30, 40, 50])

print("Array:")
print(numbers)


# 2. Zeros
zeros = np.zeros(5)

print("\nZeros:")
print(zeros)


# 3. Ones
ones = np.ones(5)

print("\nOnes:")
print(ones)


# 4. Full
constant = np.full(5, 7)

print("\nConstant:")
print(constant)


# 5. arange
sequence = np.arange(0, 20, 2)

print("\nSequence:")
print(sequence)


# 6. linspace
values = np.linspace(0, 1, 6)

print("\nEvenly spaced:")
print(values)


# 7. Data type
arr = np.array(
    [1, 2, 3],
    dtype=np.float64
)

print("\nData type:")
print(arr.dtype)