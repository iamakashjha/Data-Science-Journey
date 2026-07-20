# Functions:
# calculate_average()
# calculate_total()
# find_maximum()
# find_minimum()
# is_even()
# is_prime()

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def calculate_total(numbers):
    return sum(numbers)

def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)

def find_minimum(numbers):
    if not numbers:
        return None
    return min(numbers)

def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
