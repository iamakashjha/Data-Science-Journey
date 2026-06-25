# Day 24 — Matrices: Data as Tables

Until now:

Scalars → single numbers

Vectors → lists of numbers

Today:
```
A matrix is a collection of vectors organized into rows and columns.
```
This is extremely important because almost every dataset in Data Science is a matrix.


## 1. What is a Matrix?

Example:

This matrix has:

- 2 rows
- 2 columns

Shape:
```
(2,2)
```

## 2. Real Data Example

Imagine:

| Student | Math | Science |
| ------- | ---- | ------- |
| A       | 80   | 90      |
| B       | 75   | 85      |
| C       | 95   | 92      |

Ignoring names:

This is a matrix.


## Data Science Interpretation

Rows:
```
Observations
```
Columns:
```
Features
```
Example:
```
Rows = customers

Columns = age, income, purchases
```

## 3. Matrix Shape

If:
```
100 customers
5 features
```
Shape:
```
(100,5)
```
Always ask:

| Rows of what?

| Columns of what?


## Real AI Connection

An image:
```
28 × 28 pixels
```
is a:
```
28 × 28 matrix
```
A grayscale image is literally a matrix of numbers.

`This is why computer vision uses linear algebra.`




## Important Insight

The biggest realization today is:
```
Excel Sheet
↓

DataFrame
↓

Matrix
```

Almost every dataset can eventually be viewed as a matrix.

And almost every machine learning algorithm operates on matrices.