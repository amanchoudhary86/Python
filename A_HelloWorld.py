#This is a comment and it is the non-executionable part of the code which is used to mention whatever the programmer wants to. Ex: Reference, notes, warnings, etc.


# To diplay output on the console:
print("Hello World")
# OR
print('''Hello World''')
# OR
print('Hello World')
# All of these are valid

# More than one strings or different values can be printed with the help of a comma ',' :
print("Python", "is", "Awesome")

# To terminate a string(to simply change the line in the output, to be specific):

# 1) Using \n :
print("Hello\nWorld")
# Note : '\n' is also newline character

# 2) Using just another print statement:
print("Hello3")
print("World3")

# To take an input on the console:
input("Exter your value here : ")

# Variables: Variables are containers which contain some value. This value can be on many types and will be discussed further.

# Rules to define a variable:
# 1. Variable name should start with a letter or an underscore.
# 2. Variable name can contain only letters, numbers, and underscores.
# 3. Variable name should not contain any special characters.
# 4. Variable name should not contain any space.
# 5. Variable name should not be a keyword.

# Each variable will be studied in the further modules(files) with examples and direct executable steps

# Creating a variable which takes input and then displays it to the console:
VariableName = input("Input your number here : ")
# You may use any other name instead of 'VariableName' if you wish
print("Your number is : ", VariableName)

# id():-
# id() function returns the “identity" of the object, which is an integer that is guaranteed
# to be unique and constant for the object during its lifetime.
# It is used to check whether the two variables point to the same object in memory or not.
print(id(10))
print(id(10.5))
print(id("Hello"))

# Note: If you did not understand the above mentioned three points just know that id() simply provides the memory address of wht is inside it.