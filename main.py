from models.student import Student
from services.student_manager import StudentManager

FILE_PATH = "data/students.json"


def show_menu():
    print("\n========== STUDENT MANAGEMENT ==========")
    print("1. Add student")
    print("2. Show all students")
    print("3. Find student by ID")
    print("4. Find student by name")
    print("5. Update student")
    print("6. Delete student")
    print("7. Exit")
    print("========================================")


def input_student_info():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

    try:
        age = int(input("Enter student age: ").strip())
        score = float(input("Enter student score: ").strip())
    except ValueError:
        print("Age must be an integer and score must be a number.")
        return None

    return Student(student_id, name, age, score)


def main():
    manager = StudentManager(FILE_PATH)

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            print("\n--- Add Student ---")
            student = input_student_info()

            if student is None:
                continue

            if manager.add_student(student):
                print("Student added successfully.")
            else:
                print("Student ID already exists.")

        elif choice == "2":
            print("\n--- Student List ---")
            manager.show_all_students()

        elif choice == "3":
            print("\n--- Find Student by ID ---")
            student_id = input("Enter student ID: ").strip()
            student = manager.find_student_by_id(student_id)

            if student:
                print("Student found:")
                print(student)
            else:
                print("Student not found.")

        elif choice == "4":
            print("\n--- Find Student by Name ---")
            keyword = input("Enter name keyword: ").strip()
            results = manager.find_students_by_name(keyword)

            if results:
                print("Matching students:")
                for student in results:
                    print(student)
            else:
                print("No matching students found.")

        elif choice == "5":
            print("\n--- Update Student ---")
            student_id = input("Enter student ID to update: ").strip()
            student = manager.find_student_by_id(student_id)

            if not student:
                print("Student not found.")
                continue

            print("Leave blank if you do not want to change a field.")

            new_name = input(f"Enter new name ({student.name}): ").strip()
            new_age_input = input(f"Enter new age ({student.age}): ").strip()
            new_score_input = input(f"Enter new score ({student.score}): ").strip()

            new_name = new_name if new_name else None

            try:
                new_age = int(new_age_input) if new_age_input else None
                new_score = float(new_score_input) if new_score_input else None
            except ValueError:
                print("Invalid age or score.")
                continue

            updated = manager.update_student(
                student_id,
                new_name=new_name,
                new_age=new_age,
                new_score=new_score
            )

            if updated:
                print("Student updated successfully.")
            else:
                print("Update failed.")

        elif choice == "6":
            print("\n--- Delete Student ---")
            student_id = input("Enter student ID to delete: ").strip()

            if manager.delete_student(student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose from 1 to 7.")


if __name__ == "__main__":
    main()