'''
List:
1. We can create an empty list
2. List is heterogeneous (opp. homogeneous)
3. Accessing elements from the list:
    
    b. By using Slicing operator
    c. By using Loops
    
    Index: Position value of any element present in the list
    from left to right -->0, 1, 2....
    from right to left --> -1, -2, -3.....
    
    syntex: list_name[] --> common for all data structures
    
4. List is mutable 
5. List stores duplicate values
6. Insertion order is preserved- list will not sort the elements by default
'''
'''
a=[] # 1. We can create an empty list
print("a",type(a))
print("a", a)

b=[1, 2, 3, "Bhanu", "Sravani", 3.5, True, 3+5j] # 2. List is heterogeneous
print("b", b)

c=list(range(2, 21, 2))  #tuple, set()
print("c list before modifying", c)
# print(c[6])
# print(c[-6])
c[6]=15
print("c list after modifying", c)

d=[1, 2, 3, 3, 4, 5, 6, 6]
print("d", d)

e=[5, 7, 5, 6, 4, 1, 3, 2, 8]
print("e", e)
print("=========e list elements using for loop==========")
for i in e:
    print(i)

print("==========c list elements using while loop=========")
i=0 # index value
print("Length of the list",len(c))
while i<len(c):
    print(c[i])
    i=i+1
'''

c=list(range(2, 21, 2))
print("c-->", c)
d=[1, 2, 3, 4]
print("d-->", d)

c.append(56) # append value
print("c after appending 56-->")
print(c)

# c.append(d)
# print("c after appending d-->")
# print(c)

print(c[10])
# print(c[11])

c.extend(d)
print("c after extending with d-->")
print(c)

# c.clear()
# print(c)

e=c.copy()
print("e-->",e)

print(c.index(1))

c.insert(9, 100)
print(c)

print(c.pop(8))
print(c)

print(c.pop())
print(c)

c.remove(56)
print(c)

c.reverse()
print(c)

c.sort()
print(c)

print(c.count(100))

print(len(c))

c.remove(2)
print(c)
