### 1. What is a Set?

A set is an unordered collection of unique elements.
```
numbers = {1, 2, 3, 4}

print(numbers)
```
Notice:
```
numbers = {1, 2, 2, 3, 4, 4}

print(numbers)
```
Output:
```
{1, 2, 3, 4}
```
Duplicates disappear automatically.


### 2. Creating Sets
```
colors = {"Red", "Blue", "Green"}

numbers = set([1,2,3,4])
```
Empty set:
```
empty = set()
```
Important:
```
{}
```
creates a dictionary, not a set.

### 3. Add Elements
```
fruits = {"Apple", "Banana"}

fruits.add("Orange")

print(fruits)
```

### 4. Remove Elements
```
fruits.remove("Banana")
```
Safer option:
```
fruits.discard("Banana")
```
Difference:

- `remove()` raises an error if the element doesn't exist.
- `discard()` does nothing if it's missing.


### 5. Membership Testing
```
languages = {"Python", "SQL", "R"}

print("Python" in languages)
print("Java" in languages)
```
Sets are very fast for membership checks


## Set Operations

**Union**

Combine unique values.
```
A = {1,2,3}

B = {3,4,5}

print(A | B)
```
Output:
```
{1,2,3,4,5}
```

**Intersection**

Common elements.
```
print(A & B)
```
Output:
```
{3}
```

**Difference**

Elements in A but not B.
```
print(A - B)
```
Output:
```
{1,2}
```

**Symmetric Difference**

Elements in either set, but not both.
```
print(A ^ B)
```
Output:
```
{1,2,4,5}
```

## Data Science Connection

Imagine customer IDs:
```
customers = [
    101,
    102,
    103,
    101,
    105,
    102,
    108
]
```
Find unique customers:
```
unique_customers = set(customers)

print(unique_customers)
```
Real-world use:

- Remove duplicate users
- Count unique visitors
- Find unique products
- Identify duplicate records