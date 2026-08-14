# Reflection

---

## What did I learn today?
* Explored core **Object-Oriented Programming (OOP)** principles: **Inheritance**, **Encapsulation**, and **Polymorphism**.
* Understood how class hierarchies are structured using **parent (base)** and **child (derived)** classes.
* Learned how to use **method overriding** and the **`super()`** function to customize or extend parent behavior without rewriting existing logic.
* Examined how **encapsulation** secures data integrity by bundling state with behavior and controlling access via clean interfaces (getters/setters).

---

## Which OOP concept was easiest to understand?
* **Inheritance:** The intuitive *"is-a"* mental model (e.g., `Dog` is an `Animal`, `Manager` is an `Employee`) makes it very straightforward to see how attributes and methods flow down from generic base classes to specialized subclasses.

---

## Where do I see inheritance in real software?
* **GUI / UI Frameworks:** UI elements (like `Button`, `TextInput`, `Checkbox`) typically inherit from a base `View` or `Widget` class to share common properties like `position`, `dimensions`, and `render()`.
* **Web & API Frameworks:** Custom database models or views often inherit from framework base classes (e.g., `models.Model` in Django/SQLAlchemy or `Controller` in ASP.NET/Spring) to inherit built-in persistence, validation, and routing methods.
* **Custom Exception Handling:** Custom application errors inherit from the standard `Exception` or `Error` base class to integrate cleanly with `try/catch` runtime handlers.

---

## Which concept needs more revision?
* **Polymorphism & Method Resolution (MRO):** Deepening the understanding of dynamic dispatch, duck typing, and how multiple inheritance hierarchies determine method resolution order using `super()`.