'''
Created on 23-Mar-2024

@author: admin
'''
'''
a=2
b=3
c=a+b
print(c)
    
a=4
b=6
c=a+b
print(c)
'''
def add(a, b):
    c=a+b
    return c

def sub(a, b):
    d=a-b
    return d
def add_sub(a, b): # function with parameters/ arguments (formal arguments)
    c=add(a, b)
    d=sub(a, b)
    # print(c)
    # print(d)
    return c, d
    
e, f=add_sub(2, 3) # actual arguments
# print(e)
# print(f)
# print(add(4, 5)) 
# print(sub(7, 3))
# def display(): # recursive functions
#     print("This is display function")
#     display()
#
#
# display()
    
    