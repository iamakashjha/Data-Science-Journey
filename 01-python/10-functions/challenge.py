# Challenge

# Dataset:

# sales = [1200, 1800, 950, 2400, 1500]

# Create functions:

# calculate_total()

# calculate_average()

# find_maximum()

# find_minimum()

# Don't use Python's built-in functions like sum(), max(), or min().


sales = [1200, 1800, 950, 2400, 1500]

def calculate_total(sales):
    total = 0
    for sale in sales:
        total += sale
    return total

def calculate_average(sales):
    total = calculate_total(sales)
    return total / len(sales)

def find_maximum(sales):
    maximum = sales[0]
    for sale in sales:
        if sale > maximum:
            maximum = sale
    return maximum

def find_minimum(sales):
    minimum = sales[0]
    for sale in sales:
        if sale < minimum:
            minimum = sale
    return minimum


print("Total Sales:", calculate_total(sales))
print("Average Sales:", calculate_average(sales))
print("Maximum Sale:", find_maximum(sales))
print("Minimum Sale:", find_minimum(sales))


def calculate(a, b):
    return a + b, a - b

total, difference = calculate(10, 5)

print(total)
print(difference)