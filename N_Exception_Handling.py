'''Exception Handling :-

What is Exception Handling :- 
In programming, things don't always go as planned. For example, you might try to divide a number by zero, or read from a file that doesn't exist. These situations cause errors called "exceptions." Exception handling is a way to catch these errors and do something about them, so your program doesn't crash unexpectedly.

Why Use Exception Handling :-
Prevent Crashes: If your program encounters an error, it can handle it and keep running instead of crashing.
Provide Useful Feedback: You can show user-friendly messages instead of cryptic error messages.
Ensure Cleanup: Make sure important cleanup actions (like closing a file) are always performed.

Exception handling is done with the help of the following :-

Exception handling is done with the following:

1. Try Block:
   - The 'try' block is used to write the code that might cause an exception (an error).
   - If everything runs smoothly, the code inside the 'try' block executes normally.
'''

try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
    # This block of code might cause an error if user inputs a string or 0.

# 2. Except Block:
#    - The 'except' block is used to handle the exception.
#    - If an error occurs in the 'try' block, the code inside the 'except' block will run.
#    - You can have different 'except' blocks for different types of errors.

except ZeroDivisionError:
    # Code to handle division by zero error
    print("Error: You can't divide by zero!")
    # ZeroDivisionError is the name of the error that may appear.

except ValueError:
    # Code to handle value error (e.g., input is not a number)
    print("Error: Please enter a valid number.")
    # ValueError is the name of the error that may appear.

else:
    # Code that runs when except block is not true.
    print("Thank you once again for using the program.")

# 3. Finally Block:
#    - The 'finally' block is optional.
#    - It contains code that will always run, whether there was an error or not.
#    - This is useful for cleanup tasks.

finally:
    # Code that always runs
    print("Thank you for using the program.")


'''
Types of errors/Exceptions :-
1. SyntaxError
2. NameError
3. TypeError
4. ValueError
5. ZeroDivisionError
6. IndexError
7. KeyError
8. AttributeError
9. ImportError
10. IndentatnError

These are the most common and main types of errors. Although there are several more, but for now you will not need those, but you may go and research about them on your own if you are curious.
'''