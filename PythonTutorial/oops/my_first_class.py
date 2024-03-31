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
    
    def __init__(self, name, color, height, gender): # constructor with parameter
        self.name= name
        self.color=color
        self.height=height
        self.gender=gender
    
    def display_details(self):
        print(f"{self.name} is a human being in {self.color} color, {self.height} feet height and {self.gender} gender")
        # print("This is a Human being method")
        
    def talk(self):
        print("I'm talking")   
        
vivek=HumanBeing("Vivek","black", 5.3, "male") # Instantiation: created an object which belongs to HumanBeing class
vivek.display_details() # I called a method from HumanBeing class using vivek object
# print(id(vivek))
#"black", 5.3, "male"
#"white", 5.8, "male"
sumanth=HumanBeing("Sumanth", "white", 5.8, "male")
# print(id(sumanth))
sumanth.display_details()
print(vivek.name)
print(sumanth.color)
