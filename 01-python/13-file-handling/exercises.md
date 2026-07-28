### 1. Difference between "r", "w", and "a" modes?
| Mode  | Purpose          | File Must Exist?          | Existing Data                                           |
| ----- | ---------------- | ------------------------- | ------------------------------------------------------- |
| `"r"` | Read a file      | ✅ Yes                     | Keeps data unchanged                                    |
| `"w"` | Write to a file  | ❌ No (creates if missing) | Deletes existing data before writing                    |
| `"a"` | Append to a file | ❌ No (creates if missing) | Adds new data at the end without deleting existing data |

```python
# Read
with open("data.txt", "r") as file:
    print(file.read())

# Write
with open("data.txt", "w") as file:
    file.write("Hello World")

# Append
with open("data.txt", "a") as file:
    file.write("\nNew Line")
```

### 2. Why is with open() preferred over open() and close()?
`with open()` automatically closes the file after the block finishes, even if an exception occurs. This prevents resource leaks and makes the code cleaner and safer.

Without with:

file = open("data.txt", "r")
content = file.read()
file.close()

If an error occurs before close(), the file may remain open.

With with:

with open("data.txt", "r") as file:
    content = file.read()

The file is closed automatically.

### 3. What happens if a file doesn't exist?

It depends on the mode used:

- "r" **(read):** Raises an error because the file must already exist.
- "w" **(write):** Creates a new file if it doesn't exist.
- "a" **(append):** Creates a new file if it doesn't exist.

Example:
```python
# Error if file doesn't exist
with open("missing.txt", "r") as file:
    print(file.read())

# Creates the file
with open("new.txt", "w") as file:
    file.write("Hello")

# Also creates the file
with open("log.txt", "a") as file:
    file.write("First log")
```

### 4. What exception is raised when a file is missing?

Python raises a FileNotFoundError when trying to open a non-existent file in read mode.

**Example:**

```python
try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
```

Output:

```
File not found!
```

### 5. Why is file handling important in Data Science?

File handling is essential because data scientists frequently work with files to store, retrieve, and process data.

Common uses include:

- Reading datasets (CSV, Excel, JSON, text files).
- Saving cleaned or transformed data.
- Writing model predictions and results.
- Storing logs and experiment outputs.
- Loading and saving machine learning models.

Example:
```python
import pandas as pd

# Read a CSV file
df = pd.read_csv("employees.csv")

# Save processed data
df.to_csv("cleaned_employees.csv", index=False)
```

