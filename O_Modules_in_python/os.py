import os

# (os stands for operating system)

print(dir(os) , "<-- This are all the directories present in this module")

print(os.getcwd(), "<-- This is the current working directory") # cwd means current working directory
# Output: C:\Users\Aman\OneDrive\Desktop\Python\O_Modules_in_python


os.chdir("C:\Users\Aman\OneDrive\Desktop\Python")

print(os.getcwd(), "<-- This is the current working directory") # cwd means current working directory
# Output: C:\Users\Aman\OneDrive\Desktop\Python

# As you can see above that the directory has been changed