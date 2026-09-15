31. 🎤 5 Interview Questions
Q1. What is NumPy indexing?

Answer:

Indexing is the process of accessing a specific element of an array using its position.

For a 1D array:

arr[2]

For a 2D array:

arr[row, column]

NumPy uses zero-based indexing.

Q2. How do you select an entire column from a 2D NumPy array?

Answer:

Use:

X[:, column_index]

For example:

X[:, 2]

means:

Select all rows from column 2.

This is commonly used for feature extraction.

Q3. What does X[1:4, 2:5] mean?

Answer:

It selects:

Rows:    1, 2, 3
Columns: 2, 3, 4

because the stopping index is exclusive.

So it extracts a rectangular submatrix.

Q4. What's the difference between indexing and slicing?

Answer:

Indexing generally selects a specific element or position:

X[2, 3]

Slicing selects a range:

X[2:5, 1:4]

Indexing:

specific location

Slicing:

range/subset
Q5. Coding/Data Science Question

Given:

X = np.array([
    [25, 50000, 700],
    [30, 60000, 720],
    [35, 70000, 750]
])

You want to select only income and credit score.

What would you write?

Answer:

X_selected = X[:, 1:3]

Result:

[[50000   700]
 [60000   720]
 [70000   750]]

Shape:

(3, 2)

This is a simple example of feature selection.