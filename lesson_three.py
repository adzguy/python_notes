"""Class TUESDAY 04/16/2024"""

'''FUNCTIONS'''
# check confluens examples

# lets create our own function
# programs summed up with four key principles (STORE, REPEAT(loops), DECIDE(if/else statements), REUSE())
# the way to reuse code wherever you need it is to use functions. Functions indicate actions thus often named using verbs.
# for example: calculate_totel(), validate_input(), print_result(), or sort_list()

list_of_names = ['Amelia', 'Olivia', 'Emily', 'Alexey', 'Poppy', 'Ava', 'Isabella', 'Jessica', 'Marcus', 'Lily', 'Sophie', 'Grace', 'Vsevolod', 'Sophia', 'Mia', 'Evie', 'Ruby', 'Celim', 'Sumir', 'Ella', 'Scarlett', 'Ruben', 'Isabelle', 'Chloe', 'Cherlin', 'Sienna', 'Masha', 'Freya', 'Phoebe', 'Charlotte', 'Daisy', 'Alice', 'Florence', 'Eva', 'Sofia', 'Millie', 'Lucy', 'Evelyn', 'Elsie', 'Rosie', 'Imogen', 'Lola', 'Matilda', 'Elizabeth', 'Layla', 'Alasdair','Holly', 'Lilly', 'Molly', 'Erin', 'Ellie', 'Maisie', 'Maya', 'Abigail', 'Eliza', 'Georgia', 'Jasmine', 'Esme', 'Willow', 'Leanne', 'Bella', 'Annabelle', 'Keemiya', 'Ivy', 'Amber', 'Emilia', 'Emma', 'Summer', 'Hannah', 'Eleanor', 'Harriet', 'Rose', 'Amelie', 'Lexi', 'Megan', 'Gracie', 'Zara', 'Nuha', 'John', 'Lacey', 'Martha', 'Anna', 'Violet', 'Darcey', 'Maria', 'Maryam', 'Brooke', 'Aisha', 'Katie', 'Leah', 'Heinrich', 'Nour', 'Thea', 'Darcie', 'Hollie', 'Amy', 'Alexandra', 'Stephen', 'Jonathan', 'Penny', 'Mollie', 'Heidi', 'Lottie', 'Bethany', 'Francesca', 'Faith', 'Harper', 'Nancy', 'Beatrice', 'Isabel', 'Juliette', 'Darcy', 'Lydia', 'Sarah', 'Sara', 'Julia', 'Victoria', 'Zoe', 'Robyn', 'Oliver', 'Jack', 'Harry', 'Jacob', 'Charlie', 'Thomas', 'Annabel', 'George', 'Oscar', 'James', 'Ian', 'William', 'Noah', 'Alfie', 'Joshua', 'Yuvraj', 'Muhammad', 'Leo', 'Archie', 'Ethan', 'Joseph', 'Arushi', 'Freddie', 'Samuel', 'Alexander', 'Logan', 'Daniel', 'Isaac', 'Max', 'Mohammed', 'Benjamin', 'Hugo', 'Mason', 'Lucas', 'Edward', 'Harrison', 'Jake', 'Neil', 'Dylan', 'Asher', 'Riley', 'Akash', 'Finley', 'Catherine', 'Theo', 'Muktarsi', 'Sebastian', 'Adam', 'Zachary', 'Arthur', 'Thomas', 'Alberto', 'Toby', 'Jayden', 'Luke', 'Harley', 'Lewis', 'Tyler', 'Harvey', 'Anusha', 'Matthew', 'David', 'Reuben', 'Alok', 'Michael', 'Elijah', 'Kian', 'Tom', 'Mohammad', 'Blake', 'Jean', 'Luca', 'Theodore', 'Stanley', 'Derin', 'Jenson', 'Nathan', 'Nicholas', 'Charles', 'Frankie', 'Constantin', 'Jude', 'Teddy', 'Eric', 'Viren', 'Louie', 'Louis', 'Ryan', 'Hugo', 'Bobby', 'Niamh', 'Anya', 'Elliott', 'Dexter', 'Khai', 'Hariesh', 'Henry', 'Ollie', 'Aron', 'Alex', 'Liam', 'Kai', 'Gabriel', 'Connor', 'Aaron', 'Afrah', 'Frederick', 'Callum', 'Lorcan', 'Elliot', 'Albert', 'Leon', 'Ronnie', 'Rory', 'Jamie', 'Austin', 'Seth', 'Ibrahim', 'Mei', 'Owen', 'Caleb', 'Yousuf', 'Ellis', 'Sonny', 'Devyn', 'Robert', 'Joey', 'Felix', 'Finlay', 'Rossa', 'Ekraj', 'Jackson', 'Jimi', 'Meera', 'Rafi', 'Salahdeen', 'Guido', 'Tanya', 'Karlis']
result = []
for name in list_of_names:
    if name[0] == "P":
        result.append(name)
