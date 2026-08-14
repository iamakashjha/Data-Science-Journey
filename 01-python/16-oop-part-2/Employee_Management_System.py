class employee:
    def __init__(self, name, age, salary, tools=None, programming_language=None, frameworks=None):
        self.name = name
        self.age = age
        self.salary = salary
        self.tools = tools or []
        self.programming_language = programming_language
        self.frameworks = frameworks or []

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


class data_scientist(employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary, programming_language=programming_language)

    def work(self):
        print(f"{self.name} is building machine learning models.")
        print(f"Programming Language: {self.programming_language}")

class data_engineer(employee):
    def __init__(self, name, age, salary, tools):
        super().__init__(name, age, salary, tools=tools)
        self.tools = tools

    def work(self):
        print(f"{self.name} is working with the following tools: {', '.join(self.tools)}")

class machine_learning_engineer(employee):
    def __init__(self, name, age, salary, frameworks):
        super().__init__(name, age, salary, frameworks=frameworks)
        self.frameworks = frameworks

    def work(self):
        print(f"{self.name} is working with the following frameworks: {', '.join(self.frameworks)}")



data_scientist_1 = data_scientist("Alice", 30, 120000, "Python")
data_engineer_1 = data_engineer("Bob", 28, 110000, ["Hadoop", "Spark"])
machine_learning_engineer_1 = machine_learning_engineer("Charlie", 32, 130000, ["TensorFlow", "PyTorch"])

print("Data Scientist Info:")
data_scientist_1.display_info()
data_scientist_1.work()

print("\nData Engineer Info:")
data_engineer_1.display_info()
data_engineer_1.work()

print("\nMachine Learning Engineer Info:")
machine_learning_engineer_1.display_info()
machine_learning_engineer_1.work()