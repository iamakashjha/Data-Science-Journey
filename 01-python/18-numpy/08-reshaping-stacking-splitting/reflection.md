# Reflection - NumPy Reshaping, Flattening, Stacking & Splitting

## Understanding

### What does `reshape()` do?

It changes the shape of an array without changing the total number of elements.

### Why must the number of elements remain unchanged?

Because a reshape operation preserves the original data. It only changes how the data is organized.

### What does `-1` mean inside `reshape()`?

It tells NumPy to infer the missing dimension automatically.

### What does `flatten()` do?

It converts a multi-dimensional array into a 1D array.

### What is the difference between `flatten()` and `ravel()`?

`flatten()` returns a copy, while `ravel()` typically returns a view when possible.

### What does transpose do?

It swaps rows and columns of an array.

## Combining data

### What does `concatenate()` do?

It joins arrays along an existing axis.

### What does `stack()` do?

It creates a new axis while combining arrays.

### What is the difference between `vstack()` and `hstack()`?

`vstack()` stacks arrays vertically; `hstack()` stacks arrays horizontally.

### What does `split()` do?

It divides an array into multiple smaller arrays.

## Machine learning

### What is `X`?

`X` is usually the feature matrix: observations by features.

### What is `y`?

`y` is the target or label vector.

### Why is `X` usually 2D?

Because each row represents an observation and each column represents a feature.

### What's the difference between `(100,)` and `(100, 1)`?

`(100,)` is a 1D vector, while `(100, 1)` is a 2D column vector.

### Why should you frequently check `X.shape`?

Because the structure determines how the data should be interpreted and which ML operations are valid.

## Self assessment

- reshape: ⭐⭐⭐⭐⭐
- flatten/ravel: ⭐⭐⭐⭐⭐
- transpose: ⭐⭐⭐⭐⭐
- concatenate: ⭐⭐⭐⭐⭐
- stacking: ⭐⭐⭐⭐⭐
- splitting: ⭐⭐⭐⭐⭐
- X / y understanding: ⭐⭐⭐⭐⭐
- shape reasoning: ⭐⭐⭐⭐⭐
