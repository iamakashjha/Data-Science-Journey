class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age  
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")


student1 = Student("Rahul", 20, 88)
student2 = Student("Alice", 22, 95)

student1.display()
print()

student2.display()