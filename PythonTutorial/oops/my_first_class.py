'''
Method= every function defined inside a class
'''
'''defining a class'''
class HumanBeing():
    def display_details(self):
        print("I'm a human being")
        
vivek=HumanBeing() # Instantiation: created an object which belongs to HumanBeing class
vivek.display_details() # I called a method from HumanBeing class using vivek object
print(type(vivek))