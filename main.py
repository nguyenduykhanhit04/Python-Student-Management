from models.student import Student
from utils.file_handler import load_data, save_data

FILE_PATH = "data/students.json"

student_1 = Student("S001", "Khanh", 22, 8.5)
student_2 = Student("S002", "An", 20, 7.8)

students = [student_1.to_dict(), student_2.to_dict()]

save_data(FILE_PATH, students)

loaded_students = load_data(FILE_PATH)
print(loaded_students)