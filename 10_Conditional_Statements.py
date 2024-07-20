# Conditional statements :-

# Conditional statements are some specific statements which are used to control the flow of the program. They allow our program to choose between multiple options.
# Conditional statements are also known as decision making statements.
# There are three types of conditional statements in Python:-
# 1. if statement
# 2. if-else statement
# 3. elif statement


# if statement :-
a = 10
if a > 5 :
    print("a is greater than 5")

# Here '>' is a comparison operator which is comparing if a is greater than 5 or not
# Similarily, 
# '<' is used to compare if one value is less than the other
# '==' is used to compare if two values are equal or not
# '!=' is used to compare if two values are not equal
# '>=' is used to compare if one value is greater than or equal to the other
# '<=' is used to compare if one value is less than or equal to the other

# if statement is used to check if a condition is true or not. If the condition is true then the block of code is executed. If the condition is false then the block of code is not executed.

# Note: It is important to give a 3 line space in the next line after the colon(:) so that it can consider it a block of code, otherwise it might throw an error. This spcing is also Known as indentation

if a > 11 :
    print("a is greater than 11")
# Note: This print statement will not be executed as a > 11 is not true


# if-else statement :-
age = 10

if age >= 18 :
    print("You are allowed to drive")
else :
    print("You are not allowed to drive")
# Here, if a is greater than 5 then the first print statement will be executed, otherwise the second print statement will be executed.
# Note: The else statement is optional. It is not compulsory to use it
# Note: The else statement is executed only if the condition is false


# elif statements:

# elif is used to check multiple conditions. It is used to check if the first condition is false then it checks the second condition and so on.
# Note: elif is short for else if
# If a condition turns out to be true then it executes the respective block of code and does not check the rest of the condition

if age > 18:
    print("You are allowed to drive")
elif age == 18:
    print("You are allowed to drive")
else:
    print("You are not allowed to drive")

# Let's make this age checking program a little more dynamic : 

age = int(input("Enter your age : "))
# Note: python is a case sensitive language(meaning 'Age' and 'age' are two different variables)
# Note: int() is used to convert the input into an integer

if age > 18:
    print("You are definately allowed to drive.")
elif age == 18:
    print("Congratulations for your 18th birthday this year. Now you are allowed to drive.")
else:
    print("You are still too young to drive. Ask your parents to drop you.")