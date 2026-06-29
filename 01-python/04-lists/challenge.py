expenses = [1200, 800, 1500, 600, 900]

# Tasks:

# Add a new expense of ₹2000
# Remove ₹600
# Print:
# Total expenses
# Highest expense
# Lowest expense
# Average expense (without using sum())

# Hint: Use a loop to calculate the total.

expenses.append(2000)  # Add a new expense of ₹2000
expenses.remove(600)  # Remove ₹600
print("Total expenses:", sum(expenses))  # Total expenses
print("Highest expense:", max(expenses))  # Highest expense
print("Lowest expense:", min(expenses))  # Lowest expense
# Calculate average expense without using sum()
total = 0
for expense in expenses:
    total += expense
average = total / len(expenses)
print("Average expense:", average)  # Average expense