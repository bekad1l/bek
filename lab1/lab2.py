import math
#examples

#boolen values
 
#1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3
print(bool("Hello"))
print(bool(15))

#4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#8
def myFunction() :
  return True

print(myFunction())

#9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#10
x = 200
print(isinstance(x, int))


#operators

#1
print(10+5)

#2
print((6 + 3) - (6 + 3))

#3
print(100 + 5 * 3)

#4
print(5 + 4 - 7 + 3)

#lists
#1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#5
list1 = ["abc", 34, True, 40, "male"]

#6
thislist = list(("apple", "banana", "cherry")) 

#7
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#8
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#9
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#11
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#12
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#13
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#14
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#15
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#16
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#17
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#18
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#19
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#tuple
#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#2
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#set
#1
thisset = {"apple", "banana", "cherry"}
print(thisset)

#2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#dictionaries
#1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#2
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#3
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#4
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#conditions
#1
a = 33
b = 200
if b > a:
  print("b is greater than a")

#whileloops
#1
i = 1
while i < 6:
  print(i)
  i += 1

#2
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#for loops
#1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2
for x in "banana":
  print(x)

#3
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#EXERCISES
#booleans
#1
print(10 > 9) #true

#2
print(10 == 9) #False

#3
print(10 < 9) #False

#4
print(bool("abc")) #True

#5
print(bool(0)) #False


#operators
#1
print(10*5) #50

#2
print(10/2) #5.0

#3
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#4
if 5 != 10:
  print("5 and 10 is not equal")

#5
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

#lists
#1
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

#5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#7

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#8

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#tuples
#1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#2

fruits = ("apple", "banana", "cherry")
print(len(fruits))

#3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#ex4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#sets
#ex1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#ex2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#ex3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#ex4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#ex5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#dictionaries
#ex1
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#ex2
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
#ex3
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
#ex4
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
#ex5
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#condition
#ex1
a = 50
b = 10
if a > b:
  print("Hello World")
#ex2
a = 50
b = 10
if a != b:
  print("Hello World")
#ex3
a = 50
b = 10
if a == b:
  print("YES")
else:
  print("NO") 
#ex4
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")
#ex5
a = 50
b = 10
c = 50
d = 10
if a == b and c == d:
  print("Hello")
#ex6
a = 50
b = 10
c = 50
d = 10
if a == b or c == d:
  print("Hello") 
#ex7
if 5 > 2:
  print("YES")
#ex8
a = 2
b = 5
print("YES") if a == b else print("NO")
#ex9
a = 2
b = 50
c = 2
if a == c or b == c:
  print("YES")

#while loops
#ex1
i = 1
while i < 6:
  print(i)
  i += 1
#ex2 
i = 1
while i < 6:
  if i == 3:
    break 
  i += 1 
#ex3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
#ex4
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#forloops
#ex1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#ex2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)  
#ex3
for x in range(6):
  print(x)
#ex4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)












  












