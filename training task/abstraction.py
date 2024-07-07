from abc import ABC, abstractmethod

class Student(ABC):
    @abstractmethod
    def display_details(self):
        pass

class UndergraduateStudent(Student):
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def display_details(self):
        print("Undergraduate Student:")
        print(f"Name: {self.name}")
        print(f"Year: {self.year}")

class GraduateStudent(Student):
    def __init__(self, name, thesis_title):
        self.name = name
        self.thesis_title = thesis_title

    def display_details(self):
        print("Graduate Student:")
        print(f"Name: {self.name}")
        print(f"Thesis Title: {self.thesis_title}")


undergrad = UndergraduateStudent("Muni", 3)
grad = GraduateStudent("Nazim", "Machine Learning in Healthcare")

undergrad.display_details()
grad.display_details()
