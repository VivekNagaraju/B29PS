'''
Created on 23-Mar-2024

@author: admin
'''
c=[10, 20, 30, 40]
d={1:"Bhanu", 2:"Shashikala", 3:"Sravani", 4:"Sumanth"}
print(d)
print(d[1])
d[2]="shashi"
print(d)

print(d.fromkeys(c, "value"))

print(d.items())
print(d.keys())
print(d.values())