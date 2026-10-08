"""Student Grade Management System using Python coding standards."""
import math

class Student:
    """Represent a student and manage academic grades."""
    def __init__(self, student_id, name):
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        if isinstance(grade, bool) or not isinstance(grade, (int, float)):
            print("Error: Grade must be numeric.")
            return False

        if not math.isfinite(grade):
            print("Error: Grade must be a finite number.")
            return False

        if not 0 <= grade <= 100:
            print("Error: Grade must be between 0 and 100.")
            return False

        self.grades.append(grade)
        return True

    def calculate_average(self):
        """Calculate the arithmetic mean of the student's grades."""
        if not self.grades:
            return 0.0

        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def check_honor(self):
        self.honor = bool(self.grades) and self.calculate_average() >= 90
        return self.honor

    def check_passed(self):
        self.is_passed = bool(self.grades) and self.calculate_average() >= 60
        return self.is_passed

    def remove_grade_by_index(self, index):
        if isinstance(index, bool) or not isinstance(index, int):
            print("Error: Index must be an integer.")
            return False

        if not 0 <= index < len(self.grades):
            print("Error: Grade index is out of range.")
            return False

        self.grades.pop(index)
        return True

    def remove_grade_by_value(self, grade):
        if grade not in self.grades:
            print("Error: Grade was not found.")
            return False

        self.grades.remove(grade)
        return True

    def report(self):
        self.check_passed()
        self.check_honor()

        print("\n--- STUDENT REPORT ---")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {self.calculate_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")
        print(f"Status: {'Passed' if self.is_passed else 'Failed'}")
        print(f"Honor Roll: {self.honor}")


def start_run():
    try:
        student = Student("2026001", "Jose")

        student.add_grade(100)
        student.add_grade(50)
        student.add_grade(150)
        student.add_grade(75)
        student.add_grade(75)
        student.add_grade(75)
        student.add_grade(75)
        student.add_grade(75)
        student.add_grade("Fifty")

        student.report()

        student.remove_grade_by_index(5)
        student.remove_grade_by_index(100)
        student.remove_grade_by_value(50)
        student.remove_grade_by_value(200)

        student.report()

        Student("", "Invalid Student")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    start_run()
