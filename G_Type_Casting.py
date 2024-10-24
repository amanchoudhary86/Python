<<<<<<< HEAD
'''Type Casting:-

Type casting is the process of converting one data type into another.
It is also known as type conversion.
For example: int to float
=======
""" Type Casting:-

Type casting is the process of converting one data type into another.
It is also known as type conversion.
>>>>>>> aae58a77690af619f6a05aa14965c9a4afc7306e

There are two types of type casting:
1. Implicit Type Casting (Automatic conversion by Python)
2. Explicit Type Casting (Manual conversion by the programmer)

Implicit Type Casting
Python automatically converts a smaller data type to a larger data type
<<<<<<< HEAD
to prevent data loss.
'''
=======
to prevent data loss."""
>>>>>>> aae58a77690af619f6a05aa14965c9a4afc7306e

# Example of implicit type casting:
a = 10  # 'a' is an integer
b = 3.5  # 'b' is a float

# When we add an integer and a float, Python implicitly converts 'a' to float
result = a + b
print("Implicit Type Casting Result:", result)
print("Type of result after implicit casting:", type(result))  # Output: <class 'float'>

print()  # Just for better readability in the output

# Explicit Type Casting
# We manually convert one data type to another using Python's built-in functions.

# Before Explicit Type Casting:
c = 20  # 'c' is an integer
print("Before Type Casting:", type(c))  # Output: <class 'int'>

# After Explicit Type Casting to String:
c = str(c)
print("After Type Casting to String:", type(c))  # Output: <class 'str'>

print()  # just for better readability in the output

<<<<<<< HEAD
'''
Common functions for explicit type casting:
- int(): Converts a value to an integer
- float(): Converts a value to a float
- str(): Converts a value to a string
- list(): Converts a value to a list
- tuple(): Converts a value to a tuple
- set(): Converts a value to a set
- dict(): Converts a sequence of key-value pairs to a dictionary
'''
=======
""" Common functions for explicit type casting:
 - int(): Converts a value to an integer
 - float(): Converts a value to a float
 - str(): Converts a value to a string
 - list(): Converts a value to a list
 - tuple(): Converts a value to a tuple
 - set(): Converts a value to a set
 - dict(): Converts a sequence of key-value pairs to a dictionary"""
>>>>>>> aae58a77690af619f6a05aa14965c9a4afc7306e

# Example of converting string to integer
d = "42"
d = int(d)
print("After Converting String to Integer:", type(d))  # Output: <class 'int'>

# Example of converting list to tuple
e = [1, 2, 3]
e = tuple(e)
print("After Converting List to Tuple:", type(e))  # Output: <class 'tuple'>

print()  # Just for better readability in the output

# Potential Issues with Type Casting:
# 1. Loss of Data: Converting from float to int can lead to loss of the decimal part.
f = 3.99
g = int(f)  # The decimal part is removed
print("After Converting Float to Integer:", g)  # Output: 3

<<<<<<< HEAD
'''
2. Conversion Errors: Incompatible types can raise ValueError.
If we try to convert a string containing alphanumeric("123abc") or alphabetic("abc") characters to integer or float or to a numeric type, then it raises an error 

Use Cases for Type Casting:
- Reading data from files or user input, which is often in string format.
- Performing mathematical operations where type precision matters.
- Interfacing with APIs or libraries that require specific data types.

Summary:
- Implicit casting is done by Python automatically, whereas explicit casting is done manually.
- Use explicit casting to ensure your data is in the correct format for operations.

type function:
The type() function returns the type of the object passed to it.
It can be used to check the type of a variable or an object.
It can also be used to get the type of a variable or an object.
'''
=======
"""2. Conversion Errors: Incompatible types can raise ValueError.
 If we try to convert a string containing alphanumeric("123abc") or alphabetic("abc") characters to integer or float or to a numeric type, then it raises an error 

 Use Cases for Type Casting:
 - Reading data from files or user input, which is often in string format.
 - Performing mathematical operations where type precision matters.
 - Interfacing with APIs or libraries that require specific data types.

 Summary:
 - Implicit casting is done by Python automatically, whereas explicit casting is done manually.
 - Use explicit casting to ensure your data is in the correct format for operations.
>>>>>>> aae58a77690af619f6a05aa14965c9a4afc7306e

 type function:
 The type() function returns the type of the object passed to it.
 It can be used to check the type of a variable or an object.
 It can also be used to get the type of a variable or an object.
"""
# Example:
type(5)  # Output: <class 'int'>
type(3.14)  # Output: <class 'float'>
type("Hello")  # Output: <class 'str'>

# OR

print(type(5))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>
print(type("Hello"))  # Output: <class 'str'>
