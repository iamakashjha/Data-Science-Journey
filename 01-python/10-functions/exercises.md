### 1. What is a function?
A function is a reusable block of code that performs a specific task. It can take inputs (parameters), process them, and optionally return a result. Functions help avoid code duplication and make programs more organized.

### 2. Difference between parameters and arguments?
**Parameters** are the variables defined in the function definition.
**Arguments** are the actual values passed to the function when it is called.


### 3. Difference between print() and return?
`print()` displays the output on the screen but does not send it back to the caller.

`return` sends a value back to the caller and immediately exits the function.


### 4. Why are functions important?
Functions are important because they:

- Reduce code duplication.
- Improve code readability.
- Make programs easier to test and maintain.
- Allow code reuse.


### 5. What is variable scope?
**Variable scope** determines where a variable can be accessed.

- A local variable is created inside a function and can only be used there.
- A global variable is defined outside a function and can be accessed throughout the program. To modify a global variable inside a function, use the global keyword.


### 6. When would you use a lambda function?
A lambda function is used when you need a small, anonymous function for a short period, usually as an argument to functions like `map()`, `filter()`, or `sorted()`. It is useful for simple operations that don't require a full function definition.