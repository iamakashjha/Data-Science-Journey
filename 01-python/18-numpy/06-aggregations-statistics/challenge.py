import numpy as np

# ---------------------------------
# 1. STUDENT PERFORMANCE ANALYSIS
# ---------------------------------

scores = np.array([
    [85, 90, 78],
    [72, 88, 91],
    [90, 76, 85],
    [65, 70, 72],
    [95, 92, 96]
])

subject_means = np.mean(scores, axis=0)
student_means = np.mean(scores, axis=1)
subject_max = np.max(scores, axis=0)
subject_min = np.min(scores, axis=0)
subject_std = np.std(scores, axis=0)
student_totals = np.sum(scores, axis=1)
best_student_index = np.argmax(student_totals)

print("Student score matrix:")
print(scores)
print("\nAverage score per subject:")
print(subject_means)
print("\nAverage score per student:")
print(student_means)
print("\nHighest score in each subject:")
print(subject_max)
print("\nLowest score in each subject:")
print(subject_min)
print("\nStandard deviation per subject:")
print(subject_std)
print("\nTotal score of each student:")
print(student_totals)
print("\nStudent with the highest total:")
print(best_student_index)


# ---------------------------------
# 2. DATASET SUMMARY CHALLENGE
# ---------------------------------

X = np.array([
    [25, 50000, 700],
    [32, 65000, 720],
    [41, 80000, 750],
    [29, 55000, 690],
    [35, 72000, 730],
    [45, 90000, 780]
])

feature_names = ["Age", "Income", "Credit Score"]
summary = np.array([
    [X[:, i].mean(), np.median(X[:, i]), X[:, i].min(), X[:, i].max(), X[:, i].std()]
    for i in range(X.shape[1])
])

print("\nDataset summary:")
print("Feature         Mean      Median     Min     Max      Std")
for i, name in enumerate(feature_names):
    print(f"{name:12} {summary[i, 0]:>9.2f} {summary[i, 1]:>9.2f} {summary[i, 2]:>7.2f} {summary[i, 3]:>7.2f} {summary[i, 4]:>7.2f}")
