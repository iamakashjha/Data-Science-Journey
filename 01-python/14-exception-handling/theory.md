### 1. What is an Exception?

An exception is an error that occurs while a program is running.

Example:

```python
number = 10 / 0
```

Output:

```
ZeroDivisionError: division by zero
```

Without exception handling, the program stops immediately.

### 2. Using try and except

```python
try:
    number = 10 / 0

except ZeroDivisionError:
    print("You cannot divide by zero.")
```

Output:

```
You cannot divide by zero.
```

The program continues running instead of crashing.

### 3. Handling Invalid User Input

```python
try:
    age = int(input("Enter your age: "))
    print(age)

except ValueError:
    print("Please enter a valid number.")
```

If the user enters:

```
twenty
```

Output:

```
Please enter a valid number.
```

### 4. Catching Multiple Exceptions

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

### 5. Using else

The else block runs only if no exception occurs.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)

```

### 6. Using finally

The finally block always executes, whether an exception occurs or not.

```python
try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program finished.")

```

Common use cases:

- Closing files
- Releasing resources
- Cleaning up

### 7. Raising Your Own Exceptions

Sometimes your program should create an exception.
```
age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")
```

Output:

```
ValueError: Age cannot be negative.
```