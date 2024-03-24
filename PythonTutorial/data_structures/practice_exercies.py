'''
Created on 23-Mar-2024

@author: admin
'''
a=[1, 3, 4 ,5 ,5, 3, 4, 5, 3]
b=a.copy()
i=0
while True:
    element=b[i]
    ele_count= b.count(element)
    print(f"{element}--> {ele_count} times")
    for j in range(ele_count):
        b.remove(element)
    if len(b)==0:
        break  
# print(a)       
        