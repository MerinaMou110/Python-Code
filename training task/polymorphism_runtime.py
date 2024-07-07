class Student:
    def __init__(self, name):
        self.name = name

    def display_details(self):
        print(f"Name: {self.name}")

class UndergraduateStudent(Student):
    def __init__(self, name, year):
        super().__init__(name)
        self.year = year

    def display_details(self):  #derived function from base
        print("Undergraduate Student Details:")
        super().display_details()  
        print(f"Year: {self.year}")

class GraduateStudent(Student):
    def __init__(self, name, thesis_title):
        super().__init__(name)
        self.thesis_title = thesis_title

    def display_details(self):   #derived function from base
        print("Graduate Student Details:")
        super().display_details()
        print(f"Thesis Title: {self.thesis_title}")


undergrad = UndergraduateStudent("Nitu", 3)
grad = GraduateStudent("Mou", "Machine Learning in Healthcare")

print("Displaying Undergraduate Student Details:")
undergrad.display_details()

print("\nDisplaying Graduate Student Details:")
grad.display_details()
