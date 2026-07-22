import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

students = []
student_id = 1


def load_students():
    global students, student_id

    try:
        with open(DATA_FILE, "r") as file:
            students = json.load(file)

            if len(students) > 0:
                student_id = students[-1]["id"] + 1

    except (FileNotFoundError, json.JSONDecodeError):
        students = []


def save_students():
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    global student_id

    while True:
        name = input("Enter student name: ").strip()

        if name == "":
            print("Name cannot be empty.")
        else:
            break

    while True:
        age = input("Enter student age: ")

        if age.isdigit():
            break
        else:
            print("Age must be a number.")

    student = {
        "id": student_id,
        "name": name,
        "age": int(age)
    }

    students.append(student)
    save_students()

    student_id += 1

    print("Student added successfully!")


def show_students():
    if len(students) == 0:
        print("\nNo students found.")
    else:
        print("\n===== Students List =====")
        for student in students:
            print(
                f"ID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Age: {student['age']}"
            )


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found!")
            print(
                f"ID: {student['id']} | "
                f"Name: {student['name']} | "
                f"Age: {student['age']}"
            )
            return

    print("Student not found.")

def delete_student():
    student_id_delete = int(input("Enter student ID to delete: "))

    for student in students:
        if student["id"] == student_id_delete:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return

    print("Student not found")
load_students()

def update_student():
    student_id_update = input("Enter student ID to update: ")

    if not student_id_update.isdigit():
        print("Invalid ID.")
        return

    student_id_update = int(student_id_update)

    for student in students:
        if student["id"] == student_id_update:

            while True:
                new_name = input("Enter new name: ").strip()

                if new_name == "":
                    print("Name cannot be empty.")
                else:
                    break

            while True:
                new_age = input("Enter new age: ")

                if new_age.isdigit():
                    break
                else:
                    print("Age must be a number.")

            student["name"] = new_name
            student["age"] = int(new_age)

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")

