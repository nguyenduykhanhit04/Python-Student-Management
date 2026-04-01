from models.student import Student
from utils.file_handler import load_data, save_data


class StudentManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.students = []
        self.load_students()

    def load_students(self):
        data = load_data(self.file_path)
        self.students = [Student.from_dict(item) for item in data]

    def save_students(self):
        data = [student.to_dict() for student in self.students]
        save_data(self.file_path, data)

    def add_student(self, student):
        if self.find_student_by_id(student.student_id):
            return False
        self.students.append(student)
        self.save_students()
        return True

    def show_all_students(self):
        if not self.students:
            print("Danh sách sinh viên đang trống.")
            return

        print("\n=== DANH SÁCH SINH VIÊN ===")
        for student in self.students:
            print(student)

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_students_by_name(self, keyword):
        result = []
        keyword = keyword.lower()

        for student in self.students:
            if keyword in student.name.lower():
                result.append(student)

        return result

    def update_student(self, student_id, new_name=None, new_age=None, new_score=None):
        student = self.find_student_by_id(student_id)

        if not student:
            return False

        if new_name is not None:
            student.name = new_name
        if new_age is not None:
            student.age = new_age
        if new_score is not None:
            student.score = new_score

        self.save_students()
        return True

    def delete_student(self, student_id):
        student = self.find_student_by_id(student_id)

        if not student:
            return False

        self.students.remove(student)
        self.save_students()
        return True