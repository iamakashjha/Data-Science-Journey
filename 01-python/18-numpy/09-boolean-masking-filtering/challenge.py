import numpy as np

# -------------------------------------
# 1. Customer dataset
# -------------------------------------

data = np.array([
    [22, 35000, 680, 0],
    [28, 52000, 710, 1],
    [35, 75000, 740, 1],
    [42, 90000, 780, 1],
    [31, 62000, 720, 0],
    [26, 48000, 700, 1],
    [39, 85000, 760, 1],
    [47, 95000, 790, 0]
])

# Task 1: Age > 30
mask_age = data[:, 0] > 30
print("Age > 30:")
print(data[mask_age])

# Task 2: Income >= 70000 and Credit Score >= 750
mask_income_score = (data[:, 1] >= 70000) & (data[:, 2] >= 750)
print("\nIncome >= 70000 and Credit Score >= 750:")
print(data[mask_income_score])

# Task 3: Age < 25 or Age > 40
mask_age_extreme = (data[:, 0] < 25) | (data[:, 0] > 40)
print("\nAge < 25 or Age > 40:")
print(data[mask_age_extreme])

# Task 4: did not purchase
mask_not_purchased = data[:, 3] == 0
print("\nDid not purchase:")
print(data[mask_not_purchased])

# Task 5: count customers with Credit Score >= 720
mask_score = data[:, 2] >= 720
print("\nNumber with Credit Score >= 720:")
print(mask_score.sum())

# Task 6: classify income
income_categories = np.where(data[:, 1] >= 70000, "High Income", "Regular Income")
print("\nIncome classification:")
print(income_categories)

# Task 7: indices with credit score > 750
credit_indices = np.where(data[:, 2] > 750)
print("\nIndices with Credit Score > 750:")
print(credit_indices)

# -------------------------------------
# 2. Advanced challenge
# -------------------------------------

rng = np.random.default_rng(42)
data2 = rng.integers(1, 100, size=(1000, 5))

print("\nAdvanced challenge counts:")
print("A: Age > 50:", np.sum(data2[:, 0] > 50))
print("B: Age > 50 and Income > 70:", np.sum((data2[:, 0] > 50) & (data2[:, 1] > 70)))
print("C: Credit Score > 80 or Spending Score > 90:", np.sum((data2[:, 2] > 80) | (data2[:, 3] > 90)))
print("D: Any row with Income > 99:", np.any(data2[:, 1] > 99))
print("E: All rows with Age >= 1:", np.all(data2[:, 0] >= 1))

income_flag = np.where(data2[:, 1] >= 70, 1, 0)
print("F: income classification:", income_flag[:10])
