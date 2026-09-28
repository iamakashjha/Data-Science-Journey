# Reflection - NumPy Boolean Masking, Filtering & Conditional Selection

## Understanding

### What is a Boolean mask?

A Boolean mask is a condition that determines which elements or rows should be selected.

### What does `array[mask]` do?

It selects the values where the mask is `True`.

### What does `&` mean?

It means element-wise AND.

### What does `|` mean?

It means element-wise OR.

### What does `~` mean?

It means element-wise NOT.

### Why are parentheses important?

They make conditions clear and prevent precedence errors when combining multiple comparisons.

## NumPy

### What does `np.where()` do?

It creates values based on a condition or returns indices satisfying the condition.

### What does `np.any()` do?

It returns `True` if at least one value satisfies the condition.

### What does `np.all()` do?

It returns `True` only if all values satisfy the condition.

### How do you count matching elements?

Use `mask.sum()` because `True` counts as 1 and `False` counts as 0.

## Data science

### How can Boolean masking filter dataset rows?

By creating a mask from one or more columns and using it to select matching rows.

### How would you filter customers based on multiple features?

Use a combined mask such as `(age > 30) & (income > 60000) & (score > 720)`.

### Why is vectorized filtering preferable to manually looping through every row?

It is faster, clearer, and easier to read for large datasets.

### How does Boolean masking connect with data cleaning?

It helps identify invalid, extreme, or out-of-range values and enables conditional replacement.

### Where might you use conditional replacement?

For clipping values, filling missing or invalid entries, or capping outliers.

## Self assessment

- Boolean arrays: ⭐⭐⭐⭐⭐
- Boolean masking: ⭐⭐⭐⭐⭐
- Multiple conditions: ⭐⭐⭐⭐⭐
- `np.where()`: ⭐⭐⭐⭐⭐
- `np.any()/np.all()`: ⭐⭐⭐⭐⭐
- Dataset filtering: ⭐⭐⭐⭐⭐
- Shape + masking: ⭐⭐⭐⭐⭐
