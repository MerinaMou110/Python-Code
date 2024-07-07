# Abstract Classes:
# Definition: Abstract classes can have both abstract methods (methods without implementation) and concrete methods (methods with implementation).

# Interfaces:
# Definition: Interfaces contain only method signatures without any implementation.

from abc import ABC, abstractmethod
#  abstract base class

class Animal(ABC):
    @abstractmethod    #enforce all derived class to have eat method      
    def eat(self):
        print('I need food')

    @abstractmethod 
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.name='monkey'
        self.name=name
        super().__init__()

    def eat(self):
        print('Hey auny, you are sweet')
    def move(self):
        print('Hanging on the branches')
layka=Monkey('lucky')
layka.eat()


