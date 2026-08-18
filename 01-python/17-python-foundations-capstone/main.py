from student import Student, get_valid_marks
from statistics_utils import calculate_class_average, find_topper
import json
import os

class StudentManager:
    def __init__(self):
        self.students = []
        self.filename = "students_data.json"
    
    def add_student(self):
        """Add a new student to the system"""
        try:
            roll_no = int(input("Enter Roll Number: "))
            name = input("Enter Student Name: ")
            num_subjects = int(input("Enter number of subjects: "))
            marks = get_valid_marks(num_subjects)
            
            student = Student(roll_no, name, marks)
            self.students.append(student)
            print(f"✓ Student {name} added successfully!\n")
        except ValueError as e:
            print(f"Error: Invalid input. {e}\n")
    
    def display_students(self):
        """Display all students"""
        if not self.students:
            print("No students in the system.\n")
            return
        
        print("\n" + "="*50)
        for student in self.students:
            student.display()
            print("-"*50)
        print()
    
    def class_statistics(self):
        """Display class statistics"""
        if not self.students:
            print("No students in the system.\n")
            return
        
        class_avg = calculate_class_average(self.students)
        print(f"\nClass Average: {class_avg:.2f}\n")
    
    def find_topper(self):
        """Find and display the topper"""
        if not self.students:
            print("No students in the system.\n")
            return
        
        topper = find_topper(self.students)
        print(f"\nTopper Student: {topper.name}")
        print(f"Average Score: {topper.average():.2f}\n")
    
    def save_students(self):
        """Save students to JSON file"""
        try:
            data = []
            for student in self.students:
                data.append({
                    "roll_no": student.roll_no,
                    "name": student.name,
                    "marks": student.marks
                })
            
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"✓ Students saved to {self.filename}\n")
        except Exception as e:
            print(f"Error saving students: {e}\n")
    
    def load_students(self):
        """Load students from JSON file"""
        try:
            if not os.path.exists(self.filename):
                print(f"File {self.filename} not found.\n")
                return
            
            with open(self.filename, 'r') as f:
                data = json.load(f)
            
            self.students = []
            for item in data:
                student = Student(item["roll_no"], item["name"], item["marks"])
                self.students.append(student)
            print(f"✓ Students loaded from {self.filename}\n")
        except Exception as e:
            print(f"Error loading students: {e}\n")
    
    def search_student(self):
        """Search for a student by roll number"""
        try:
            roll_no = int(input("Enter Student ID: "))
            for student in self.students:
                if student.roll_no == roll_no:
                    print("\nStudent Found")
                    student.display()
                    print()
                    return
            print("Student not found.\n")
        except ValueError:
            print("Error: Please enter a valid number.\n")
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*50)
        print("Student Performance Manager")
        print("="*50)
        print("1. Add Student")
        print("2. Display Students")
        print("3. Class Statistics")
        print("4. Find Topper")
        print("5. Search Student")
        print("6. Save Students")
        print("7. Load Students")
        print("8. Exit")
        print("="*50)
    
    def run(self):
        """Main program loop"""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.class_statistics()
            elif choice == '4':
                self.find_topper()
            elif choice == '5':
                self.search_student()
            elif choice == '6':
                self.save_students()
            elif choice == '7':
                self.load_students()
            elif choice == '8':
                print("Thank you for using Student Performance Manager. Goodbye!\n")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.\n")

if __name__ == "__main__":
    manager = StudentManager()
    manager.run()