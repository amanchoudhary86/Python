
# Important : there is a special variable name in python and it is '__name__'. when we run a python file directly then, this variable stores the string "__main__". And if the file is run by importing then the filename is stored in it.

# Remember we met a file called example.py on the way? Time to use it here:
import example

# Note: If we import a file and execute the code, then the whole code written in the imported file gets extcuted. For this to not happen we use the following:


# if __name__ == "__main__":
#     simple_function

# Note : Refer example.py
