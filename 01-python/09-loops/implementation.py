students = {
    "Rahul": 88,
    "Alice": 91,
    "Bob": 76
}

for name, marks in students.items():
    print(f"{name}: {marks}")

print()

numbers = [2, 4, 6, 8, 10]

total = 0

for number in numbers:
    total += number

print("Total:", total)
print("Average:", total / len(numbers))