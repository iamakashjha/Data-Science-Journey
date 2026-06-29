marks = [78, 85, 92, 67, 88]

# Program should:

# Print all marks
# Find highest mark
# Find lowest mark
# Calculate average manually
# Add a new mark
# Remove the lowest mark
# Print the updated list

# This is similar to processing a small dataset.

for mark in marks:
    print(mark)  # Print all marks

print("Highest mark:", max(marks))  # Find highest mark
print("Lowest mark:", min(marks))  # Find lowest mark
# Calculate average manually
total = 0
for mark in marks:
    total += mark
average = total / len(marks)
print("Average mark:", average)  # Print average

marks.remove(min(marks))  # Remove the lowest mark
print("Updated list:", marks)  # Print the updated list