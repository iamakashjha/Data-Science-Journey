# Day 54 - NumPy Boolean Masking, Filtering & Conditional Selection

## 1. Boolean values

Python and NumPy use Boolean logic:

```python
age = 25
print(age > 18)  # True
print(age < 18)  # False
```

NumPy applies this element-wise to arrays.

## 2. Boolean operations on arrays

```python
import numpy as np

ages = np.array([18, 22, 27, 31, 16, 40])
print(ages > 25)
# [False False  True  True False  True]
```

This produces a Boolean array.

## 3. Boolean mask

A Boolean mask is a condition that tells NumPy which values to select.

```python
mask = ages > 25
print(mask)
```

Interpretation:

- `True` -> select
- `False` -> skip

## 4. Boolean indexing

```python
ages[ages > 25]
# [27 31 40]
```

This means: "Give me the values of `ages` whose condition is `True`." 

## 5. Examples

```python
ages >= 30
ages < 25
ages == 22
ages != 22
```

## 6. Core pattern

```python
array[condition]
```

Examples:

```python
prices[prices > 1000]
scores[scores >= 70]
ages[ages < 30]
```

## 7. Real dataset example

```python
data = np.array([
    [25, 50000, 700],
    [32, 65000, 720],
    [41, 80000, 750],
    [29, 55000, 690],
    [35, 72000, 730]
])
```

Select customers with income greater than 60,000:

```python
income = data[:, 1]
mask = income > 60000

filtered = data[mask]
```

This returns the rows whose income condition is true.

## 8. Why this matters

Vectorized filtering is much more efficient than manually iterating through every row in Python. For large datasets, this is a critical data-science technique.

## 9. Multiple conditions

To filter with multiple rules, combine masks.

```python
mask = (data[:, 0] > 30) & (data[:, 1] > 60000)
filtered = data[mask]
```

This means:

- age > 30
- and income > 60000

## 10. Use `&`, not `and`

This is a very common mistake.

Wrong:

```python
(data[:, 0] > 30) and (data[:, 1] > 60000)
```

Right:

```python
(data[:, 0] > 30) & (data[:, 1] > 60000)
```

`and` works for single Python values, but NumPy Boolean arrays need element-wise `&`.

## 11. Parentheses matter

Always write:

```python
mask = ((data[:, 0] > 30) & (data[:, 1] > 60000))
```

This is clearer and avoids operator-precedence problems.

## 12. OR conditions

Use `|` for OR:

```python
ages = np.array([18, 22, 27, 31, 16, 40])
mask = (ages < 25) | (ages > 35)
print(ages[mask])
# [18 22 40]
```

## 13. NOT condition

Use `~` for negation:

```python
mask = ~(ages > 25)
print(ages[mask])
```

## 14. The three essential operators

- `&` -> AND
- `|` -> OR
- `~` -> NOT

## 15. Filtering 2D arrays

```python
score_mask = data[:, 2] >= 720
filtered = data[score_mask]
```

This selects rows whose credit score is at least 720.

## 16. Multiple feature filtering

```python
mask = (
    (data[:, 0] > 30) &
    (data[:, 2] >= 720)
)
filtered = data[mask]
```

This is a very common data-science pattern.

## 17. Store the mask

```python
mask = (
    (data[:, 0] > 30) &
    (data[:, 1] > 60000) &
    (data[:, 2] > 720)
)

result = data[mask]
```

This makes the code clearer and easier to debug.

## 18. Inspect the mask

```python
print(mask)
print(mask.sum())
```

`mask.sum()` counts the number of `True` values because:

- `True` = 1
- `False` = 0

## 19. `np.where()`

```python
scores = np.array([45, 72, 88, 55, 91])

result = np.where(scores >= 60, "Pass", "Fail")
print(result)
# ['Fail' 'Pass' 'Pass' 'Fail' 'Pass']
```

Structure:

```python
np.where(condition, value_if_true, value_if_false)
```

## 20. `np.where()` for indices

```python
np.where(scores >= 80)
# (array([2, 4]),)
```

This returns the positions of matching elements.

## 21. `np.any()`

```python
scores = np.array([45, 55, 72, 88])
print(np.any(scores > 80))  # True
```

This checks whether at least one element satisfies the condition.

## 22. `np.all()`

```python
print(np.all(scores > 40))  # True
print(np.all(scores > 60))  # False
```

This checks whether all values satisfy the condition.

## 23. Conditional replacement

```python
scores = np.array([45, 72, 88, 55, 91])

scores[scores < 60] = 0
print(scores)
# [ 0 72 88  0 91]
```

This is a very useful data-cleaning pattern.

## 24. Another replacement example

```python
temperatures = np.array([22, 35, 40, 18, 30])
temperatures[temperatures > 30] = 30
```

This caps values at 30.

## 25. Filtering is not modification

```python
filtered = data[data[:, 1] > 60000]
```

This creates a filtered subset. It does not delete rows from the original array.

## 26. Real dataset example

```python
data = np.array([
    [22, 35000, 680, 0],
    [28, 52000, 710, 1],
    [35, 75000, 740, 1],
    [42, 90000, 780, 1],
    [31, 62000, 720, 0],
    [26, 48000, 700, 1],
    [39, 85000, 760, 1],
    [47, 95000, 790, 0]
])
```

A typical masked query:

```python
mask = (
    (data[:, 0] > 30) &
    (data[:, 1] >= 70000) &
    (data[:, 2] >= 750)
)

result = data[mask]
```

This selects the exact rows matching the rules.

## 27. Translate business questions into masks

Examples:

- “Age between 25 and 40” -> `(age >= 25) & (age <= 40)`
- “Income below 50,000 or credit score above 750” -> `(income < 50000) | (credit_score > 750)`
- “Customers who did not purchase” -> `purchased == 0` or `~(purchased == 1)`

This transformation is fundamental in data science.

## 28. Common mistakes

### Mistake 1: using `and`

```python
# Wrong
(x > 20) and (x < 50)

# Correct
(x > 20) & (x < 50)
```

### Mistake 2: missing parentheses

```python
# Wrong
x > 20 & x < 50

# Correct
(x > 20) & (x < 50)
```

### Mistake 3: using assignment instead of comparison

```python
# Wrong
x = 30

# Correct
x == 30
```

## 29. Shape and masking

For a matrix `X` with shape `(100, 4)`, the mask from one column has shape `(100,)`:

```python
mask = X[:, 0] > 30
print(mask.shape)  # (100,)
```

Then:

```python
filtered = X[mask]
```

selects the matching rows.

This is a key pattern in row-based filtering.

## 30. Summary

Key ideas:

- Boolean arrays are conditions over data
- `array[condition]` filters values
- use `&`, `|`, and `~` for boolean logic
- use `np.where()` for conditional values or indices
- use `np.any()` and `np.all()` to summarize truth values
- use conditional replacement for cleaning data
- row filtering using masks is one of the most practical data-science skills

The important mental model is:

- build a condition
- evaluate the condition element-wise
- select the rows or values that are `True`
