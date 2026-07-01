python_students = {
    "Rahul",
    "Alice",
    "Bob",
    "Charlie"
}

sql_students = {
    "Alice",
    "David",
    "Charlie",
    "Emma"
}

# Find:

# Students enrolled in both courses
print("Students enrolled in both courses:", python_students.intersection(sql_students))

# Students enrolled only in Python
print("Students enrolled only in Python:", python_students.difference(sql_students))

# Students enrolled only in SQL
print("Students enrolled only in SQL:", sql_students.difference(python_students))

# All students
print("All students:", python_students.union(sql_students))

