# Write a program that:

# Takes:
# Name
# Age
# CGPA
# Determines:
# Eligible for Internship

# Criteria:

# Age ≥ 18
# CGPA ≥ 7.5

# Example Output:

# Student: Rahul

# Eligible: True


name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: "))


eligible = age >= 18 and cgpa >= 7.5

print(f"Student: {name}")
print(f"Eligible: {eligible}")

