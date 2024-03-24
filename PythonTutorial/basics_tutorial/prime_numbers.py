'''
Created on 23-Mar-2024

@author: admin
'''
a=int(input("Please enter a number:"))
if a==1:
        print("It's a prime number")
for i in range(2, a+1):
    b=a%i
    if b==0 and i<a:
        print("Not a prime number")
        break
    if b==0 and i==a:
        print("It's a prime number")