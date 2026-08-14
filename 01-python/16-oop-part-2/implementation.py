class Employee:

    def __init__(self, name):
        self.name = name

    def role(self):
        print("General Employee")


class DataScientist(Employee):

    def __init__(self, name, programming_language):
        super().__init__(name)
        self.programming_language = programming_language

    def role(self):
        print("Builds Machine Learning models")


employee = Employee("Rahul")
data_scientist = DataScientist("Alice", "Python")

employee.role()
data_scientist.role()