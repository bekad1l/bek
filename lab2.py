#Booleans

#ex1

print(10>9) #True

#ex2
print(10==9) #False

#ex3
print(10<9) #False

#ex4
print(bool("abc")) #True

#ex5
print(bool(0)) #False

#Operators

#ex1
print(10*5) #50

#ex2
print(10/2) #5

#ex3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#ex4
if 5 != 10:
    print("5 and 10 is not equal")

#ex5
if 5 == 10 or 4==4:
    print("At least one of the statements is true")

#Lists
    
#ex1
fruits = ["apple","banana", "cherry"]
print(fruits[1])

#ex2
fruits = ["apple","banana", "cherry"]
fruits[0] = "kiwi"

#ex3
fruits = ["apple","banana", "cherry"]
fruits.append("orange")

#ex4
fruits = ["apple","banana", "cherry"]
fruits.insert(1,"lemon")

#ex5
fruits = ["apple","banana", "cherry"]
fruits.remove("banana")

#ex6
fruits = ["apple","banana", "cherry"]
print(fruits[-1])

#ex7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#ex8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))