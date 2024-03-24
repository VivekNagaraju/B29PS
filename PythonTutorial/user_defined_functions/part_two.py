'''
Types of arguments:
1. Formal arguments
    a. default arguments
    b. variable length (positional) arguments
    c. variable length keyword arguments
2. Actual arguments
    a. positional arguments
    b. keyword arguments
    
special cases:
> passing positional arguments and keyword arguments for single function

'''
def add(a=0, b=0): # default formal arguments
    print("a-->", a)
    print("b-->", b)
    c=a+b
    print("Sum-->", c)

def addition(*a): # variable length (positional) arguments
    c=0
    for i in a:
        c=c+i  
    print(c)
def display_details(**a): # variable length keyword arguments
    print(a)
    
def mixed_v_arg(*a,**b):   
    print(a, b) 
    
add(4, 2) # positional arguments
add(b=4, a=2) # keyword arguments
add(8, b=6)
# add(a=8, 6) # syntax error- positional argument can't be passed after keyword argument
# add(8, a=6) # TypeError: add() got multiple values for argument 'a'
add(2)
addition(1, 2, 6,3 ,4,5)
display_details(a=1, b=2, c=3, d=4, e=5)

mixed_v_arg(1, 2, 3, 4, c=3, d=4, e=5)
# mixed_v_arg(c=3, d=4, e=5, 1, 2, 3, 4)
