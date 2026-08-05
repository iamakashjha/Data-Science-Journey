### Data Science Connection

Imagine you're analyzing thousands of students.

Instead of using dictionaries:

```python
student = {
    "name": "Rahul",
    "marks": 88
}
```

You can use objects:

```python
student = Student("Rahul", 88)
```

This keeps data and related behavior together, making programs easier to extend and maintain.



### Remember this simple relationship:
```
Class
   │
   ├── Blueprint
   │
   ▼
Objects
   │
   ├── Data (Attributes)
   └── Behavior (Methods)
```