# 💼 Interview Questions

### 1. Why would you use a class instead of a dictionary to represent a student?

A dictionary is useful for simple data representation, while a class allows us to combine data with related behavior. A Student object can contain both attributes such as marks and methods such as `average()` and `grade()`.

### 2. What is the benefit of splitting this project into multiple modules?

It separates responsibilities.

**For example:**
```
student.py          → Student behavior
statistics_utils.py → Calculations
file_utils.py       → File operations
main.py             → Application flow
```
This improves readability, testing, reuse, and maintenance.

### 3. Why should you validate marks before storing them?

Because invalid data can produce incorrect analysis.

**For example:**
```
Math = 150
```
would produce misleading statistics and potentially affect downstream models.

Data validation is an important part of real-world Data Science pipelines.

### 4. Why use JSON instead of simply storing Python objects in a text file?

JSON is a standardized, human-readable data format that can be exchanged between different programs and programming languages. It's also commonly used by APIs.

### 5. What happens if students is empty when calculating the average?

You should handle that case explicitly to avoid division by zero.

**For example:**
```
if not students:
    return 0
```
This is an example of defensive programming.