print(result)

# what if i have a function called find_names_starting_with that would give me the list of names starts with P
# functions are self-contained mini-program that can be called by main program or another function or another program

def find_names_starting_with(letter, names):
    result = []
    for name in names:
        if name[0] == letter:
            result.append(name)
    return result

names_p = find_names_starting_with(letter="P", names=list_of_names)
names_a = find_names_starting_with(letter="L", names=list_of_names)
print(names_p)
print(names_a)

# find names by length
def find_names_of_length(length, names):
    result = []
    for name in names:
        if len(name) == length:
            result.append(name)
    return result

names_l3 = find_names_of_length(length=3, names=list_of_names)
print(names_l3)

# homework
# What if you want to find all names that start with E and are six letters long? create a new function (pay attention to the names of the function)
# find_names_starting_with_and_of_length(letter, length, list_of_names)

# default argument
def greet(name='World'):
    print("Hello, " + name + "!")

# Example usage
greet("Alice")  # Prints: Hello, Alice!
greet()         # Prints: Hello, World!

# *args is a special parameter that allows a function to accept an arbitrary number of positional arguments
def my_function(*args):
    print("Number of arguments:", len(args))
    print("Arguments:", args)

my_function(1, 2, 3)
my_function('a', 'b', 'c', 'd', 'e')
my_function(True, False)

def calculate_total(*args):
    total = 0
    for price in args:
        total += price
    return total

# Example usage
total_price = calculate_total(10.99, 5.99, 7.49, 3.25)
print("Total price:", total_price)

# allows the function to accept any number of keyword arguments, 
# and these arguments are collected into a dictionary within the function.
def my_function(**kwargs):
    print("Number of keyword arguments:", len(kwargs))
    print("Keyword arguments:", kwargs)

my_function(a=1, b=2, c=3)
my_function(name='Alice', age=30, city='New York')
my_function(x=10, y=20, z=30, foo='bar')

def create_person(**kwargs):
    person = {}
    for key, value in kwargs.items():
        person[key] = value
    return person

# Example usage
person1 = create_person(name='Alice', age=25, city='London')
person2 = create_person(name='Bob', age=30, city='New York', occupation='Engineer')

print(person1)
print(person2)

'''Recursion'''
# Recursion is a programming technique where a function calls itself in order to solve a problem (loop)
# factorial (multiply of integers from n down to 1)
def factorial(n):
    # Base case: if n is 0 or 1, return 1  ## 0! = 1 in math
    if n == 0 or n == 1:
        return 1
    # Recursive case: multiply n by the factorial of (n-1)
    else:
        return n * factorial(n-1)
    
# factorial(5) calls factorial(4)
# factorial(4) calls factorial(3)
# factorial(3) calls factorial(2)
# factorial(2) calls factorial(1)
# factorial(1) returns 1 (base case)
# factorial(2) returns 2 * 1 = 2
# factorial(3) returns 3 * 2 = 6
# factorial(4) returns 4 * 6 = 24
# factorial(5) returns 5 * 24 = 120

# Example usage
print(factorial(5))  # Output: 120


# Example usage
result = factorial(5)
print("Factorial of 5 is:", result)  # Output: 120

# Example tri_recursion (sum of integers from k down to 1)
def tri_recursion(k):
    if k == 0:
        return 0
    else:
        return k + tri_recursion(k-1)
result = tri_recursion(6)
print(result)

# tri_recursion(6) calls tri_recursion(5) or you can say: tri_recursion(6) = 6 + tri_recursion(5)
# tri_recursion(5) calls tri_recursion(4)
# tri_recursion(4) calls tri_recursion(3)
# tri_recursion(3) calls tri_recursion(2)
# tri_recursion(2) calls tri_recursion(1)
# tri_recursion(1) calls tri_recursion(0)
# tri_recursion(0) returns 0 (from base case)
# tri_recursion(1) returns 1 + 0 = 1
# tri_recursion(2) returns 2 + 1 = 3
# tri_recursion(3) returns 3 + 3 = 6
# tri_recursion(4) returns 4 + 6 = 10
# tri_recursion(5) returns 5 + 10 = 15
# tri_recursion(6) returns 6 + 15 = 21 (final result after chainning calls)

