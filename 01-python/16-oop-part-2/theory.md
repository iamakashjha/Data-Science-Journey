# 📖 Theory

### 1. What is Inheritance?

Inheritance allows one class to reuse the attributes and methods of another class.

Think of it like this:
```
Animal
   │
   ├── Dog
   ├── Cat
   └── Bird
```

Every animal has common properties, but each child class can also have its own behavior.

### 2. Parent Class
```python
class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound.")
```

### 3. Child Class

```python
class Dog(Animal):

    def bark(self):
        print("Woof!")
```

### Create an object:

```python
dog = Dog("Tommy")

dog.speak()
dog.bark()
```

**Output:**

Animal makes a sound.

```
Woof!
```

The Dog class inherits the speak() method from Animal.

### 4. Method Overriding

A child class can replace a method from the parent class.

```python
class Dog(Animal):

    def speak(self):
        print("Woof!")
```

Now:

```python
dog = Dog("Tommy")

dog.speak()
```

**Output:**
```
Woof!
```

This is called method overriding.

### 5. Using super()

Sometimes you want to reuse the parent constructor.

```python
class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

Now both name and breed are initialized correctly.

### 6. Polymorphism

One interface, many implementations.

Example:
```python
class Dog:

    def speak(self):
        print("Woof!")

class Cat:

    def speak(self):
        print("Meow!")
```

Loop through different objects:

```python
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()
```

**Output:**

Woof!  
Meow!

The same method name behaves differently depending on the object.

### 7. Encapsulation (Introduction)

Encapsulation means protecting an object's internal data.

Example:
```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

The double `underscore (__)` indicates the attribute should not be accessed directly from outside the class.

Instead, provide methods:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
```

**Usage:**

```python
account = BankAccount(1000)

print(account.get_balance())
```

### Key Takeaway

Remember the four pillars of OOP:
```
Object-Oriented Programming
│
├── Encapsulation
├── Inheritance
├── Polymorphism
└── Abstraction
```
Today you've learned the first three in depth. **Abstraction** will be explored further as you work with larger applications and Python libraries.

Understanding OOP will make it much easier to understand APIs like:

```python
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

Here, different machine learning models expose the same methods while implementing them differently—a practical example of polymorphism.
