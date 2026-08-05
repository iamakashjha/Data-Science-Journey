# Student Management System

# Create a Student class with:

# Attributes:

# Name
# Age
# Marks

# Methods:

# display_details()
# is_pass() (returns True if marks ≥ 40)

# Create at least 3 student objects and display their information.


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")

    def is_pass(self):
        return self.marks >= 40


student1 = Student("Rahul", 20, 88)
student2 = Student("Alice", 22, 35)

student1.display_details()
print(f"Pass Status: {'Pass' if student1.is_pass() else 'Fail'}")
print()

student2.display_details()
print(f"Pass Status: {'Pass' if student2.is_pass() else 'Fail'}")
print()
