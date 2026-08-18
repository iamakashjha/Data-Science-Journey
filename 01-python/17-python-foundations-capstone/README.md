# Day 45 — Python Foundations Capstone

Today is a milestone day.

You've spent the last several days building Python fundamentals. Instead of learning another isolated topic, today you'll prove that you can combine those concepts into one complete program.

Your goal is not to write the shortest code.

Your goal is to write **organized, readable, reusable Python.**

## Today's Project

### Student Performance Management System

You'll build a small application that:

1. Stores student information
2. Adds students
3. Calculates statistics
4. Assigns grades
5. Identifies the topper
6. Saves data to a file
7. Loads data from a file
8. Handles invalid input
9. Uses functions
10. Uses a class
11. Uses a separate module

This will combine almost everything you've learned.

```
📂 Folder Structure

01-python/
└── 17-python-foundations-capstone/
    ├── README.md
    ├── main.py
    ├── student.py
    ├── statistics_utils.py
    ├── file_utils.py
    ├── data/
    │   └── students.json
    ├── tests/
    │   └── test_student.py
    ├── screenshots/
    ├── reflection.md
    └── resources.md
```

Notice that we're introducing **JSON** today.

That's intentional.

JSON is extremely common in APIs and real-world data systems, so it's a good bridge between basic Python and the tools you'll use later.

🧠 Concepts You're Combining
```
| Concept       | Where you'll use it      |
| ------------- | ------------------------ |
| Variables     | Student information      |
| Data types    | Names, marks, IDs        |
| Lists         | Student marks            |
| Dictionaries  | Student records          |
| Sets          | Unique subjects          |
| Tuples        | Fixed student statistics |
| Conditionals  | Grade assignment         |
| Loops         | Processing students      |
| Functions     | Reusable calculations    |
| Modules       | Project organization     |
| File handling | Saving/loading data      |
| Exceptions    | Invalid data             |
| OOP           | `Student` class          |

```

This is the point of the foundation module:

**Individual concepts become one system.**


### Part 1 — Create the Student Class

Create student.py.

Start with:

```python
class Student:

    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks


    def average(self):
        return sum(self.marks) / len(self.marks)


    def highest_mark(self):
        return max(self.marks)


    def lowest_mark(self):
        return min(self.marks)


    def grade(self):
        average = self.average()


        if average >= 90:
            return "A"


        elif average >= 80:
            return "B"


        elif average >= 70:
            return "C"


        elif average >= 60:
            return "D"


        else:
            return "F"


    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
        print(f"Grade: {self.grade()}")
```

Don't just copy this.

Understand what every line is doing.

### Part 2 — Statistics Module

Create:

```
statistics_utils.py
```

Add functions that work with multiple students.


### 🧠 Data Science Connection

This project may look like a simple student application.

But conceptually you're already building a miniature data pipeline:

```
Raw Data
   ↓
Validation
   ↓
Storage
   ↓
Processing
   ↓
Statistics
   ↓
Analysis
   ↓
Results
```

That's extremely close to what you'll eventually do with real datasets.

The difference is that instead of manually managing the data, you'll soon use:

```
NumPy
   ↓
Pandas
   ↓
SQL
   ↓
Machine Learning
```


