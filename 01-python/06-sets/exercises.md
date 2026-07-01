### 1. What is a set?
A set is an unordered, mutable collection of unique elements. It does not allow duplicate values.

### 2. Why are duplicates removed automatically?
Sets are designed to store only unique values. When you add duplicate elements, Python automatically ignores them because sets use hashing to keep each element unique.


### 3. Difference between a list and a set?
```
| List                    | Set                           |
| ----------------------- | ----------------------------- |
| Ordered collection      | Unordered collection          |
| Allows duplicate values | Does not allow duplicates     |
| Mutable                 | Mutable                       |
| Supports indexing       | Does not support indexing     |
| Written using `[]`      | Written using `{}` or `set()` |
```

### 4. Difference between remove() and discard()?
```
| `remove()`                                      | `discard()`                                         |
| ----------------------------------------------- | --------------------------------------------------- |
| Removes the specified element                   | Removes the specified element                       |
| Raises a `KeyError` if the element is not found | Does not raise an error if the element is not found |
```

### 5. What is the purpose of:
- **Union**
```
a) Union (| or union())

Combines all unique elements from two or more sets.
```
**Intersection**
```
b) Intersection (& or intersection())

Returns only the common elements between sets.
```

**Difference**
```
c) Difference (- or difference())

Returns elements that are in the first set but not in the second.
```

**Symmetric Difference**
```
d) Symmetric Difference (^ or symmetric_difference())

Returns elements that are in either set but not in both.
```


### 6. Where are sets useful in Data Science?
Sets are useful in Data Science for:

- Removing duplicate records from datasets.
- Finding common customers, products, or users between different datasets using intersection.
- Comparing datasets to find missing or extra records using difference.
- Identifying unique categories or labels in a dataset.
- Performing fast membership checks, since sets provide efficient lookup operations.