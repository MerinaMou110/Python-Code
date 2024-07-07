
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_details(self):
        return f"Name: {self.name}, Student ID: {self.student_id}"


class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_title):
        super().__init__(name, student_id)  
        self.thesis_title = thesis_title

    def get_details(self):
        base_details = super().get_details()  
        return f"{base_details}, Thesis Title: {self.thesis_title}"


grad_student = GraduateStudent("Mou", "43", "Object oriented program")
print(grad_student.get_details())
