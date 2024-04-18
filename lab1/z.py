class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


import re
#11
pattern = r'^[A-Z]{6}[0-9]$'


strings = {"K2","BARCELONA111","ABCDEF1","Aqwertu9" }


for string in strings:
    if re.match(pattern, string):
        print("yes")
    else:
        print("no")

        
