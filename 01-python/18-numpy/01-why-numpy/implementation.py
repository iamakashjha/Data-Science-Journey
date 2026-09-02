import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Array:", numbers)

print("Type:", type(numbers))

print("Data type:", numbers.dtype)

print("Double:", numbers * 2)

print("Add 5:", numbers + 5)

print("Total:", np.sum(numbers))

print("Average:", np.mean(numbers))

print("Maximum:", np.max(numbers))

print("Minimum:", np.min(numbers))