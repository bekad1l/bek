#Python Syntax exercise 1
print("Hello world")

#Python Syntax exercise 2
if 5 > 2:
    print("YES")

#Python comments exercise 1
#This is a comment

#Python comments exercise 2

""""
This is a comment
written in 
more than just one line

"""

#Python Variables ex 1
carname = "Volo"
#Python Variables ex 2
x = 50
#Python Variables ex 3
x = 5
y = 10
print(x + y)
#Python Variables ex 4
x = 5
y = 10
z = x + y
print(z)
#Python Variables ex 5 
x,y,z = "Orange", "Banana", "Cherry"
#Python Variables ex 6
x = y = z = "Orange"
#Python Variables ex 7
def myfunc():
    global x
    x = "fantastic"

#Python Datatypes ex 1
x = 5
print(type(x)) #type(x) = int

#Python Datatypes ex 2
x = "Hello world"
print(type(x)) #type(x) = str

#Python Datatypes ex 3
x = 20.5
print(type(x)) #type(x) = float

#Python Datatypes ex 4
x = ["apple", "banana", "cherry"]
print(type(x)) #type(x) = list

#Python Datatypes ex 5
x = ("apple", "banana", "cherry")
print(type(x)) #type(x) = tuple

#Python Datatypes ex 6

x = {"name" : "John", "age" : 36}
print(type(x)) #type(x) = dict

#Python Datatypes ex 7
x = True
print(type(x)) #type(x) = boolean

#Python Numbers ex 1
x = 5
x = float(x) #5.0

#Python Datatypes ex 2
x = 5.5
x = int(x) #5

#Python Datatypes ex 3
x = 5
x = complex(x) #(5+0j)

#Python Strings ex1
x = "Hello World"
print(len(x))

#Python Strings ex2

txt = "Hello World"
x = txt[0] #H

#Python Strings ex3
txt = "Hello World"
x = txt[2:5] #llo

#Python Strings ex4
txt = " Hello World "
x = txt.strip() #Hello world

#Python Strings ex5
txt = "Hello World"
x = txt.upper() #HELLO WORLD

#Python Strings ex6
txt = "Hello World"
x = txt.lower() #hello world

#Python Strings ex7
txt = "Hello World"
x = txt.replace("H", "J") #Jello World

#Python Strings ex8
age = 36
txt = " My name is John, and I am {} years old"
print(txt.format(age))











