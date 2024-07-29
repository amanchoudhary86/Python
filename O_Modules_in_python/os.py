import os

# (os stands for operating system)

print(dir(os) , "<-- This are all the directories present in this module")

print(os.getcwd(), "<-- This is the current working directory") # cwd means current working directory
# Output: C:\Users\Aman\OneDrive\Desktop\Python\O_Modules_in_python


os.chdir(r"C:\Users\Aman\OneDrive\Desktop\Python")

print(os.getcwd(), "<-- This is the current working directory") # cwd means current working directory
# Output: C:\Users\Aman\OneDrive\Desktop\Python

# As you can see above that the directory has been changed

os.chdir(r"C:\Users\Aman\OneDrive\Desktop\Python\O_Modules_in_python")
f = open("template.txt") # Note : Make sure you are in the correct directory to read this file otherwise it might raise an error.
print("The file template.txt has been read")

print(os.listdir(r"C:\Users\Aman\OneDrive\Desktop\Python\O_Modules_in_python")) # <--This prints all the files and directories in the given path.

os.mkdir("Template_Directory_1") #<-- This simply creates a directory?folder named "Template_Directory" in our current working folder
# Note : Only run this code once because it might cause an error saying that the directory we want to create already exists.

os.makedirs("Template_directory_2/New")
# Note : This creates directories within directories

# Note : You cannot rename a file which is already opened by the program(refer line 19)
f.close()

os.rename("template.txt", "template_2.txt")
# This is simply used to rename the files

# These are only some of the implementation of the os module. I would suggest you to visit the official documentation for this module on the official page of python