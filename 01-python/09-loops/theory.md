## Why Do We Need Loops?

Suppose you have:
```
marks = [85, 92, 78, 90, 88]
```
Without loops:
```
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
```
This doesn't scale.

With a loop:
```
for mark in marks:
    print(mark)
```
The same code works even if there are 10 million marks.

## 1️⃣ The for Loop

A for loop iterates over a sequence.
```
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)
```
Output:
```
Apple
Banana
Orange
```
Loop with range()
```
for i in range(5):
    print(i)
```
Output:
```
0
1
2
3
4
```
Different forms:
```
range(5)        # 0 → 4
range(2, 8)     # 2 → 7
range(0, 10, 2) # 0,2,4,6,8
```

## 2️⃣ The while Loop

Runs until a condition becomes False.
```
count = 1

while count <= 5:
    print(count)
    count += 1
```

Always update the condition, or you'll create an infinite loop.


## 3️⃣ Looping Through Different Data Structures
**List**
```
numbers = [10, 20, 30]

for num in numbers:
    print(num)
```

**Tuple**
```
coordinates = (10, 20)

for value in coordinates:
    print(value)
```

**Set**
```
skills = {"Python", "SQL", "Pandas"}

for skill in skills:
    print(skill)
```
Remember: sets are unordered.

**Dictionary**
```
student = {
    "name": "Rahul",
    "age": 22,
    "cgpa": 8.8
}

for key, value in student.items():
    print(key, value)
```

## 4️⃣ break and continue

**break**

Stops the loop immediately.
```
for i in range(10):
    if i == 5:
        break

    print(i)
```
Output:
```
0
1
2
3
4
```

**continue**

Skips the current iteration.

```
for i in range(5):
    if i == 2:
        continue

    print(i)
```

Output:
```
0
1
3
4
```

## Data Science Connection

Suppose you have sales data:
```
sales = [1200, 1800, 2200, 900, 1500]
```
Find the total sales.
```
total = 0

for sale in sales:
    total += sale

print(total)
```
Later, Pandas will do this with:
```
df["Sales"].sum()
```
But understanding loops helps you understand what happens behind the scenes.


### Key Takeaway

Almost every Data Science workflow follows this pattern:
```
Dataset
    │
    ▼
Loop through records
    │
    ▼
Apply logic
    │
    ▼
Store results
```