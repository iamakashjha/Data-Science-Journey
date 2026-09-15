import numpy as np

X = np.array([
    [25, 50000, 700, 5],
    [32, 65000, 720, 7],
    [41, 80000, 750, 10],
    [29, 55000, 690, 4],
    [35, 72000, 730, 8]
])


age = X[:, 0]
income = X[:, 1]
Credit_score = X[:, 2]
Years_of_experience = X[:, 3]

print("Ages:")
print(age)
print("\nIncome:")
print(income)
print("\nCredit Score:")
print(Credit_score)
print("\nYears of Experience:")
print(Years_of_experience)

input_features = X[:, :3]
print("\nInput Features:")
print(input_features)


print("\nInput Features Analysis")
input_features_analysis = {
    "Dimensions": input_features.ndim,
    "Shape": input_features.shape,
    "Total elements": input_features.size,
    "Number of samples": input_features.shape[0],
    "Number of features": input_features.shape[1]
}
for key, value in input_features_analysis.items():
    print(f"{key}: {value}")

