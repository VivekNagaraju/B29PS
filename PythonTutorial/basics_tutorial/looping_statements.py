'''
Looping statements: to execute any code repeatedly
1. While loop: executes code repeatedly until condition is fulfilled 
(as long as condition is satisfied)
    a. initialization of conditional variable
    b. define loop with the condition
    c. Increment/ decrement section
2. For loop: executes a code repeatedly based on the 
                sequence or range provided
                
                for loop iterates over the sequence of objects/ elements

Loop control statements:
1. break
2. continue (skip)
'''
'''
count=1

while count<=200:
    # print(count<=5)
    if count==100:
        count=count+1
        continue
    print(count)
    count=count+1  
    # if count==100:
    #     break
'''    
''' 
for count in range(5):
    print("Hello, world!")

'''
'''
for i in "shashikala":
    if i=="i":
        continue
    print(i)
    # if i=="i":
    #     break
'''
'''
for i in range(1, 20, 2):
    print(i)
    
'''
'''
*
**
***
****
*****

   *
  ***
 *****
*******

*****
****
***
**
*

*******
 *****
  ***
   *
   
*
**
***
****
*****
******
*****
****
***
**
*

*****
****
***
**
*
*
**
***
****
*****

1
12
123
1234
12345

A
AB
ABC
ABCD
ABCDE
'''

for i in range(5): # row
    for j in range(5-i): # column
        print("*", end=" ")
    print()
    