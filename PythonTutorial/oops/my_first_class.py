'''
Method= every function defined inside a class
<class 'int'> type(a)
<class '__main__.HumanBeing'> type(vivek)

<class 'class name'>
a= b, b=c >> a=c

language which supports OOP:
Language based on OOP:

'''
'''defining a class'''
class HumanBeing():
    def __init__(self, color, height, gender):
        self.color=color
        self.height=height
        self.gender=gender
    
    def display_details(self):
        print(f"I'm a human being in {self.color} color, {self.height} feet height and {self.gender} gender")
        
vivek=HumanBeing("black", 5.3, "male") # Instantiation: created an object which belongs to HumanBeing class
vivek.display_details() # I called a method from HumanBeing class using vivek object


sumanth=HumanBeing("white", 5.8, "male")
sumanth.display_details()

