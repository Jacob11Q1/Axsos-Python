# Student System Management Project

# Ask for student's name
student_name = input("Enter the student's name: ")

# Define the Student class
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        if grade >= 60:
            print(f"Student {self.name} passed this grade entry: {grade}")
        else:
            print(f"Student {self.name} failed this grade entry: {grade}")
        return self

    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def print_report(self):
        print(f"\n--- Report For {self.name} ---")
        print(f"Grades: {self.grades}")
        average = self.get_average()
        print(f"Average Grade: {average:.2f}")
        if average >= 60:
            print("Status: Passed overall ✅")
        else:
            print("Status: Failed overall ❌")
        return self

# Create a student object
student = Student(student_name)

# Ask how many grades to enter
num = int(input("How many grades do you want to enter? "))

# Add grades using a loop
for i in range(num):
    grade = float(input(f"Enter grade #{i + 1}: "))
    student.add_grade(grade)

# Print final report
student.print_report()