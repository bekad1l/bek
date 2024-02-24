#TSIS 1
#task 1
class StringDet():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = StringDet()
str1.get_String()
str1.print_String()

#task 2
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(int(input()))
print (aSquare.area())

#task3
class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width

rect = Rectangle(2,4)
print(rect.area())

#task4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance

# Example usage:
point1 = Point(1, 2)
point2 = Point(3, 4)

point1.show()
point2.show()

distance = point1.dist(point2)
print(f"Distance between the two points: {distance}")

point1.move(5, 6)
point1.show()

#task5
class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')
# 1. Instantiate the class
acct1 = Account('Jose',100)
# 2. Print the object
print(acct1)


# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

#task6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Use filter with a lambda function to filter prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)

#TSIS2
#task10
def unique_elements(input_list):
    
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(original_list)
print("Original List:", original_list)
print("List with Unique Elements:", result)

#task11
def is_palindrome(word):
    
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_word = ''.join(word.lower().split())

    # Check if the cleaned word is the same when reversed
    return cleaned_word == cleaned_word[::-1]

# Example usage:
user_input = input("Enter a word or phrase: ")
result = is_palindrome(user_input)

if result:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")

#1to5
#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Example usage:
grams_amount = 100
ounces_amount = grams_to_ounces(grams_amount)
print(f"{grams_amount} grams is equal to {ounces_amount:.2f} ounces.")


#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Считываем температуру в градусах Фаренгейта из ввода пользователя
fahrenheit_temperature = float(input("Введите температуру в градусах Фаренгейта: "))

# Преобразуем температуру из градусов Фаренгейта в градусы Цельсия, используя функцию
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

# Выводим эквивалентную температуру в градусах Цельсия
print(f"{fahrenheit_temperature} градусов Фаренгейта равно {celsius_temperature:.2f} градусам Цельсия.")


#3
def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if(heads>=legs):
        print(error_msg)
    elif(legs%2!=0):
        print(error_msg)
    else:
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))
solve(35,94)


#4
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage:
numbers_list = input("Enter a list of numbers separated by spaces: ").split()
numbers_list = [int(num) for num in numbers_list]

prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)


#5
from itertools import permutations

def print_permutations(input_string):
    
    permuted_strings = [''.join(p) for p in permutations(input_string)]
    
    print("All permutations of the string:")
    for permuted_string in permuted_strings:
        print(permuted_string)

# Example usage:
user_input = input("Enter a string: ")
print_permutations(user_input)

#6task
def reverse_words(input_string):
    words = input_string.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example usage:
user_input = input("Enter a sentence: ")
result = reverse_words(user_input)
print("Sentence with reversed words:", result)

#7task
def has_adjacent_threes(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Example usage:
result1 = has_adjacent_threes([1, 2, 3, 3, 4])  # True
result2 = has_adjacent_threes([1, 2, 3, 4, 5])  # False
result3 = has_adjacent_threes([3, 3, 5, 6])  # True

print(result1)
print(result2)
print(result3)

#8task
def spy_game(nums):
    
    for i in range(0, len(nums)):
        if nums[i] == 0:
            for x in range(i + 1, len(nums)):
                if nums[x] == 0:
                    for y in range(x + 1, len(nums)):
                        if nums[y] == 7:
                            return True
    return False

# Example usage:
result1 = spy_game([1, 2, 4, 0, 0, 7, 5])  # True
result2 = spy_game([1, 0, 2, 4, 0, 5, 7])  # True
result3 = spy_game([1, 7, 2, 0, 4, 5, 0])  # False

print(result1)
print(result2)
print(result3)

#9task
import math

def sphere_volume(radius):
    volume = (4 / 3) * math.pi * radius**3
    return volume

# Example usage:
radius = float(input("Enter the radius of the sphere: "))
result = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is: {result:.2f}")

#hystogram
def histogram(items):
    for n in items:
        output = ''  
        times = n     
        
        
        while times > 0:
            output += '*'
            times = times - 1 
        
        
        print(output)

histogram([2, 8, 1, 10])

#lasttask
#code который определяет функцию для вычисления площади прямоугольника
def calculate_rectangle_area(length, width):   
    area = length * width
    return area

# Example usage:
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_rectangle_area(length, width)
print("The area of the rectangle is:", area)

#lasttask#2

import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')  
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') 

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)

