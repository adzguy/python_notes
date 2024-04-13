"""Class TUESDAY 04/09/2024"""

'''Variables'''
# are used to store data
# Assigning values to variables
x: int = 5      # x is an integer variable
y = 3.14        # y is a floating-point variable
name = "Alice"  # name is a string variable
is_valid = True # is_valid is a boolean variable

# You can also assign multiple variables in a single line
a, b, c = 1, 2, 3

# Variables can be re-assigned with different values
x = 10
# Python is dynamically typed, so variables can hold different types of data
x = "Hello"     # Now x holds a string instead of an integer

# Variable naming conventions
# - Variable names must start with a letter (a-z, A-Z) or an underscore (_)
# - The remainder of the variable name can consist of letters, numbers, and underscores
# - Variable names are case-sensitive
# - Avoid using Python keywords as variable names (e.g., 'if', 'else', 'while', etc.)

# Examples of valid variable names
my_var = 42
myVar = "Hello"
_my_var = True
MYVAR = 3.14

# Examples of invalid variable names
# 4myvar = "invalid"   # Cannot start with a number
# my-var = 10          # Hyphens are not allowed in variable names
# my var = "error"     # Spaces are not allowed in variable names
# class = "Python"     # 'class' is a reserved keyword in Python. help("keywords")

'''Arithmetic Operations'''
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335, print(round(10/3, 2)) for 3.33
print(a // b) # Output: 3
print(a % b)  # Output: 1 remainder
print(a ** b) # Output: 1000

'''Comparison Operators'''
x = 5
y = 10
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)   # Output: False
print(x < y)   # Output: True
print(x >= y)  # Output: False
print(x <= y)  # Output: True

'''Logical Operators'''
p = True
q = False
print(p and q)  # Output: False
print(p or q)   # Output: True
print(not p)    # Output: False

'''IF/ELSE'''
# we use if when we need to decide how to proceed (conditional statement)
# Example 1: Basic if statement
x = 10
if x > 5:
    print("x is greater than 5")

# Example 2: if-else statement
y = 3
if y % 2 == 0:
    print("y is even")
else:
    print("y is odd")

# Example 3: if-elif-else statement
z = 15
if z < 10:
    print("z is less than 10")
elif z > 10:
    print("z is greater than 10")
else:
    print("z is equal to 10")

# Example: Checking if a number is between two ranges
number = 15

if number > 0 and number < 10:
    print("Number is between 0 and 10")
elif number > 20 or number < 5:
    print("Number is either greater than 20 or less than 5")
elif not (number % 2 == 0):
    print("Number is odd")
else:
    print("Number doesn't meet any condition")

# Example
day = "Monday"
if day == "Monday":
    print("Have a great week")
elif day == "Tuesday":
    print("Hand on in there")
elif day == "Wednesday":
    print("Half way through the week")
elif day == "Thusday" or day == "Friday":
    print("It's almost a weekend")
else:
    print("This is a weekend")

# Example: Determining eligibility for a discount based on age and membership status
age = 35
is_member = True

if age >= 18:
    if is_member:
        if age >= 65:
            discount = 0.3  # 30% discount for senior members
        elif age >= 30:
            discount = 0.2  # 20% discount for adult members under 65
        else:
            discount = 0.1  # 10% discount for adult members under 30
        print("Congratulations! You are eligible for a discount.")
        print(f"Your discount rate is {discount * 100}%.")
    else:
        print("Sorry, you must be a member to receive a discount.")
else:
    print("Sorry, you must be at least 18 years old to receive a discount.")


'''LIST''' 
# ordered, mutable (you can change value)
# items belong together for example you want to store names of 4 team members at work
name1 = "Jack"
name2 = "Mike"
name3 = "Kishor"
name4 = "Ben"
# better use list data type
team_members = ["Jack", "Mike", "Kishor", "Ben", "Mike"]
print(len(team_members))
print(team_members.count("Mike")) 

# slicing and indexing
team_one = team_members[:len(team_members)//2]
team_two = team_members[len(team_members)//2:]
print(f"team_one: {team_one}")
print(f"team_two: {team_two}")
team_three = ["Sarah", "Jesica"]
print(team_one + team_two + team_three) # you can not substract but add

# mutable
team_members[0] = "Sam"
print(team_members)

# loop over list
for name in team_members:
    print(f"Hello {name}. How are you doing today?")

# you can store any datatype
my_numbers = [1,2,3,4,5,6]
quiz_ans = [True, False, True, True]
useless_stuff = ["Hello", 2.3, False, "Bye"]


'''LOOPS'''
# think of a white room which represents a computer program, all actions happen in a program occur in this room
# any resources that are needed to perform action must be in this room
# several shelves
# room is not entirely empty, lowermost shelf a booklet called built-in, keywords and funcs such as if else needs to be in the room so it is in booklet
# writing DRY code, opposit is WET (Waste everyone's time/ we enjoy typing)

# meow.py
print("meow")
print("meow")
print("meow")
i = 0
while i < 3:
    print("meow")
    i = i + 1

for i in [0, 1, 2]:
    print(str(i) + " meow")

# use range()  to check builtins dir(__builtins__)
for i in range(10): # pythonic way to do it "the way to do it" in python community
    print("meow")

# forever loop when break removed
while True:
    print("meow")
    break

# Example: Multiplication table using nested loops
for i in range(1, 11):  # Outer loop for rows
    for j in range(1, 11):  # Inner loop for columns
        print(f"{i} x {j} = {i * j}")
    print()  # Add a newline after each row
