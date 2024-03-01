#1 task
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

# Test
numbers = [1, 2, 3, 4, 5]
print("Product of all numbers:", multiply_list(numbers))

#2 task
def count_upper_lower_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

# Test
text = "Hello World"
upper, lower = count_upper_lower_case(text)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)

#3task
def is_palindrome(string):
    return string == string[::-1]

# Test
word = "radar"
if is_palindrome(word):
    print("The word '{}' is a palindrome.".format(word))
else:
    print("The word '{}' is not a palindrome.".format(word))


#4task
    
import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

# Test
number = 25100
milliseconds = 2123
result = square_root_after_milliseconds(number, milliseconds)
print("Square root of {} after {} milliseconds is {}".format(number, milliseconds, result))

#5task
def all_elements_true(tup):
    return all(tup)

# Test
tuple1 = (True, True, False)
tuple2 = (True, True, True)
print("All elements of tuple1 are True:", all_elements_true(tuple1))
print("All elements of tuple2 are True:", all_elements_true(tuple2))


#Python directions and files
import os
import string

# Task 1: List only directories, files, and all directories, files in a specified path
def list_directories_and_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

    print("\nAll Directories and Files:")
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))
        for file in files:
            print(os.path.join(root, file))

# Task 2: Check for access to a specified path
def check_path_access(path):
    print("Existence:", os.path.exists(path))
    print("Readability:", os.access(path, os.R_OK))
    print("Writability:", os.access(path, os.W_OK))
    print("Executability:", os.access(path, os.X_OK))

# Task 3: Test whether a given path exists or not. If the path exists, find the filename and directory portion of the given path
def path_information(path):
    if os.path.exists(path):
        print("Path exists")
        print("Filename:", os.path.basename(path))
        print("Directory portion:", os.path.dirname(path))
    else:
        print("Path does not exist")

# Task 4: Count the number of lines in a text file
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

# Task 5: Write a list to a file
def write_list_to_file(filename, input_list):
    with open(filename, 'w') as file:
        for item in input_list:
            file.write("%s\n" % item)

# Task 6: Generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is file {letter}.txt")

# Task 7: Copy the contents of a file to another file
def copy_file(source, destination):
    with open(source, 'r') as file1, open(destination, 'w') as file2:
        file2.write(file1.read())

# Task 8: Delete a file by a specified path. Before deleting, check for access and whether the given path exists or not
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully")
        else:
            print("No write access to the file")
    else:
        print("File does not exist")

# Test each task

# Task 1
path = "."  # specify your path here
print("Task 1:")
list_directories_and_files(path)
print()

# Task 2
print("Task 2:")
check_path_access(path)
print()

# Task 3
print("Task 3:")
path_information(path)
print()

# Task 4
print("Task 4:")
filename = "example.txt"  # specify your filename here
print("Number of lines:", count_lines(filename))
print()

# Task 5
print("Task 5:")
filename = "output.txt"  # specify your filename here
my_list = ["apple", "banana", "cherry"]
write_list_to_file(filename, my_list)
print()

# Task 6
print("Task 6:")
generate_files()
print()

# Task 7
print("Task 7:")
source_file = "source.txt"  # specify your source filename here
destination_file = "destination.txt"  # specify your destination filename here
copy_file(source_file, destination_file)
print()

# Task 8
print("Task 8:")
file_to_delete = "file_to_delete.txt"  # specify your filename here
delete_file(file_to_delete)
print()

