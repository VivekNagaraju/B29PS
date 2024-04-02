'''
Abstraction: existing in idea but not yet implemented
Types of method:
1. implemented method
2. unimplemented method

abstract class: a class having one or more abstract methods
- an abstract class can have both implemented and unimplemented methods
- if an abstract class contains abstract methods only, then it is called as an 'Interface'.

- Concrete classes, abstract classes, Interfaces

Implementation of abstraction:
1. from abc module import everything (from abc import *)
2. Inherit ABC class into your abstract class
3. add @abstractmethod decorator to the methods which are to considered as abstract methods

Note:

1. We can't create an object from the abstract class unless abstractmethod is implemented
2. We can't create an object from sub-classes (child classes) of abstract class unless abstractmethod is implemented
'''
from abc import *

class Car(ABC):
    def __init__(self, color, seats, wheels=4):
        self.color=color
        self.wheels=wheels
        self.seats=seats
        print("Car object is created successfully")
        
    def move_forward(self): # implemented method
        print("Car is moving forward")
      
        
    def move_backward(self):
        print("Car is moving backward")
      
    @abstractmethod  
    def engine_specifications(self): # unimplemented method
        pass
       
class HatchBack(Car):
    def hb_function(self):
        print("This is HatchBack class function")
    
    def engine_specifications(self):
        print("engine_specifications defined")   

# car1=Car("red", 8)

swift=HatchBack("white", 4)      