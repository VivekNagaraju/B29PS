'''
Encapsulation: wrapping data-elements (members) inside an entity

elements: variables, methods
entity: class

Capsule= a small case or container

1. Protected data-elements: 
    - elements can't be accessed outside the class, 
    but can be accessed within the class and its sub-classes
    - prefix the element with single underscore (_) 
      to denote that element is protected
2. Private data-elements:
    - elements can't be accessed outside the class or its sub-classes,
    but it can be accessed within the class
    - prefix the element with double underscore (__)
'''

class Parent:
    def __init__(self, name):
        self.__name=name
        
    def display_details(self):
        print(f"Parent name is {self.__name}")  
          
p1=Parent("amma")
p1.display_details()
print(p1._Parent__name) # name mangling technique
print(dir(p1))