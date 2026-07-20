def calculate_statistics(*numbers):
    """
    Calculate basic statistics.

    Returns:
        tuple: (total, average)
    """

    total = sum(numbers)
    average = total / len(numbers)

    return total, average


total, average = calculate_statistics(
    10, 20, 30, 40
)

print("Total:", total)
print("Average:", average)