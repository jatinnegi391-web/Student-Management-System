import csv
import os

FILE_NAME = "students.csv"


class Student:
    """Represents one student record."""

    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }


class StudentManager:
    """Handles student CRUD operations and file persistence."""

    def __init__(self, filename=FILE_NAME):
        self.filename = filename
        self.students = []
        self.load_students()

    def load_students(self):
        self.students = []
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.students.append(
                    Student(row["id"], row["name"], row["grade"])
                )

    def save_students(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "name", "grade"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in self.students:
                writer.writerow(student.to_dict())

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def add_student(self, student):
        if self.find_student(student.student_id):
            raise ValueError("Student ID already exists.")
        self.students.append(student)
        self.save_students()

    def update_student(self, student_id, name, grade):
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found.")
        student.name = name
        student.grade = grade
        self.save_students()

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found.")
        self.students.remove(student)
        self.save_students()

    def list_students(self):
        return self.students


def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty.")


def print_students(students):
    if not students:
        print("\nNo student records found.")
        return

    print("\n" + "-" * 55)
    print(f"{'ID':<15}{'Name':<25}{'Grade':<15}")
    print("-" * 55)
    for student in students:
        print(f"{student.student_id:<15}{student.name:<25}{student.grade:<15}")
    print("-" * 55)


def main():
    manager = StudentManager()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                student_id = get_non_empty("Enter Student ID: ")
                name = get_non_empty("Enter Student Name: ")
                grade = get_non_empty("Enter Grade: ")

                manager.add_student(Student(student_id, name, grade))
                print("Student added successfully.")

            elif choice == "2":
                student_id = get_non_empty("Enter Student ID to update: ")
                name = get_non_empty("Enter new name: ")
                grade = get_non_empty("Enter new grade: ")

                manager.update_student(student_id, name, grade)
                print("Student updated successfully.")

            elif choice == "3":
                student_id = get_non_empty("Enter Student ID to delete: ")
                manager.delete_student(student_id)
                print("Student deleted successfully.")

            elif choice == "4":
                print_students(manager.list_students())

            elif choice == "5":
                print("Thank you for using Student Management System.")
                break

            else:
                print("Invalid choice. Please select 1-5.")

        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
