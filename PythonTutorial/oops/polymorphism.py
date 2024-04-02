'''
Polymorphism:
Poly= Many
Morph= form

1. Overloading:
    a. Operator overloading
        + -->  arithmetic addition of 2 Numerical data type objects
          --> combining  2 strings
          --> Extending a list with the elements of another list
    b. Method overloading: multiple methods with same name but different number of arguments
    c. Constructor overloading
2. Over-riding: 
    a. Method over-riding
    b. Constructor over-riding
'''

'''
# Operator overloading

print(2+4.9)
print("2" + "4.9")
print([1, 2, 3, 4] + [5, 6, 7, 8])
'''

# Method Overloading

class Example:
    def __init__(self, *b): # constructor overloading with the help of variable length arguments
        print(b)
        
    def method_one(self, *a): # method overloading with the help of variable length arguments
        print(a)
    
    def method_two(self, a=0, b=0, c=0, d=0):  # method overloading using default values
        print(a+b+c+d)  
        
obj1=Example(1, 2)
obj1.method_one(1, 3, 4)
obj1.method_one(1,3, 4, 5,6, 6, 7)
obj1.method_two()
obj1.method_two(1)
obj1.method_two(2, 4)
obj1.method_two(3, 5, 6, 7)