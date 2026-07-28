# Write a program that:

# Reads the file
# Skips the header row
# Prints each employee's details in a readable format

try:
    with open("01-python/13-file-handling/employees.csv", "r") as file:
        next(file)  # Skip the header row
        for line in file:
            name, department, salary = line.strip().split(",")
            print(f"Name: {name}, Department: {department}, Salary: {salary}")
except FileNotFoundError:
    print("employees.csv not found.")
