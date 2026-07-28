
# Write a program that:

# Reads all marks
# Converts them to integers
# Calculates:
# Total
# Average
# Highest mark
# Lowest mark

file = open("01-python/13-file-handling/marks.txt", "r")

marks = []

for line in file:
    marks.append(int(line.strip()))

file.close()

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Highest mark: {highest}")
print(f"Lowest mark: {lowest}")
