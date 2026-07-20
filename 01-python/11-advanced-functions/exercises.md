### 1. Difference between positional and keyword arguments?
**Positional arguments** are passed based on their order in the function call.

**Keyword arguments** are passed using the parameter name, so the order doesn't matter.

### 2. What problem does *args solve?
`*args` allows a function to accept a **variable number of positional arguments**, so you don't need to know how many arguments will be passed in advance.
```
def add(*args):
    return sum(args)

print(add(1, 2, 3))      # 6
print(add(5, 10, 15, 20)) # 50
```
**Use case:** When the number of inputs is unknown.

### 3. What problem does **kwargs solve?
`**kwargs` allows a function to accept a **variable number of keyword arguments** as a dictionary.


### 4. Why should every function have a docstring?
A **docstring** explains what a function does, its parameters, return value, and usage. It improves readability, maintainability, and automatically generates documentation.

```
def square(num):
    """
    Returns the square of a number.

    Args:
        num (int or float): Input number.

    Returns:
        int or float: Square of the input.
    """
    return num * num
```

### 5. What are type hints?
Type hints specify the **expected data types** of function parameters and return values. They improve code readability and help IDEs and static type checkers detect errors.

Example:
```
def add(a: int, b: int) -> int:
    return a + b
```
Here:

**a:** int → a should be an integer.  
**b:** int → b should be an integer.  
**->** int → function returns an integer.

Type hints are not enforced at runtime; they are mainly for documentation and tooling.

### 6. When is recursion useful?

Recursion is useful when a problem can be broken down into **smaller instances of the same problem.** A recursive function calls itself until a base case is reached.

**Common use cases:**

- Tree and graph traversal
- Directory/file traversal
- Factorial and Fibonacci
- Binary search
- Divide-and-conquer algorithms (e.g., Merge Sort, Quick Sort)

Example (Factorial):
```
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```
