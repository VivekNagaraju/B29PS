import re
'''
1. Mobile number validation
- have 10 digits
- 1st digit should be any digit from 5-9
- remaining digits can be any digit from 0-9

RE= "[5-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
    "[5-9][0-9]{9}"
    "[5-9]\d{9}"
    
'''
number=input("Please enter a phone number:")
my_re= "[5-9]\d{9}"
match_object=re.fullmatch(my_re, number)
# print(match_object)
if match_object != None:
    print("You entered a valid phone number")
else:
    print("You entered an invalid phone number")
