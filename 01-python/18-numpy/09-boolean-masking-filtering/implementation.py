import numpy as np


# -----------------------------------------
# 1. BOOLEAN ARRAY
# -----------------------------------------

ages = np.array([18, 22, 27, 31, 16, 40])
mask = ages > 25

print("Mask:")
print(mask)


# -----------------------------------------
# 2. BOOLEAN FILTERING
# -----------------------------------------

print("\nAges greater than 25:")
print(ages[ages > 25])


# -----------------------------------------
# 3. AND CONDITION
# -----------------------------------------

print("\nAges between 20 and 35:")
mask = (ages >= 20) & (ages <= 35)
print(ages[mask])


# -----------------------------------------
# 4. OR CONDITION
# -----------------------------------------

print("\nAges below 20 or above 35:")
mask = (ages < 20) | (ages > 35)
print(ages[mask])


# -----------------------------------------
# 5. NOT CONDITION
# -----------------------------------------

print("\nAges not greater than 25:")
mask = ~(ages > 25)
print(ages[mask])


# -----------------------------------------
# 6. np.where()
# -----------------------------------------

scores = np.array([45, 72, 88, 55, 91])
result = np.where(scores >= 60, "Pass", "Fail")

print("\nPass/Fail:")
print(result)


# -----------------------------------------
# 7. np.where() INDICES
# -----------------------------------------

indices = np.where(scores >= 80)
print("\nIndices where score >= 80:")
print(indices)


# -----------------------------------------
# 8. ANY
# -----------------------------------------

print("\nAny score above 90:")
print(np.any(scores > 90))


# -----------------------------------------
# 9. ALL
# -----------------------------------------

print("\nAll scores above 40:")
print(np.all(scores > 40))


# -----------------------------------------
# 10. CONDITIONAL ASSIGNMENT
# -----------------------------------------

clean_scores = scores.copy()
clean_scores[clean_scores < 60] = 0

print("\nScores after replacement:")
print(clean_scores)


# -----------------------------------------
# 11. DATASET FILTERING
# -----------------------------------------

data = np.array([
    [25, 50000, 700, 1],
    [32, 65000, 720, 0],
    [41, 80000, 750, 1],
    [29, 55000, 690, 0],
    [35, 72000, 730, 1],
    [45, 90000, 780, 1]
])

mask = (
    (data[:, 0] > 30) &
    (data[:, 1] > 60000) &
    (data[:, 2] > 720)
)

filtered_data = data[mask]

print("\nFiltered dataset:")
print(filtered_data)

print("\nMask:")
print(mask)

print("\nNumber of matching rows:")
print(mask.sum())
