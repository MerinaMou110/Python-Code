from math import pi

class Shape:
    def __init__(self,name) -> None:
        self.name=name
class Rectangle(Shape):
    def __init__(self, name,length,width) -> None:
        self.length=length
        self.width=width
        super().__init__(name)

    def area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self, name,radius) -> None:
        self.radius=radius
        super().__init__(name)

    def area(self):
        return pi*self.radius*self.radius
    




    # another example

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for shape in shapes:
 print(f"Area of the shape is: {shape.area()}")
