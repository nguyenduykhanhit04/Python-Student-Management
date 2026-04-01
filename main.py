from models.student import Student
from services.student_manager import StudentManager

FILE_PATH = "data/students.json"

manager = StudentManager(FILE_PATH)

student_1 = Student("S001", "Khanh", 22, 8.5)
student_2 = Student("S002", "An", 20, 7.8)
student_3 = Student("S003", "Nam", 21, 9.0)

print("=== TEST ADD STUDENT ===")
print(manager.add_student(student_1))
print(manager.add_student(student_2))
print(manager.add_student(student_3))

print("\n=== TEST SHOW ALL ===")
manager.show_all_students()

print("\n=== TEST FIND BY ID ===")
found_student = manager.find_student_by_id("S002")
print(found_student)

print("\n=== TEST FIND BY NAME ===")
students_by_name = manager.find_students_by_name("na")
for student in students_by_name:
    print(student)

print("\n=== TEST UPDATE ===")
updated = manager.update_student("S001", new_name="Nguyen Duy Khanh", new_age=23, new_score=9.2)
print("Update result:", updated)
manager.show_all_students()

print("\n=== TEST DELETE ===")
deleted = manager.delete_student("S002")
print("Delete result:", deleted)
manager.show_all_students()