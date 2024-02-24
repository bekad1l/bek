#Pythondate

#ex1

from datetime import datetime, timedelta

today = datetime.now()

fivedaysago = today - timedelta(days = 5)

print("Today is:", today.strftime("%Y-%m-%d"))
print("5 days ago:", fivedaysago.strftime("%Y-%m-%d"))

#ex2

from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)

tomorrow = today + timedelta(days=1)

print("Today:", today.strftime("%Y-%m-%d"))
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d") )

#ex3

from datetime import datetime

x = datetime.now()
dropped = x.replace(microsecond=0)

print("With microsecond", x)
print("Without microsecond", dropped)

#ex4

from datetime import datetime


date1 = input()
date2 = input()

dateformat = "%Y-%m-%d %H:%M:%S"
date1 = datetime.strptime(date1, dateformat)
date2 = datetime.strptime(date2, dateformat)

diff = abs((date2 - date1).total_seconds())

print("Difference:", diff)

#python math

#ex1

import math

def radian(deg):
    return deg * (math.pi / 180)

degree = float(input())
radian = radian(degree)
print("radian:", radian)

#ex2

import math
def area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

base1 = float(input())
base2 = float(input())
height = float(input())

areatrap = area(base1, base2, height)

print(areatrap)

#ex3

import math

def areapoly(n, s):
    return (n * s ** 2) / (4 * math.tan(math.pi / n))

number = int(input())
length = float(input())

area = areapoly(number, length)
print(area)

#ex4

def areapal(base, height):
    return base * height

length = float(input())
height = float(input())

area = areapal(length, height)
print( area)

#python iterators
#ex1

def gensquares(N):
    for i in range(1, N + 1):
        yield i ** 2

N = int(input())

squares = gensquares(N)

print(f"Squares till to {N}:", end = " ")
for square in squares:
    print(square, end = " ")

#ex2
    def evennumbers(n):
        for i in range(n + 1):
            if i % 2 == 0:
                yield i

def main():
    n = int(input())

    even_numbers = evennumbers(n)
    print("Even numbers between 0 and", n, ":", end=" ")
    for num in even_numbers:
        print(num, end=", " if num < n else "\n")

if __name__ == "__main__":
    main()

#ex3
    def divisible_by_3_and_4(n):
        for i in range(n + 1):
            if i % 3 == 0 and i % 4 == 0:
                yield i

def main():
    n = int(input())
    numbers = divisible_by_3_and_4(n)
    print("Numbers divisible by both 3 and 4 between 0 and", n, ":")
    for num in numbers:
        print(num, end=" ")

if __name__ == "__main__":
    main()

#ex4
    def squares(a, b):
     for i in range(a, b + 1):
        yield i ** 2


a = int(input())
b = int(input())

print("Squared values from", a, "to", b, ":")
for square in squares(a, b):
    print(square)

#ex5
    def countdown(n):
        while n >= 0:
            yield n
        n -= 1

n = int(input())

print("Countdown from", n, "to 0:")
for num in countdown(n):
    print(num)

#jsons
import json

# temp_file = json.dumps(sample-data.json)
with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface status")
print("=" * 80)
print("DN", " " * 40, "Description ", "speed", " " * 10, "MTU")
print("-" * 41, "-" * 12, "-" * 13, "\t", "-" * 4)
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]:
            print(imdata[i][j]["dn"],"\t", "\t"  , imdata[i][j]["speed"] ,"\t" , imdata[i][j]["mtu"])



    




