import numpy as np


# ---------------------------------
# 1. 1D INDEXING
# ---------------------------------

arr = np.array([10, 20, 30, 40, 50])

print("First element:", arr[0])
print("Third element:", arr[2])
print("Last element:", arr[-1])


# ---------------------------------
# 2. 1D SLICING
# ---------------------------------

print("\nSlicing:")
print("First three:", arr[:3])
print("From index 2:", arr[2:])
print("Middle:", arr[1:4])
print("Every second:", arr[::2])
print("Reverse:", arr[::-1])


# ---------------------------------
# 3. 2D ARRAY
# ---------------------------------

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("\n2D Array:")
print(data)

print("\nSpecific element:")
print(data[1, 2])

print("\nFirst row:")
print(data[0])

print("\nSecond column:")
print(data[:, 1])

print("\nFirst two rows:")
print(data[:2])

print("\nFirst two columns:")
print(data[:, :2])

print("\nSubmatrix:")
print(data[1:3, 1:3])


# ---------------------------------
# 4. DATA SCIENCE EXAMPLE
# ---------------------------------

X = np.array([
    [25, 50000, 700],
    [32, 65000, 720],
    [41, 80000, 750],
    [29, 55000, 690],
    [35, 72000, 730]
])

ages = X[:, 0]
income = X[:, 1]
credit_score = X[:, 2]

print("\nAges:")
print(ages)

print("\nIncome:")
print(income)

print("\nCredit Score:")
print(credit_score)


# Select Age + Income
X_selected = X[:, 0:2]

print("\nSelected Features:")
print(X_selected)