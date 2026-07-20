## 1. Positional vs Keyword Arguments
**Positional Arguments**

The order matters.
```
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce("Rahul", 22)
```

**Keyword Arguments**

The order doesn't matter.

```
introduce(age=22, name="Rahul")
```

This makes code much more readable.


## 2. Default Arguments

Provide default values when an argument isn't supplied.
```
def greet(name="Student"):
    print(f"Hello, {name}")

greet()
greet("Rahul")
```
Output:
```
Hello, Student
Hello, Rahul
```

## 3. Variable-Length Arguments (*args)

Sometimes you don't know how many arguments you'll receive.
```
def calculate_total(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(calculate_total(10, 20, 30))
print(calculate_total(5, 10))
```
Output:
```
60
15
```
*args collects positional arguments into a tuple.


## 4. Keyword Variable Arguments (**kwargs)

Accept any number of keyword arguments.
```
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(
    name="Rahul",
    age=22,
    cgpa=8.9
)
```
Output:
```
name: Rahul
age: 22
cgpa: 8.9
```
**kwargs collects keyword arguments into a dictionary.


## 5. Type Hints

Type hints improve readability and editor support.
```
def calculate_average(numbers: list) -> float:
    return sum(numbers) / len(numbers)
```
This means:

- Input should be a list
- Output should be a float

Python doesn't enforce this automatically, but it helps humans and tools.


## 6. Docstrings

Every professional function should explain what it does.
```
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
        numbers (list): List of numeric values.

    Returns:
        float: Average value.
    """
    return sum(numbers) / len(numbers)
```
Anyone using your function can immediately understand it.

## 7. Recursion (Introduction)

A recursive function calls itself.

Example:
```
def countdown(n):
    if n == 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)

countdown(5)
```

