#base class,parent class,common attribute+functionality class
# derived class,child class,uncommon attribute+functionality


class Gadget:
    def __init__(self,brand,price,color,origin) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin

    def run(self):
        return f'Running lapto: {self.brand}'
        
class Laptop:
    def __init__(self,memory,ssd) -> None:
        self.memory=memory
        self.ssd=ssd
    
    
    
    def coding(self):
        return f'learning python and practicing'
    
class phone(Gadget):
    def __init__(self,brand,price,color,origin,dual_sim) -> None:
        self.dual_sim=dual_sim
        super().__init__(brand,price,color,origin)
   
    def phone_call(self,number,text):
        return f'Sending SMS to: {number} with : {text}'
    
    def __repr__(self) -> str:
        
        return f'phone: {self.brand} {self.price} {self.dual_sim}'
    
class Camera:
    def __init__(self,pixel) -> None:
        
        self.pixel=pixel

   
    def change_lens(self):
        pass
        

# inheritance
my_phone=phone(True)
my_phone.brand

print(my_phone)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self) -> str:
#         return f"Point({self.x}, {self.y})"

# # Creating an instance of the Point class
# p = Point(3, 5)

# # Printing the object representation using repr()
# print(p)  # Output: Point(3, 5)
