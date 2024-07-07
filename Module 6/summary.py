class Book:
    def __init__(self,name) -> None:
        self.name=name

    def read(self):
        print('reading physics')
class physics(Book):
    def __init__(self,name,lab) -> None:
        self.lab=lab
        super().__init__(name)

topon=physics('topn',True)

print(issubclass(physics,Book))   #check physics book er subclass kina 
print(isinstance(topon,physics))
print(isinstance(topon,Book))
topon.read()
