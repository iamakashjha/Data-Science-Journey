# Object-Oriented Programming (OOP) Exercises

---

### 1. What is inheritance?
**Inheritance** is a fundamental OOP mechanism where a new class (child/subclass) derives properties, attributes, and methods from an existing class (parent/superclass). 

* **Purpose:** It facilitates **code reusability** and establishes an **"is-a" relationship** between objects (e.g., a `Dog` *is an* `Animal`).

---

### 2. Difference between a parent class and a child class?

| Feature | Parent Class (Base / Superclass) | Child Class (Derived / Subclass) |
| :--- | :--- | :--- |
| **Definition** | The existing class whose features are inherited. | The new class that inherits features from the parent. |
| **Generality** | More generic and general in purpose. | More specialized and specific. |
| **Awareness** | Has no direct knowledge of its subclasses. | Explicitly knows and inherits from its parent class. |
| **Code Scope** | Defines common attributes and behaviors. | Reuses parent logic and adds or overrides features. |

---

### 3. What is method overriding?
**Method overriding** occurs when a child class provides its own specific implementation of a method that is already defined in its parent class.

* **Requirement:** The method in the child class must share the same name and signature as the one in the parent class.
* **Purpose:** Allows a subclass to customize or completely replace the inherited behavior without altering the parent class.

---

### 4. Why do we use `super()`?
We use `super()` (or the language equivalent) to give a child class access to methods and the constructor of its parent class.

* **Extending Initialization:** Commonly used inside `__init__()` (or constructors) to ensure parent attributes are properly initialized before adding child-specific attributes.
* **Preserving Logic:** Allows you to override a method while still executing the original parent implementation (extending rather than fully replacing).
* **Maintainability:** Avoids hardcoding the parent class's name, making refactoring and multiple inheritance hierarchies easier to manage.

---

### 5. What is polymorphism?
**Polymorphism** (meaning "many forms") is the ability of different classes to respond to the same method call in ways specific to their own data types.

* **Key Benefit:** It allows code to treat different objects uniformly through a common interface without needing to know their specific types at runtime (e.g., calling `.draw()` on `Circle`, `Square`, and `Triangle` objects iteratively).

---

### 6. What is encapsulation?
**Encapsulation** is the bundling of data (attributes) and the methods that operate on that data into a single unit (a class), while restricting direct external access to some of the object's internal components.

* **Data Hiding:** Achieved using access modifiers (`private`, `protected`, `public` or naming conventions like `_` and `__` in Python).
* **Controlled Access:** Provides public methods (**getters** and **setters**) to validate or manage how data is viewed and modified, protecting object integrity.