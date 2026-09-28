# Exercises - NumPy Advanced Indexing, Sorting & Ranking

## Exercise 1

Given:

```python
values = np.array([45, 12, 89, 34, 67, 23])
```

Find:

- sorted values
- sorting indices
- ascending order
- descending order
- minimum
- maximum
- index of minimum
- index of maximum

## Exercise 2

Given:

```python
names = np.array(["A", "B", "C", "D", "E"])
scores = np.array([88, 72, 95, 81, 90])
```

Print the students from highest score to lowest.

## Exercise 3

Find the top 2 students without manually sorting the scores.

## Exercise 4

Given:

```python
sales = np.array([
    [100, 200, 150],
    [300, 120, 250],
    [180, 220, 190]
])
```

Find:

- sorted values by row
- sorted values by column
- largest value
- smallest value
- position of largest value
- position of smallest value

## Interview questions

### Q1. What is the difference between `sort()` and `argsort()`?

`np.sort(x)` returns sorted values. `np.argsort(x)` returns the indices that would produce the sorted order.

### Q2. What is the difference between `max()` and `argmax()`?

`np.max(x)` returns the maximum value. `np.argmax(x)` returns the index of the maximum value.

### Q3. How do you find the top 5 values and their original positions?

```python
indices = np.argsort(x)[::-1][:5]
values = x[indices]
```

### Q4. What is the difference between `argsort()` and `argpartition()`?

`argsort()` produces a complete ordering. `argpartition()` performs a partial ordering around a specified position, which is useful for top-k or bottom-k selection.

### Q5. Why is `argsort()` useful with multiple related arrays?

Because it gives a shared ordering that can be applied to all aligned arrays without breaking the relationships between them.
