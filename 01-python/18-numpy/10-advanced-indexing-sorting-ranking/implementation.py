import numpy as np


# ============================================================
# 1. INTEGER ARRAY INDEXING
# ============================================================

scores = np.array([72, 91, 65, 88, 95])

indices = np.array([4, 1, 3])

selected_scores = scores[indices]

print("Selected scores:")
print(selected_scores)


# ============================================================
# 2. SORT VS ARGSORT
# ============================================================

print("\nOriginal:")
print(scores)

print("\nSorted values:")
print(np.sort(scores))

print("\nSorting indices:")
print(np.argsort(scores))


# ============================================================
# 3. DESCENDING ORDER
# ============================================================

descending_order = np.argsort(scores)[::-1]

print("\nDescending order:")
print(scores[descending_order])


# ============================================================
# 4. ARGMAX / ARGMIN
# ============================================================

max_index = np.argmax(scores)
min_index = np.argmin(scores)

print("\nMaximum score:")
print(scores[max_index])

print("Maximum score index:")
print(max_index)

print("\nMinimum score:")
print(scores[min_index])

print("Minimum score index:")
print(min_index)


# ============================================================
# 5. STUDENT RANKING
# ============================================================

students = np.array([
    "Akash",
    "Rahul",
    "Priya",
    "Neha",
    "Aman"
])

student_scores = np.array([
    82,
    95,
    76,
    91,
    88
])

ranking = np.argsort(student_scores)[::-1]

print("\nStudent ranking:")
for position in ranking:
    print(students[position], student_scores[position])


# ============================================================
# 6. TOP 3
# ============================================================

top_3 = ranking[:3]

print("\nTop 3 students:")
for position in top_3:
    print(students[position], student_scores[position])


# ============================================================
# 7. 2D ARRAY SORTING
# ============================================================

marks = np.array([
    [80, 90, 70],
    [60, 85, 95],
    [75, 65, 88]
])

print("\nOriginal matrix:")
print(marks)

print("\nSort across each row:")
print(np.sort(marks, axis=1))

print("\nSort down each column:")
print(np.sort(marks, axis=0))


# ============================================================
# 8. PAIRED INTEGER INDEXING
# ============================================================

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

rows = np.array([0, 1, 2])
cols = np.array([2, 0, 1])

selected = data[rows, cols]

print("\nSelected coordinates:")
print(selected)


# ============================================================
# 9. PARTITION
# ============================================================

values = np.array([
    91, 72, 88, 95, 65, 84, 79
])

partitioned = np.partition(values, 2)

print("\nOriginal values:")
print(values)

print("\nPartitioned:")
print(partitioned)


# ============================================================
# 10. ARGPARTITION
# ============================================================

partition_indices = np.argpartition(values, 2)

print("\nPartition indices:")
print(partition_indices)

print("\nValues using partition indices:")
print(values[partition_indices])
