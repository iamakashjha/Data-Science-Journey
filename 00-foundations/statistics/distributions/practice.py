import numpy as np

marks = np.array([70, 75, 80, 85, 95, 300])

print("Mean:", np.mean(marks))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))


# Observe: one outlier changes average heavily.