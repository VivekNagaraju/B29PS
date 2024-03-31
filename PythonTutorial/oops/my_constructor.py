'''
Constructor: is a method used to construct an object
1. Constructor is not mandatory
2. Constructor will be called implicitly when an object is created
3. Constructor can be defined with/ without parameters
'''

class HumanBeing():
    def __init__(self): # constructor without parameter
        print("This is a constructor")
        
    def display_details(self):
        print("This is a Human being method")

sravani=HumanBeing()
sravani.__init__()
# sravani.display_details()  

# print(dir(sravani))    