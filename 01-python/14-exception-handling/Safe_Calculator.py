# Create a calculator that:

# Accepts two numbers from the user
# Lets the user choose:
# Addition
# Subtraction
# Multiplication
# Division
# Handles:
# Invalid numbers
# Division by zero
# Invalid operation choices

def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        return "Invalid input. Please enter valid numbers."

    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

    if operation == '1':
        return f"The result of addition is: {num1 + num2}"
    elif operation == '2':
        return f"The result of subtraction is: {num1 - num2}"
    elif operation == '3':
        return f"The result of multiplication is: {num1 * num2}"
    elif operation == '4':
        try:
            result = num1 / num2
            return f"The result of division is: {result}"
        except ZeroDivisionError:
            return "Cannot divide by zero."
    else:
        return "Invalid operation choice."
