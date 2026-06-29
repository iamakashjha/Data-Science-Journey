### 1. Difference between / and //?
- `/` performs true division and always returns a floating-point result (even if the division is exact).
- `//` performs floor division, returning the quotient rounded down to the nearest whole number (or toward negative infinity).

Example:
```
10 / 3   # 3.3333333333333335
10 // 3  # 3

-10 // 3 # -4
```

### 2. What does % do?
The % operator returns the remainder after division. It is commonly used to:
- Check if a number is even or odd.
- Determine divisibility.
- Wrap values in cycles (e.g., clocks, indexing).

Example:
```
10 % 3  # 1
8 % 2   # 0
```

### 3. Why are comparison operators useful?
Comparison operators compare two values and return either True or False. They are useful for making decisions, filtering data, and controlling program flow using conditions.

Example:
```
age >= 18
salary > 50000
```

### 4. What is operator precedence?
Operator precedence is the set of rules that determines the order in which Python evaluates operators in an expression. It is similar to the BODMAS/PEMDAS rule in mathematics, ensuring expressions are evaluated correctly without unnecessary parentheses.

Example:
```
2 + 3 * 4   # 14
(2 + 3) * 4 # 20
```

### 5. Why are logical operators important in Data Science?
Logical operators (and, or, not) are important because they allow us to combine multiple conditions when filtering, cleaning, and analyzing data. They help create complex queries and make decision-making more efficient.

Example (Pandas):
```
df[(df["Age"] > 25) & (df["Salary"] > 50000)]
```

