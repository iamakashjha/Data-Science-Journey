import numpy as np

data = [5, 7, 9, 12, 15, 18, 20, 25, 30]

q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)

iqr = q3 - q1

print("Q1:", q1)
print("Median:", q2)
print("Q3:", q3)
print("IQR:", iqr)