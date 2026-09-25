# Mini Project — Sales Revenue Calculator

import numpy as np

quantity = np.array([
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40]
])

price = np.array([100, 200, 300])

revenue = quantity * price

print("Revenue:")
print(revenue)

total_revenue = revenue.sum()
print("\nTotal revenue:")
print(total_revenue)


# Bonus challenge: student score adjustment
scores = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 95],
    [55, 65, 70]
])

bonus = np.array([5, 3, 2])
adjusted_scores = scores + bonus
totals = adjusted_scores.sum(axis=1)
averages = adjusted_scores.mean(axis=0)

print("\nAdjusted scores:")
print(adjusted_scores)

print("\nStudent totals:")
print(totals)

print("\nSubject averages:")
print(averages)