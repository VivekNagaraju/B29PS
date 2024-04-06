'''
Exception handling: Handling of abnormal/ unexpected behaviors

Types of errors:
1. Compile time errors: This can't be handled. Developer/ coder/ programmer is solely responsible for this
2. Run-time errors: these are unexpected and can be handled

How to handle exception?
- using single try - single except default block
- using single try - specific except block
- using single try - multiple specific except blocks
- using single try - multiple specific except and single except default block
- nested try - except blocks
- try-except-finally

'''

print(1+2) #3
print(5-3) #2
print(4*6) #24
try:
    try:
        print(9/3)

    except ZeroDivisionError as ze:
        print(ze)
    
except TypeError:
    print("TypeError: unsupported operand type(s) for /: 'int' and 'str'")
    
except Exception as e: # default except block
    print("Exception thrown at line 20:", e)
    
finally:
    print("This is 'finally' block")

print(2**4) #16
print(9//4) #2