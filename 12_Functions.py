# Functions:-

# Although we had a slight overview about functions in one of the previous modules, here we are going to deep dive about them.

# Definition:-
# Functions are block of code which can be executed when they are called by the programmer.
# Functions are used to reduce the code redundancy and make the code more readable and maintainable.

# Let us understand with a simple example:

# suppose a programmer wants to display/print "Hello World" on the console. Now to do this he calls the print() function and this function executes the code written inside it in some other module and when that code executes, the string written inside it will be printed successfully on the console.

# Types of functions (This will clarify about the working even more):
# 1. Built-in functions:-
# These are the functions which are already defined in the python language and we can use them directly without defining them. For example: print(), input(), len(), etc.

# 2. User-defined functions:-
# These are the functions which are defined by the programmer himself.

# 1. Built-in functions:-

# When we install python in our system then there are some files which contain the code necessary for the functions we use normally like the print(), input() etc. These type of functions are called Built-in function.

# 2. User-defined functions:-
# Suppose a programmer wants to print the sum of three variables, and wants to use this functionality multiple times in his code. In this case instead of writing the code of addition again and again, he sipmly creates a function to do so.

# Syntax:
# def function_name():
     # code to be executed
#    return

# Firstly we use the 'def keyword to define a function'
# function_name() is the name of the function which can be anything but it should be unique and
# should not be a keyword of python.
# The code to be executed is the code which will be executed when the function is called.
# return is the keyword which is used to return the value of the function.
# The function can be called by simply writing the function_name() in the code.
# The function can be called multiple times in the code.

# Example: Defining a function to add three variables:
def addition(a,b,c):
    print("The sum of ",a," ", b," " ,c, " is =", a+b+c)
    return 0
# Here return 0 means that the function will simply execute the code written inside it but will not provide a value, instead of print statement here we could also write it after return like this:

# def addition(a,b,c):
#     return print("The sum of ",a," ", b," " ,c, " is =", a+b+c)

# Calling the function:
addition(1,2,3)
addition(4,5,6)
addition(7,8,9)
addition(10,11,12)
addition(13,14,15) #You may call it anywhere now and as many times as you like