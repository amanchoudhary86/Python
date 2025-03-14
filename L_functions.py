'''Functions:-

Note : From now on we will be using Functions as a part of a normal code. So make sure to understand this module properly, in case a doubt occurs it is recommended to watch a youTube tutorial on 'Functions in python'

Although we had a slight overview about functions in one of the previous modules, here we are going to deep dive about them.

Definition:-
Functions are block of code which can be executed when they are called by the programmer.
Functions are used to reduce the code redundancy and make the code more readable and maintainable.

Applications of function:
1. Code reusability:- Functions are used to reduce the code redundancy and make the code more readable and maintainable.
2. Code organization:- Functions are used to organize the code in a logical way.
3. Modularity:- Functions are used to divide the code into small modules which can be used to perform a specific task.
4. Reusability:- Functions are used to reuse the code in different parts of the program.
5. Readability:- Functions are used to make the code more readable by giving a meaningful name to
the function.
6. Maintainability:- Functions are used to make the code more maintainable by dividing the code into
small modules.

Let us understand with a simple example:

Suppose a programmer wants to display/print "Hello World" on the console. Now to do this he calls the print() function and this function executes the code written inside it in some other module and when that code executes, the string written inside it will be printed successfully on the console.

Types of functions (This will clarify about the working even more):
1. Built-in functions:-
These are the functions which are already defined in the python language and we can use them directly without defining them. For example: print(), input(), len(), etc.

2. User-defined functions:-
These are the functions which are defined by the programmer himself.

1. Built-in functions:-

When we install python in our system then there are some files which contain the code necessary for the functions we use normally like the print(), input() etc. These type of functions are called Built-in function.

2. User-defined functions:-
Suppose a programmer wants to print the sum of three variables, and wants to use this functionality multiple times in his code. In this case instead of writing the code of addition again and again, he sipmly creates a function to do so.

Syntax:
def function_name(arguments):
     code to be executed
   return


Firstly we use the 'def' keyword to define a function.
function_name() is the name of the function which can be anything but it should be unique and should not be a keyword of python.

arguments are the variables which are passed to the function when it is called. These variables are called
parameters of the function.

The code to be executed is the code which will be executed when the function is called.
return is the keyword which is used to return the value of the function.
The function can be called by simply writing the function_name() in the code.
The function can be called multiple times in the code.
'''

# Example: Defining a function to add three variables:
def addition(a,b,c):
    print("The sum of ",a," ",b," ",c," is =", a+b+c)
    return 0
''' Here return 0 means that the function will simply execute the code written inside it but will not provide a value, instead of print statement here we could also write it after return like this:

def addition(a,b,c):
    return print("The sum of ",a," ", b," ",c," is =", a+b+c)
'''

# Calling/Using the function:
addition(1,2,3)
addition(4,5,6)
addition(7,8,9)
addition(10,11,12)
addition(13,14,15) # You may call it anywhere now and as many times as you like

'''
Lambda function:-
Lambda functions are the anonymous functions which are used to create small functions. They are used when we need to pass a function as an argument to another function. They are also called as the 'one line function' because they can be written in a single line.
'''

# Example:

# Define and assign the lambda function to a variable
add_five = lambda a: print(a + 5) #<-- lambda function takes only one variable as argument

# Call the lambda function with an argument
add_five(5)

'''
Global variable:-
Global variables are the variables which are defined outside the function and can be accessed from any part of the program. These variables are accessible from any part of the program.

Local variable:-
Local variables are the variables which are defined inside the function and can be accessed only inside the function. These variables are not accessible from outside the function.

Note:-
The keyword global can be used to make a local variable global, which might be present inside a function or a class.

Example is as follows:

'''

def fun():
    global x #<-- making x global
    x = 10

x = 15
fun()
print('The value has been changed for this global variable from 15 to -->',x)

'''
globals() function:-
The globals() function is used to return the global symbol table as a dictionary. It is used to access the global variables from inside the function.

Example is as follows:

'''

def func():
    x = 10
    globals()['x'] = 20
    print('This is a local variable -->',x)


x = 15
func()
print('This is a global variable which was changed in a function using the globals() function-->',x)