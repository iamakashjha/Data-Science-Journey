### Question:

Why is catching a specific exception (like `ValueError`) better than using a broad `except Exception`?

### Answer:

Specific exception handling makes debugging easier, avoids hiding unexpected bugs, and allows your program to respond appropriately to different types of errors.