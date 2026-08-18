class Student:

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = self._validate_marks(marks)
    
    def _validate_marks(self, marks):
        """Validate that all marks are between 0 and 100"""
        validated_marks = {}
        for subject, mark in marks.items():
            try:
                mark_int = int(mark)
                if mark_int < 0 or mark_int > 100:
                    raise ValueError(f"Mark {mark_int} is out of range. Marks must be between 0 and 100.")
                validated_marks[subject] = mark_int
            except ValueError as e:
                print(f"Error: {e}")
                raise
        return validated_marks
    
    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def highest_mark(self):
        return max(self.marks.values()) if self.marks else 0

    def lowest_mark(self):
        return min(self.marks.values()) if self.marks else 0

    def grade(self):
        average = self.average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    def get_subject_score(self, subject):
        """Get score for a specific subject"""
        return self.marks.get(subject, "Subject not found")

    def display(self):
        print(f"ID: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.average():.2f}")
        print(f"Grade: {self.grade()}")

def get_valid_marks(num_subjects):
    """Get marks from user with validation"""
    marks = {}
    for i in range(num_subjects):
        while True:
            subject = input(f"Enter subject name {i+1}: ")
            try:
                mark = int(input(f"Enter marks for {subject}: "))
                if mark < 0 or mark > 100:
                    print("Please enter a valid number between 0 and 100.")
                    continue
                marks[subject] = mark
                break
            except ValueError:
                print("Please enter a valid number.")
    return marks