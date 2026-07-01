student = {
    "name": "Rahul",
    "age": 22,
    "cgpa": 8.9
}

student["city"] = "Delhi"

student["cgpa"] = 9.2

for key, value in student.items():
    print(f"{key}: {value}")



students = {
    101: {
        "name": "Alice",
        "cgpa": 8.5
    },
    102: {
        "name": "Bob",
        "cgpa": 9.1
    }
}

print(students[101]["name"])