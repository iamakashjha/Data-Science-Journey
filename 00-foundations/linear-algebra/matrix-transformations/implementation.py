import numpy as np

S = np.array([
    [2, 0],
    [0, 2]
])

v = np.array([
    [2],
    [3]
])

result = S @ v

print(result)


# Try changing the scaling factor to 0.5 or 3 and observe the result.