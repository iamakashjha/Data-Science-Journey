### What is a dictionary?
A dictionary is a built-in Python data type that stores data as key-value pairs. Each key is unique and is used to access its corresponding value. Dictionaries are mutable, meaning their contents can be changed after creation.

### Difference between a dictionary and a list?

| List                                  | Dictionary                                      |
| ------------------------------------- | ----------------------------------------------- |
| Stores elements in a sequence.        | Stores data as key-value pairs.                 |
| Accessed using an index (0, 1, 2...). | Accessed using keys.                            |
| Ordered and mutable.                  | Ordered (Python 3.7+) and mutable.              |
| Duplicate values are allowed.         | Keys must be unique (values can be duplicated). |


### Why are dictionary keys unique?
Dictionary keys are unique because each key acts as an identifier for its value. If duplicate keys were allowed, Python would not know which value to return. If the same key is added again, the new value overwrites the old one.


### Difference between [] and get()?

| `[]`                                           | `get()`                                                        |
| ---------------------------------------------- | -------------------------------------------------------------- |
| Raises a `KeyError` if the key does not exist. | Returns `None` (or a default value) if the key does not exist. |
| Used when you're sure the key exists.          | Safer when the key may be missing.                             |



### What does items() return?

The items() method returns a view object containing all the dictionary's (key, value) pairs as tuples.


### Where are dictionaries used in Data Science?

Dictionaries are widely used in Data Science for:

- Storing dataset records as key-value pairs.
- Representing JSON data from APIs.
- Creating pandas DataFrames from dictionaries.
- Counting frequencies of values (e.g., word counts, class counts).
- Storing machine learning model parameters and configurations.
- Mapping categorical values to numerical values (encoding).