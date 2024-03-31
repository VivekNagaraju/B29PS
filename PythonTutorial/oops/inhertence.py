'''
Inheritance:
1. Single level inheritance (GrandFather --> Father)
2. Multi-level inheritance (GrandFather --> Father --> Child)
3. Multiple inheritance (Father, Mother --> Child)

Method Resolution Order (MRO)
'''
class GrandFather:
    def gf_method(self):
        print("This is Gf method")
        
    def car(self):
        print("This is GF's car")
        
class Father(GrandFather):
    def f_method(self):
        print("This is father method")
        
    def car(self):
        print("This is Father's car")
        GrandFather.car(self)
        
class Mother:
    def m_method(self):
        print("This is mother method")
        
    def car(self):
        print("This is Mother's car")
        
class Child(Father, Mother):
    def c_method(self):
        print("This is child method") 
        
    def car(self):
        print("This is my car")
        Father.car(self)
        Mother.car(self)

print("=======GF========")               
ajja=GrandFather()
ajja.gf_method()


print("========Father=========")
appa=Father()
appa.f_method()
appa.gf_method()

print("=========Child=========")
myself=Child()
myself.c_method()
myself.f_method()
myself.gf_method()
myself.m_method()
myself.car()

print("=========MRO==========")
print(Child.mro())