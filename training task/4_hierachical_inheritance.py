class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_student_details(self):
        person_details = self.get_details()
        return f"{person_details}, Student ID: {self.student_id}"

class Teacher(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_teacher_details(self):
        person_details = self.get_details()
        return f"{person_details}, Employee ID: {self.employee_id}"

student = Student("Nitu", 20, "S19")
teacher = Teacher("sadia", 35, "T89")

print(student.get_student_details())
print(teacher.get_teacher_details())
