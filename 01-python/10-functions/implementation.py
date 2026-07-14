def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


marks = [85, 90, 78, 95]

average = calculate_average(marks)

print("Average:", average)