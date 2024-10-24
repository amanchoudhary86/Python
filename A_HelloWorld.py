#This is a comment and it is the non-executionable part of the code which is used to mention whatever the programmer wants to. Ex: Reference, notes, warnings, etc.


'''This is a called a doc-string (also known as documentation string)
and it is used just for the documentation purpose. In simple terms it could be understood as the comments which are primarily for study purpore. 
'''

'''Note: Comments are primarily used by the programmers in the development phase or so. Also neither comments nor doc-strings affect the functionality of our program.'''

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
# Note : '\n' is also known as newline character

# 2) Using just another print statement:
print("Hello3")
print("World3")

# To take an input on the console:
input("Exter your value here : ")

'''Variables: Variables are containers which contain some value. This value can be on many types and will be discussed further.

Rules to define a variable:
1. Variable name should start with a letter or an underscore.
2. Variable name can contain only letters, numbers, and underscores.
3. Variable name should not contain any special characters.
4. Variable name should not contain any space.
5. Variable name should not be a keyword.

Each variable will be studied in the further modules(files) with examples and direct executable steps

Creating a variable which takes input and then displays it to the console:'''
VariableName = input("Input your number here : ")
# You may use any other name instead of 'VariableName' if you wish
print("Your number is : ", VariableName)