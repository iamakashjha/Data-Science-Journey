import numpy as np

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

print("\nAdjusted Scores:")
print(adjusted_scores)
print("\nTotal Scores for Each Student:")
print(totals)
print("\nAverage Scores for Each Subject:")
print(averages)