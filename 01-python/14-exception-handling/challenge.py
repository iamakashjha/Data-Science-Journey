"""
Tasks:
Convert values to integers
Ignore invalid values
Calculate:
Total
Average
Highest
Lowest
Hint:
Use try and except inside a loop.
"""



marks = [
    "90",
    "85",
    "abc",
    "78",
    "100",
    "xyz"
]

new_marks = []

for mark in marks:
    try:
        mark_int = int(mark)
        new_marks.append(mark_int)
    except ValueError:
        print(f"Ignoring invalid mark: {mark}")

print(f"Total: {sum(new_marks)}")
print(f"Average: {sum(new_marks) / len(new_marks)}")
print(f"Highest: {max(new_marks)}")
print(f"Lowest: {min(new_marks)}")


# Requirements:

# Otherwise, return the square root.
# Raise a ValueError if the number is negative.

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    else:
        return number ** 0.5

print(calculate_square_root(16))
print(calculate_square_root(-9))