# below tri_recursion does not have base case to stop the recursion
# you get "maximum recursion depth exceeded" error 
def tri_recursion(k):
    return k + tri_recursion(k-1)


'''MODULES'''
'''In Python, a module is a file containing Python code. The code can be functions, classes, 
or variables that you can use in your Python program. Modules allow you to organize your 
Python code into reusable units, making your code more modular and easier to manage.'''

# create module named mymodule.py (usually modules contain related functions, classes or variables)
def greet(name):
    print("Hello, " + name)

def add(x, y):
    return x + y

# Variables
PI = 3.14159

# create python file then import mymodule
# import mymodule

# mymodule.greet("Alice")
# print(mymodule.add(5, 3))
# print(mymodule.PI)

# you can also import specific functions or variables from modules
# from mymodule import greet, add, PI

# greet("Bob")
# print(add(7, 2))
# print(PI)

'''Python Standard Library'''
'''is a collection of modules and packages that are included with every Python installation. 
These modules provide a wide range of functionalities, including working with files, 
interacting with the operating system, handling data structures, performing mathematical operations, 
implementing networking protocols, and much more.'''

# builtins is a module that you don't need to import
import math

print(math.sqrt(25))  # Using the sqrt function from the math module
print(help(math))   # to see inside the math module
print(dir(math))

# or 
from math import sqrt

print(sqrt(25))  # No need to prefix with "math."

# Example
import sys

# Print the command-line arguments
print("Command-line arguments:", sys.argv[1:])


'''PACKAGING'''
'''Packaging refers to the process of bundling Python code, 
along with related resources and metadata, into a distributable
format that can be shared and installed by others.
Packages are directories containing one or more Python modules, 
along with additional files such as READMEs, license files, and data files. 
They also include a special __init__.py file to indicate that the directory should be treated as a package.
Packages often include a setup.py file, which is a Python script that contains information 
about the package and instructions for installing it using tools like pip.
Packaging is essential for sharing libraries and applications with others, 
whether through distribution on platforms like PyPI (Python Package Index) or 
distribution within an organization.'''

'''pip'''
# is the standard package manager used for installing and manading software packages 
# written in Python

# pip install <package>: Installs a Python package.
# pip install -r requirements.txt: Installs all the packages listed in a requirements.txt file.
# pip uninstall <package>: Uninstalls a Python package.
# pip list: Lists all installed Python packages.
# pip freeze >> requirements.txt: generates a requirements.txt file containing a list of 
    # all the Python packages installed in your current environment along their versions.

# Example 1: create moo.py file
# pip install cowsay
# import cowsay
# cowsay.cow("This is scripting lesson 13")

name = input("what is your name? ")
# cowsay.cow(f"hello, {name}")

# Example 2: create qr.py file
# pip install qrcode
# import qrcode # type: ignore

# img = qrcode.make("https://www.tntk.io") ## try with different urls

# img.save("images/tntk.png")

# Example 3: create blur.py
# pip install pillow (you need pillow )
from PIL import Image, ImageFilter # type: ignore

before = Image.open("images/stock-photo.jpg")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("images/blur.jpg")


'''Some other modules/packages'''
## requests
# import requests

# # Define the GitHub API endpoint for fetching information about a user
# github_api_url = 'https://api.github.com/users/'

# # Input the GitHub username you want to fetch information about
# username = input("Enter GitHub username: ")

# # Construct the URL for the user's profile
# user_profile_url = github_api_url + username

# # Make a GET request to the user's profile URL
# response = requests.get(user_profile_url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     # Parse the JSON response
#     user_data = response.json()
#     print(user_data)
#     # Extract relevant information
#     name = user_data.get('name', 'N/A')
#     followers = user_data.get('followers', 'N/A')
#     public_repos = user_data.get('public_repos', 'N/A')
#     bio = user_data.get('bio', 'No bio provided')
    
#     # Print the information
#     print(f"Name: {name}")
#     print(f"Followers: {followers}")
#     print(f"Public Repositories: {public_repos}")
#     print(f"Bio: {bio}")
# else:
#     # Print an error message if the request failed
#     print(f'Error: {response.status_code}')


# os
import os

print(os.environ)

for key in os.environ:
    print(f'The key is {key} and the value is {os.environ[key]}')

print(os.uname()) # returns info about the current os