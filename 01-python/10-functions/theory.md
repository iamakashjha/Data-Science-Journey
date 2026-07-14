## 1. What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing:
```
print("Welcome to Data Science!")
print("Welcome to Data Science!")
print("Welcome to Data Science!")
```
Create a function:
```
def greet():
    print("Welcome to Data Science!")
```
Call it:
```
greet()
greet()
greet()
```
Output:
```
Welcome to Data Science!
Welcome to Data Science!
Welcome to Data Science!
```

## 2. Functions with Parameters

Functions become useful when they accept input.
```
def greet(name):
    print(f"Hello, {name}!")
```
Call:
```
greet("Rahul")
greet("Alice")
```
Output:
```
Hello, Rahul!
Hello, Alice!
```


## 3. Functions with Return Values

Printing is useful.

Returning is powerful.
```
def square(number):
    return number * number
```
Now:
```
result = square(5)

print(result)
```
Output:
```
25
```
Think of it this way:

- `print()` shows something.
- `return` gives the value back to the caller.


## 4. Multiple Parameters
```
def add(a, b):
    return a + b

print(add(10, 20))
```
Output:
```
30
```

## 5. Default Parameters

```
def greet(name="Student"):
    print(f"Hello, {name}")
```

Calls:
```
greet()

greet("Rahul")
```
Output:
```
Hello, Student
Hello, Rahul
```