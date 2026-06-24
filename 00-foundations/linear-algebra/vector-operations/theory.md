# Day 22 — Vector Operations
**Goal**

Understand:

- Vector addition
- Scalar multiplication
- Vector scaling
- Why these operations matter in ML and AI


## 1. Vector Addition

**Suppose:**

Vector A:

Vector B:

Add corresponding elements:

Interpretation:
```
Move 2 right and 3 up.

Then move 4 right and 1 up.

Final position:
6 right and 4 up.
```

## 2. Scalar Multiplication

Suppose:

Multiply by 3:

This changes the length.

The direction stays the same.


## Why Scaling Matters

Suppose:
```
Age: 25
Income: 500000
```
Income dominates because of its large scale.

Machine learning often scales features before training models.

## 3. Unit Vectors

A unit vector has:

Unit vectors preserve direction while removing magnitude.

This becomes important in:

- cosine similarity
- embeddings
- recommendation systems

## Real AI Connection

Imagine two users:
```
User A:
[5, 4, 5]

User B:
[10, 8, 10]
```
Same preferences.

Different activity levels.

Scaling helps us compare direction rather than size.


## Deep Exercise

Suppose:
```
Study Hours:
[2, 4]

Extra Study:
[1, 2]
```
Add them:

What does the result mean?


## Important Insight

Think of vectors as:
```
Direction
+
Magnitude
```
Operations allow us to:

- combine information
- scale information
- compare information

That is exactly what modern machine learning systems do.