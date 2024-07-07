class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_details(self):
        person_details = self.get_person_details()
        return f"{person_details}, Student ID: {self.student_id}"

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_title):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title

    def get_graduate_student_details(self):
        student_details = self.get_student_details()
        return f"{student_details}, Thesis Title: {self.thesis_title}"

grad_student = GraduateStudent("Mou", 23, "G43", "Machine Learning in Healthcare")
print(grad_student.get_graduate_student_details())
