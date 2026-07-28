### 1. What is File Handling?

File handling allows a Python program to store and retrieve data from your computer.

Instead of keeping data only in memory, you can save it permanently.

Example:
```
students.csv
```
```
Name,Marks
Rahul,88
Alice,91
Bob,76
```

### 2. Opening a File

Python uses the `open()` function.
```
file = open("sample.txt", "r")
```
Arguments:

- `"sample.txt"` → file name
- `"r"` → read mode

### 3. Reading a File
Read the Entire File
```
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

**Read Line by Line**

```
file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()
```

Using `.strip()` removes the newline character.


### 4. Writing to a File

Mode:
```
w
```

```python
file = open("output.txt", "w")

file.write("Welcome to Data Science!")

file.close()
```

If the file doesn't exist, Python creates it.

If it exists, its contents are replaced.

### 5. Appending to a File

Mode:
```
a
```

```python
file = open("output.txt", "a")

file.write("\nPython is awesome!")

file.close()
```

This adds data without deleting existing content.

### 6. Using with

The recommended way to work with files.
```python
with open("sample.txt", "r") as file:
    content = file.read()

print(content)
```

**Advantages:**

- Automatically closes the file
- Cleaner code
- Prevents resource leaks

### 7. Reading CSV Files

Suppose you have:
```
Name,Marks
Rahul,88
Alice,91
Bob,76
```
Read it:
```python
with open("students.csv", "r") as file:
    for line in file:
        print(line.strip())
```

Output:
```
Name,Marks
Rahul,88
Alice,91
Bob,76
```
Later, Pandas will make reading CSV files much easier, but it's important to understand what happens behind the scenes.


### 8. Handling Missing Files

If the file doesn't exist:
```python
with open("unknown.txt", "r") as file:
    print(file.read())
```
Python raises a FileNotFoundError.

Handle it safely:
```python
try:
    with open("unknown.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

### 🧠 Data Science Connection

Imagine a dataset:
```
sales.csv
Date,Sales
2026-01-01,1200
2026-01-02,1800
2026-01-03,1500
```

Without Pandas, you'd need to read and process each line manually.

Later you'll simply write:

```python
import pandas as pd

df = pd.read_csv("sales.csv")
```

Understanding basic file handling helps you appreciate how these libraries work.

