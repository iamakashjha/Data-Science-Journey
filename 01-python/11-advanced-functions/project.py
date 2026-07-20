students = {
    "Rahul": [85, 90, 88],
    "Alice": [92, 95, 91],
    "Bob": [70, 75, 80]
}


def calculate_average(scores):
    return sum(scores) / len(scores)

for student, scores in students.items():
    average = calculate_average(scores)
    print(f"{student}: {average:.2f}")

def calculate_highest(student_scores):
    highest_score = 0
    top_student = ""
    for student, scores in student_scores.items():
        average = calculate_average(scores)
        if average > highest_score:
            highest_score = average
            top_student = student
    print(f"Highest Average Score: {top_student} with {highest_score:.2f}")

def calculate_lowest(student_scores):
    lowest_score = float('inf')
    bottom_student = ""
    for student, scores in student_scores.items():
        average = calculate_average(scores)
        if average < lowest_score:
            lowest_score = average
            bottom_student = student
    print(f"Lowest Average Score: {bottom_student} with {lowest_score:.2f}")

def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    else:
        return "C"

def generate_report(student_scores):
    print("Student Report:")
    print("-" * 30)
    for student, scores in student_scores.items():
        average = calculate_average(scores)
        grade = assign_grade(average)
        print(f"{student}: {average:.2f} ({grade})")


print("\nCalculating Highest and Lowest Average Scores:")
calculate_highest(students)
calculate_lowest(students)
generate_report(students)
assign_grade(85)
