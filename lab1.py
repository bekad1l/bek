#Example 1
if 5 > 2:
  print("Five is greater than two!")
#Example 2
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
#example 3
#This is a comment
print("Hello, World!")

#example 4
print("Hello, World!") #This is a comment

#example 5
#print("Hello, World!")
print("Cheers, Mate!")

#example 6
#This is a comment
#written in
#more than just one line
print("Hello, World!")

#example 7
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#example 8 - variables
x = 5
y = "John"
print(x)
print(y)

#example 9 - variables
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#example 10 - variables
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#example 11 - varibales
x = 5
y = "John"
print(type(x))
print(type(y))

#example 12 - varibales
x = "John"
# is the same as
x = 'John'

#example 13 - varibales 
a = 4
A = "Sally"
#A will not overwrite a

#example 14 - variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#example 15 - multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#example 16 - multiple values 
x = y = z = "Orange"
print(x)
print(y)
print(z)

#example 17 - multiple values
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#example 18 - output varibales 
x = "Python is awesome"
print(x)

#example 19 - output variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#example 20 - output variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#example 21
x = 5
y = 10
print(x + y)

#example 22
x = 5
y = "John"
print(x, y)

#example 23 - global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#example 24 - global varibales
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#example 25 - data types 
x = 5
print(type(x))

#example 26 - numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#example 27 - numbers 
print(type(x))
print(type(y))
print(type(z))

#example 28 - numbers
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#example 29 - numbers 
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#example 30 
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#example 31 
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#example 32 
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#example  33 - strings 
a = "Hello, World!"
print(a[1])

#example 34 - strings 
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#example 35 - strings
b = "Hello, World!"
print(b[2:5])

#example 36 - strings
b = "Hello, World!"
print(b[:5])

#example 37 - strings 
b = "Hello, World!"
print(b[2:])

#example 38 - strings 
a = "Hello, World!"
print(a.upper())

#example 39 - strings 
a = "Hello, World!"
print(a.lower())

#example 40 - strings 
a = " Hello, World! "
print(a.strip())

#example 41 - strings 
a = "Hello, World!"
print(a.replace("H", "J"))

#example 42 - strings 
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#example 43 - strings 
a = "Hello"
b = "World"
c = a + b
print(c)

#example 44 - strings 
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#example 45 - strings 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#example 46 - strings 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#example 47 - strings 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))





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











