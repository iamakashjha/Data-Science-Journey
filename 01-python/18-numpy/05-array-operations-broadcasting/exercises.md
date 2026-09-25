# Exercises - Array Operations and Broadcasting

Use NumPy and predict the result before running each expression.

## 1. Scalar operations

Given `x = np.array([10, 20, 30])`, calculate `x + 5`, `x - 5`, `x * 5`,
`x / 5`, and `x ** 2`.

## 2. Array operations

Given `a = np.array([10, 20, 30])` and `b = np.array([2, 4, 5])`, calculate
`a + b`, `a - b`, `a * b`, and `a / b`.

## 3. Filtering

Given `scores = np.array([45, 72, 88, 34, 91])`, select scores greater than 70.

## 4. Multiple conditions

Using the same scores, select values between 50 and 90, inclusive.

## 5. Row broadcasting

What is the result of `np.ones((4, 3)) + np.array([10, 20, 30])`? Explain which
axis receives the three values.

## 6. Shape compatibility

Does broadcasting work for shapes `(4, 3)` and `(3,)`? State the resulting shape.

## 7. Column broadcasting

Does broadcasting work for shapes `(4, 3)` and `(4, 1)`? Explain the result.

## 8. Broadcasting error

Does broadcasting work for shapes `(4, 3)` and `(2,)`? Explain the conflicting
dimensions.

## 9. Data science

Given `X.shape == (1000, 5)` and `mean.shape == (5,)`, would `X - mean` work?
Explain what the five values represent.

## 10. Interview practice

Given `X.shape == (100, 4)` and `weights.shape == (4,)`, what is the shape of
`X * weights` and what does each weight affect?
