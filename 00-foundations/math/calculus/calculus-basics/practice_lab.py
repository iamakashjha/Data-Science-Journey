import math

# Function
def f(x):
    return x**2 + 2*x + 1

# Values
for x in range(5):
    print(f"x = {x}")
    print("f(x) =", f(x))

    # Derivative intuition
    derivative = 2*x + 2
    print("Approx Slope:", derivative)

    print("-" * 20)