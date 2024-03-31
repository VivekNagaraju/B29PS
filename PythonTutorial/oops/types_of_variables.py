'''
Types of variables:
1. Instance/ object variables: values changes from object to object
2. Static/ class variable
3. method/ local variables

Note:
1. Instance variables can be declared anywhere with the help of self keyword
2. Static variables can be declared anywhere with the help of class name
'''

class Student():
    # school_name="iQuest" # static/ class variable
    def __init__(self, name, roll_no):
        self.name=name # Instance variables
        self.roll_no=roll_no
        Student.school_name="iQuest"
        
    def display_details(self):
        print(f"{self.name} has {self.roll_no} roll no from {Student.school_name}")
        
    def display_total_score(self, english, science, maths):
        self.english=english
        total=self.english+science+maths # method/ local variables
        print(f"{self.name} has scored {total}")
        
    def display_english_score(self):
        print(self.english)