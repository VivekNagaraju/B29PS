'''
Constructor Inheritance:
1. Parent class Constructor will be inherited and called implicitly
         when child class object is created
'''
class GrandFather:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("This is GF Constructor")
        
    def gf_method(self):
        print(f"GF name is {self.name} and {self.age} years old ")
        
class Father(GrandFather):
    def __init__(self, name, age, aadhaar_id):
        print("This is Father class constructor")
        # self.name=name
        # self.age=age
        self.aadhaar_id=aadhaar_id
        # GrandFather.__init__(self, name, age)
        super().__init__(name, age)
        
    def f_method(self):
        print(f"Father's name is {self.name}, {self.age} years old and has aadhaar_id {self.aadhaar_id}")
        
    def car(self):
        print("This is Father's car")
        
print("=======GF========")               
ajja=GrandFather("ajja", 99)
ajja.gf_method()

print("========Father=========")
appa=Father("appa", 69, 1001)
appa.f_method()

