class Student:
 university = 'Astana IT University' # class attribute
 def __init__(self, name, group, gpa):
    self.name = name
    self.group = group
    self.gpa = gpa
 def is_passing(self):
     return self.gpa > 2.0 # True if GPA > 2.0
 def __str__(self):
    return f'{self.name} ({self.group}) | GPA: {self.gpa}'
# Test your class
s1 = Student('Asel', 'SE-101', 3.7)
s2 = Student('Bekzat', 'SE-102', 1.5)
print(s1) # Expected: Asel (SE-101) | GPA: 3.7
print(s1.is_passing()) # Expected: True
print(s2.is_passing()) # Expected: False


    
