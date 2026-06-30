student_1 = ("Rahul", 22, "Python", 8.9)

student_2 = ("Akash", 22, "Java", 9.6)

Name_1, Age_1, Favorite_Language_1, CGPA_1 = student_1
Name_2, Age_2, Favorite_Language_2, CGPA_2 = student_2

print(f"Name: {Name_1}")
print(f"Age: {Age_1}")
print(f"Favorite Language: {Favorite_Language_1}")
print(f"CGPA: {CGPA_1}")

print(f"Name: {Name_2}")
print(f"Age: {Age_2}")
print(f"Favorite Language: {Favorite_Language_2}")
print(f"CGPA: {CGPA_2}")


locations = [
    ("Library", (10,20)),
    ("Cafe", (25,18)),
    ("Office", (30,12))
]

for location in locations:
    name, coordinates = location
    x, y = coordinates
    print(f"Location: {name}, Coordinates: ({x}, {y})")