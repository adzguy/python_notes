"""Class THURSDAY 04/11/2024"""

'''Built-In DataTypes'''
answer = input("What is your name? ") # returns str
print("Hello " + answer)
is_tuesday = True   # bool
is_sunny = False    # bool
x = None            # NoneType

'''TYPE CONVERSION'''
a = 0   # int
a_as_bool = bool(a)  # a_as_bool will be False

b = 42
b_as_bool = bool(b)  # b_as_bool will be True

x = input("x: ")
x = int(x)
y = input("y: ")
y = int(y)
print(x + y)


'''Methods'''
# methods is a function that is associated with a specific
# data type and acts on that data type.
name = "Jacqueline"
print(name.upper()) # upper() is method that belong to str data type (<data_type>.<method>)


'''Exceptions'''
# it is an event that occurs during the execution of a program that distrupts the normal 
# flow of the program's instructions.
# Exception handling allows developrs to manage unexpected errors
# Exceptiong types

# Example 1: Division by zero exception
try:
    result = 10 / 0  # Division by zero will raise an exception
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Example 2: ValueError exception
try:
    num = int("abc")  # Converting a string with alphabets to an integer will raise a ValueError
except ValueError:
    print("Error: Could not convert the string to an integer.")

# Exception is a base class for all built-in exceptions
# The else block lets you execute code when there is no error.
try:
    # Code that may raise an exception
    result = x / y
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Division result:", result)

# raise an exception
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("Age is valid.")

try:
    age = int(input("Enter your age: "))
    validate_age(age)
except ValueError as e:
    print("Error:", e)

# from confluence
x = "hello"
if not isinstance(x, int):
    raise TypeError("Only integers are allowed")


'''TUPLE''' 
# ordered, immutable
# you can use indexing and slicing on tuples (parentheses)
# collection data type
my_tuple = ("apple", "orange", "banana")
my_tuple = "apple", "orange", "banana"
print(my_tuple[1])

#immutable (try to change one value)
my_tuple = ["apple", "banana", "orange"]
my_tuple[0] = "peer"

# They are also used in functions that return multiple values, 
# as you can return a tuple of values and easily unpack them when calling the function.

'''SETS''' # unordered, immutable, unindexable
my_set = {1, 2, 3, 4}
another_set = {'a', 'b', 'c', 'd'}
empty_set = set() # can't use {} because it will create dictionary

# no dubplicates one of the main feature
my_set = {1, 2, 3, 4, 4}  # Duplicate 4 will be ignored
print(my_set)  # Output: {1, 2, 3, 4}

# supports various operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1.union(set2)  # or set1 | set2

# Intersection
intersection_set = set1.intersection(set2)  # or set1 & set2

# Difference
difference_set = set1.difference(set2)  # or set1 - set2


'''DICTIONARY''' 
# ordered, keys are immutable and values are mutable, no duplicats
# collection data type stores key value pair
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# list_of_dict = [
#     {'name': 'John', 'age': 30, 'city': 'New York'},
#     {'name': 'Steph', 'age': 32, 'city': 'San Francisco'}
# ]
# keys can be of any immutable data types such as str, number, tuple

print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 30
print(my_dict.get('gender', 'Unknown'))  # Output: Unknown if 'gender' key is not present in dict

# Changing value
my_dict['age'] = 31

# Adding new key-value pair
my_dict['gender'] = 'Male'

# Removing key-value pair
del my_dict['city']

print(my_dict)

# iterate over dict using loops
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)


# improvisation example from the class demo
my_list_of_dict = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Ben', 'age': 18, 'city': 'Chicago'},
    {'name': 'Sarah', 'age': 25, 'city': 'Milan'}
]

for item in my_list_of_dict:
    email = input("What is your email? ")
    item['email'] = email
    item['phone'] = f"+1.234.567.00{item['age']}"
    for k, v in item.items():
        print(f"{k}: {v}")
    print()