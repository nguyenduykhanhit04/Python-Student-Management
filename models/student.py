class Student:
    def __init__(self, student_id, name, age, score):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score = score

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["score"]
        )

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Score: {self.score}"