class StudentPrivate:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age    

    def get_name(self):
        return self.__name

   
    def set_name(self, name):
        self.__name = name

  
    def get_age(self):
        return self.__age


    def set_age(self, age):
        self.__age = age

    def display_details(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


student = StudentPrivate("Mohua", 20)

print("Original Details:")
student.display_details()

student.set_name("Mukta")
student.set_age(22)

print("Modified Details:")
student.display_details()
