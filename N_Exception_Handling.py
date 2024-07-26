# Exception Handling :-
# Exception handling is a mechanism in programming languages that allows developers to manage and respond to runtime errors or unusual conditions that may occur during the execution of a program. Instead of causing the program to crash, exceptions can be caught and handled gracefully, enabling the program to continue running or to fail in a controlled manner.

# What is Exception Handling :- 
# In programming, things don't always go as planned. For example, you might try to divide a number by zero, or read from a file that doesn't exist. These situations cause errors called "exceptions." Exception handling is a way to catch these errors and do something about them, so your program doesn't crash unexpectedly.

# Why Use Exception Handling :-
# Prevent Crashes: If your program encounters an error, it can handle it and keep running instead of crashing.
# Provide Useful Feedback: You can show user-friendly messages instead of cryptic error messages.
# Ensure Cleanup: Make sure important cleanup actions (like closing a file) are always performed.

# Exception handling is done with the help of the following :-

# Exception handling is done with the following:

# 1. Try Block:
#    - The 'try' block is used to write the code that might cause an exception (an error).
#    - If everything runs smoothly, the code inside the 'try' block executes normally.

try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)

# 2. Except Block:
#    - The 'except' block is used to handle the exception.
#    - If an error occurs in the 'try' block, the code inside the 'except' block will run.
#    - You can have different 'except' blocks for different types of errors.

except ZeroDivisionError:
    # Code to handle division by zero error
    print("Error: You can't divide by zero!")

except ValueError:
    # Code to handle value error (e.g., input is not a number)
    print("Error: Please enter a valid number.")

# 3. Finally Block:
#    - The 'finally' block is optional.
#    - It contains code that will always run, whether there was an error or not.
#    - This is useful for cleanup tasks.

finally:
    # Code that always runs
    print("Thank you for using the program.")