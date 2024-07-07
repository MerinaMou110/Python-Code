class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_person_details(self):
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
        person_details = self.get_person_details()
        academic_details = self.get_academic_details()
        return f"{person_details}, {academic_details}, Student ID: {self.student_id}"


student = Student("Mou", 20, "NWU", "Computer Science", "S12345")
print(student.get_student_details())
