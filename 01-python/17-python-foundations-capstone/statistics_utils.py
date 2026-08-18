def calculate_class_average(students):
    """Calculate the average marks of the entire class"""
    if not students:
        return 0
    total = sum(student.average() for student in students)
    return total / len(students)

def find_topper(students):
    """Find the student with the highest average"""
    return max(students, key=lambda student: student.average())

def highest_subject_average(students):
    """Find which subject has the highest class average"""
    if not students:
        return None
    
    subject_totals = {}
    for student in students:
        for subject, mark in student.marks.items():
            if subject not in subject_totals:
                subject_totals[subject] = []
            subject_totals[subject].append(mark)
    
    subject_averages = {subject: sum(marks) / len(marks) for subject, marks in subject_totals.items()}
    return max(subject_averages, key=subject_averages.get)

def get_subject_class_average(students, subject):
    """Get class average for a specific subject"""
    marks = [student.marks.get(subject) for student in students if subject in student.marks]
    if not marks:
        return 0
    return sum(marks) / len(marks)

def get_subject_score(self):
    """Get a student's score in a specific subject"""
    try:
        roll_no = int(input("Enter Student ID: "))
        student = None
        for s in self.students:
            if s.roll_no == roll_no:
                student = s
                break
            
        if not student:
            print("Student not found.\n")
            return
            
        subject = input("Enter subject name: ")
        score = student.get_subject_score(subject)
        print(f"\n{student.name}'s {subject} score: {score}\n")
    except ValueError:
        print("Error: Please enter a valid number.\n")
    
    def subject_class_average(self):
        """Find class average for a specific subject"""
        from statistics_utils import get_subject_class_average
        
        if not self.students:
            print("No students in the system.\n")
            return
        
        subject = input("Enter subject name: ")
        avg = get_subject_class_average(self.students, subject)
        if avg == 0:
            print(f"No marks found for subject: {subject}\n")
        else:
            print(f"\nClass average for {subject}: {avg:.2f}\n")
    
    def highest_subject_average(self):
        """Find subject with highest class average"""
        from statistics_utils import highest_subject_average
        
        if not self.students:
            print("No students in the system.\n")
            return
        
        top_subject = highest_subject_average(self.students)
        from statistics_utils import get_subject_class_average
        avg = get_subject_class_average(self.students, top_subject)
        print(f"\nSubject with highest average: {top_subject} ({avg:.2f})\n")