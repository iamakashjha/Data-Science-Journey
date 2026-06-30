## 🌍 Mini Project
Coordinate System

Represent locations as tuples.
```
locations = [
    ("Library", (10,20)),
    ("Cafe", (25,18)),
    ("Office", (30,12))
]
```
Print:
```
Library → (10,20)

Cafe → (25,18)

Office → (30,12)
```
This introduces the idea of structured records.


## Exercises

### 1. What is a tuple?
A tuple is an immutable, ordered collection of items. It can store elements of different data types, and once created, its contents cannot be changed.

### 2. Why are tuples immutable?
Tuples are immutable to ensure that their data remains constant after creation. This makes them safer to use when the data should not change and allows Python to optimize their performance in some cases.

### 3. Difference between list and tuple?
Both are same but the only difference is list is mutable and tuple is immutable. lists are used for flexible data type and tuples are used for fixed data types.

### 4. Why does Python return tuples from many functions?
Python often returns tuples when a function needs to return multiple related values. Since these returned values usually represent a fixed result, making them immutable prevents accidental modification.

### 5. Give three real-world examples where tuples are better than lists.
- DOB
- GPS coordinates
- Shape of a NumPy array