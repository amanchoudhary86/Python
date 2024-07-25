# If you have not reached 'M_Module2.py' then no need to worry about this file and just skip it. 

# Note : If you read it before reaching the above mentioned module, you might get confused.

def simple_function():
    print("Hello World")

if __name__ == "__main__":
    simple_function

    # Everything in this if-statement executes only if the programmer wants to execute it in the M_Modules_2 file. Thanks to it the function simple_function will not run just by importing example.py

else:
    print("This is a string which was printed just because of importing. The programmer did not even wanted to print it.")