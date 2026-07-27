## 1. What is a Module?

A module is simply a Python file (.py) containing reusable code.

Example:

```python
math_utils.py
def square(x):
    return x * x

def cube(x):
    return x * x * x
```

Another file can use it.

## 2. Importing Modules

```python
import math

print(math.sqrt(25))
print(math.pi)
```
Output:
```
5.0
3.141592653589793
```

## 3. Import Specific Functions

Instead of importing everything:

```python
from math import sqrt

print(sqrt(49))
```

## 4. Import with Alias

```python
import numpy as np
import pandas as pd
```

You'll use these aliases throughout your Data Science journey.


## 5. Creating Your Own Module

Create:

`math_utils.py`

```python

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def square(x):
    return x * x
```

`implementation.py`

```python

import math_utils

print(math_utils.add(10, 20))
print(math_utils.square(5))
```

Output:

```
30
25
```


## 📦 What is a Package?

A package is a folder containing multiple modules.

**Example:**

```python
package_demo/
│
├── __init__.py
├── statistics.py
└── preprocessing.py
```

This helps organize larger projects.

## Data Science Connection

Imagine a Machine Learning project.

```
customer_churn/
│
├── data_loader.py
├── preprocessing.py
├── feature_engineering.py
├── train_model.py
├── evaluate.py
└── utils.py
```

Each file has one responsibility.

This makes projects easier to read, test, and maintain.
