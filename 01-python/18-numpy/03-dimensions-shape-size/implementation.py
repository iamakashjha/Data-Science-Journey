import numpy as np


# 1D array
arr_1d = np.array([10, 20, 30, 40])

print("1D Array:")
print(arr_1d)

print("ndim:", arr_1d.ndim)
print("shape:", arr_1d.shape)
print("size:", arr_1d.size)
print("length:", len(arr_1d))


# 2D array
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr_2d)

print("ndim:", arr_2d.ndim)
print("shape:", arr_2d.shape)
print("size:", arr_2d.size)
print("length:", len(arr_2d))


# 3D array
arr_3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("\n3D Array:")
print(arr_3d)

print("ndim:", arr_3d.ndim)
print("shape:", arr_3d.shape)
print("size:", arr_3d.size)


# Reshaping
arr = np.arange(1, 7)

print("\nOriginal:")
print(arr)
print("Shape:", arr.shape)

reshaped = arr.reshape(2, 3)

print("\nReshaped:")
print(reshaped)
print("Shape:", reshaped.shape)


# Column vector
values = np.array([10, 20, 30, 40, 50])

column = values.reshape(-1, 1)

print("\nColumn Vector:")
print(column)
print("Shape:", column.shape)