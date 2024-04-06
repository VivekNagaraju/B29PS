'''
Regular expressions (RegEx): RegEx is used for validating input
 
'''
import re 

a="VV 897 Vivek"
b="gcagsj@gmail.com"
c="Vivek"
print(re.subn("\d", "*", a, 7))
print(re.split("\s", a, 3))
print(re.findall("\s", a))

print(re.search("Vivek", a))
