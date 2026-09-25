import numpy as np


# ---------------------------------
# 1. SCALAR OPERATIONS
# ---------------------------------

arr = np.array([10, 20, 30, 40])

print("Original:")
print(arr)

print("\nAddition:")
print(arr + 5)

print("\nSubtraction:")
print(arr - 5)

print("\nMultiplication:")
print(arr * 2)

print("\nDivision:")
print(arr / 10)

print("\nPower:")
print(arr ** 2)


# ---------------------------------
# 2. ARRAY OPERATIONS
# ---------------------------------

sales = np.array([100, 200, 300])
costs = np.array([60, 120, 180])

profit = sales - costs

print("\nProfit:")
print(profit)


# ---------------------------------
# 3. VECTOR OPERATIONS
# ---------------------------------

x = np.array([1, 2, 3, 4, 5])

y = 2 * x + 10

print("\nVectorized formula:")
print(y)


# ---------------------------------
# 4. COMPARISONS
# ---------------------------------

scores = np.array([45, 67, 89, 32, 95])

print("\nScores > 60:")
print(scores > 60)

print("\nScores > 60:")
print(scores[scores > 60])


# ---------------------------------
# 5. BOOLEAN CONDITIONS
# ---------------------------------

mask = (scores >= 60) & (scores <= 90)

print("\nScores between 60 and 90:")
print(scores[mask])


# ---------------------------------
# 6. BROADCASTING
# ---------------------------------

X = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nX + 10:")
print(X + 10)


# ---------------------------------
# 7. 1D BROADCASTING
# ---------------------------------

offset = np.array([1, 2, 3])

result = X + offset

print("\nX + offset:")
print(result)


# ---------------------------------
# 8. COLUMN BROADCASTING
# ---------------------------------

column = np.array([
    [1],
    [2],
    [3]
])

result = X + column

print("\nX + column:")
print(result)


# ---------------------------------
# 9. SHAPE INSPECTION
# ---------------------------------

print("\nShapes:")
print("X:", X.shape)
print("offset:", offset.shape)
print("column:", column.shape)