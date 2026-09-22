# Syntecxhub - Student Management System

A simple Python CLI-based Student Management System created for the Syntecxhub Internship Project 1.

## Features

- Add student records
- Update student records
- Delete student records
- List all students
- Unique Student ID validation
- Formatted console output
- CSV file persistence
- Object-Oriented Programming using `Student` and `StudentManager`
- File I/O using Python's built-in `csv` module

## Project Structure

```text
Syntecxhub_Student_Management_System/
├── student_management.py
├── students.csv
├── README.md
└── .gitignore
```

## Requirements

- Python 3.8 or higher
- No external libraries are required.

## How to Run

Open a terminal in the project folder and run:

```bash
python student_management.py
```

On some systems, use:

```bash
python3 student_management.py
```

## Student Data

Student records are automatically stored in `students.csv`.

The CSV format is:

```text
id,name,grade
```

## Example

```text
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Update Student
3. Delete Student
4. List Students
5. Exit

Enter your choice: 1
Enter Student ID: S101
Enter Student Name: Rahul
Enter Grade: A
Student added successfully.
```

## Internship Requirement Mapping

| Requirement | Implementation |
|---|---|
| Add / update / delete / list | `StudentManager` CRUD methods |
| Classes | `Student` and `StudentManager` |
| Persistence | `students.csv` |
| Validation | Unique Student ID and non-empty input |
| Formatted output | `print_students()` |
| File I/O | Python `csv` module |
| OOP basics | Constructors, classes, methods |

## Author

Jatin

## License

This project is created for educational/internship purposes.
