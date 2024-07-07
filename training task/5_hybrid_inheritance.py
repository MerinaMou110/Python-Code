class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Academic:
    def __init__(self, institution, major):
        self.institution = institution
        self.major = major

    def get_academic_details(self):
        return f"Institution: {self.institution}, Major: {self.major}"

class Student(Person, Academic):
    def __init__(self, name, age, institution, major, student_id):
        Person.__init__(self, name, age)
        Academic.__init__(self, institution, major)
        self.student_id = student_id

    def get_student_details(self):
        person_details = self.get_details()
        academic_details = self.get_academic_details()
        return f"{person_details}, {academic_details}, Student ID: {self.student_id}"

class GraduateStudent(Student):
    def __init__(self, name, age, institution, major, student_id, thesis_title):
        super().__init__(name, age, institution, major, student_id)
        self.thesis_title = thesis_title

    def get_graduate_student_details(self):
        student_details = self.get_student_details()
        return f"{student_details}, Thesis Title: {self.thesis_title}"

grad_student = GraduateStudent("Mou", 23, "NWU", "Computer Science", "G12345", "Machine Learning in Healthcare")
print(grad_student.get_graduate_student_details())
