def divide(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."

    else:
        return result


print(divide(20, 5))
print(divide(20, 0))