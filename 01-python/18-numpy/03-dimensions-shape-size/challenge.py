import numpy as np


data = np.array([
    [25, 50000, 700],
    [32, 65000, 720],
    [41, 80000, 750],
    [29, 55000, 690],
    [35, 72000, 730]
])


print("Dataset:")
print(data)

print("\nDataset Analysis")
print("----------------")
print("Dimensions:", data.ndim)
print("Shape:", data.shape)
print("Total elements:", data.size)
print("Number of samples:", data.shape[0])
print("Number of features:", data.shape[1])