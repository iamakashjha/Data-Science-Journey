# Day 29 — Python Data Types & Variables
Goal: Learn the building blocks of every Python program.

By the end of today, you should understand:

- Variables
- Basic data types
- Type conversion
- Why data types matter in Data Science

## Step 1 — Variables

A variable stores a value.
```
name = "Alice"
age = 25
salary = 50000
```
Think of variables as labels attached to data.

## Step 2 — Core Data Types
```
name = "Alice"      # str
age = 25            # int
height = 5.8        # float
is_student = True   # bool
```
Check the type:
```
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

### Why This Matters in Data Science

Imagine a dataset:
```
Name	Age	Salary	Purchased
Alice	25	50000	True
```
Python represents this as:
```
name = "Alice"
age = 25
salary = 50000.0
purchased = True
```
Every dataset is made up of different data types.

## Step 3 — Type Conversion

Sometimes data arrives as text.
```
age = "25"

print(type(age))
```
Convert it:
```
age = int(age)

print(type(age))
```

### Example
```
price = "199.99"

price = float(price)

print(price * 2)
```

## Step 4 — User Input
```
name = input("Enter your name: ")

print(name)
```
Notice:
```
age = input("Enter age: ")

print(type(age))
```
Everything from `input()` is a string.

Convert it:
```
age = int(age)
```

### Real Data Science Exercise

Suppose data comes from a CSV file:
```
Name,Age,Salary
Alice,25,50000
Bob,30,70000
```

**Questions:**
- Which columns are strings?

Name columns is in string format.  

- Which are integers?

Age and Salary columns are integer.

- Which might be floats?

There is no float columnns available in the data.

- Why is choosing the correct type important?
Choosing the correct data important because we can perform the necessary calculation or appropriate operations.

Write your answers in `theory.md`