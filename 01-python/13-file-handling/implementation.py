try:
    with open("01-python/13-file-handling/students.csv", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("students.csv not found.")