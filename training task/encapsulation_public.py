class StudentPublic:
    def __init__(self, name, age,address):
        self.name = name  
        self.age = age   
        self.address = address   

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

student = StudentPublic("Nitu", 20,"Moulovipara")

print("Original Details:")
student.display_details()

student.name = "Mou"
student.age = 22
student.address = "sonadanga"

print("Modified Details:")
student.display_details()
