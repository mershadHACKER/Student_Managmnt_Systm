import csv

FILE_NAME = "dataset/students.csv"


def view_students():
    """Display all students in the dataset."""
    
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\nStudent Records")
        print("-" * 70)

        for student in reader:
            print(
                f"ID: {student['student_id']} | "
                f"Name: {student['name']} | "
                f"Age: {student['age']} | "
                f"Course: {student['course']} | "
                f"Attendance: {student['attendance']}%"
            )


def add_student():
    """Add a new student to the dataset."""

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter course: ")
    attendance = input("Enter attendance percentage: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            student_id,
            name,
            age,
            course,
            attendance
        ])

    print("Student added successfully.")


def search_student():
    """Search for a student using student ID."""

    student_id = input("Enter student ID: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["student_id"] == student_id:
                print("\nStudent Found")
                print("-" * 30)
                print(f"ID: {student['student_id']}")
                print(f"Name: {student['name']}")
                print(f"Age: {student['age']}")
                print(f"Course: {student['course']}")
                print(f"Attendance: {student['attendance']}%")
                return

    print("Student not found.")


def delete_student():
    """Delete a student using student ID."""

    student_id = input("Enter student ID to delete: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    found = False

    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            found = True
            break

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = [
                "student_id",
                "name",
                "age",
                "course",
                "attendance"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)

        print("Student deleted successfully.")
    else:
        print("Student not found.")


def main():
    """Display the dataset management menu."""

    while True:
        print("\n===== Student Dataset Management =====")
        print("1. View students")
        print("2. Add student")
        print("3. Search student")
        print("4. Delete student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_students()

        elif choice == "2":
            add_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()