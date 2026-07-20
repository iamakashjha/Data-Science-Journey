from math_utils import calculate_average, calculate_total, find_maximum, find_minimum, is_even, is_prime

x = [1, 2, 3, 4, 5]
print("Average:", calculate_average(x))
print("Total:", calculate_total(x))
print("Maximum:", find_maximum(x))
print("Minimum:", find_minimum(x))
print("Is 4 even?", is_even(4))
print("Is 7 prime?", is_prime(7))


def clean_customer_names(names: list) -> list:
    """Clean and standardize customer names."""

    cleaned = []

    for name in names:
        cleaned.append(name.strip().title())

    return cleaned