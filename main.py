
import json
import os

FILE_NAME = "students.json"
SUBJECTS = ["English", "Mathematics", "Computer Science", "Physics", "Chemistry"]


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read the saved file. Starting with an empty list.")
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def add_student(students):
    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    roll_number = input("Enter roll number: ").strip()
    if not roll_number:
        print("Roll number cannot be empty.")
        return

    for student in students:
        if student["roll_number"] == roll_number:
            print("This roll number already exists.")
            return

    marks = {}

    for subject in SUBJECTS:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks.values())
    percentage = total / len(SUBJECTS)
    grade = calculate_grade(percentage)

    student = {
        "name": name,
        "roll_number": roll_number,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)
    save_students(students)

    print("\nStudent added successfully!")
    print(f"Total: {total:.2f} / {len(SUBJECTS) * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


def view_students(students):
    print("\n--- All Student Records ---")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("-" * 35)
        print(f"Name: {student['name']}")
        print(f"Roll Number: {student['roll_number']}")

        for subject, mark in student["marks"].items():
            print(f"{subject}: {mark:g}")

        print(f"Total: {student['total']:.2f} / {len(SUBJECTS) * 100}")
        print(f"Percentage: {student['percentage']:.2f}%")
        print(f"Grade: {student['grade']}")


def search_student(students):
    print("\n--- Search Student ---")
    roll_number = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll_number"] == roll_number:
            print(f"\nName: {student['name']}")
            print(f"Roll Number: {student['roll_number']}")

            for subject, mark in student["marks"].items():
                print(f"{subject}: {mark:g}")

            print(f"Total: {student['total']:.2f}")
            print(f"Percentage: {student['percentage']:.2f}%")
            print(f"Grade: {student['grade']}")
            return

    print("Student not found.")


def delete_student(students):
    print("\n--- Delete Student ---")
    roll_number = input("Enter roll number to delete: ").strip()

    for student in students:
        if student["roll_number"] == roll_number:
            students.remove(student)
            save_students(students)
            print("Student record deleted successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== Student Marks Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
