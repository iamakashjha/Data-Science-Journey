# 💼 Interview Questions

### 1. What are the four pillars of Object-Oriented Programming?

**Answer:**

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

### 2. What is the difference between inheritance and composition?

**Answer:**

- **Inheritance** models an **"is-a"** relationship (e.g., Dog is an Animal).
- **Composition** models a **"has-a"** relationship (e.g., Car has an Engine).

Composition often provides greater flexibility because objects can be combined without creating deep inheritance hierarchies.

### 3. What is method overriding?

**Answer:**

Method overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

### 4. Why is OOP important in Data Science?

**Answer:**

OOP makes code modular, reusable, and maintainable. Popular Data Science libraries such as **Pandas, Scikit-learn, and TensorFlow** use classes and objects to represent datasets, models, transformers, and pipelines.

### 5. Coding Question

Create a parent class Animal and child classes Dog and Cat. Override the speak() method so each child prints its own sound.

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


animals = [Dog(), Cat()]


for animal in animals:
    animal.speak()
```