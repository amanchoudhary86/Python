'''Modules:-

A module is nothing but a python file which contain some python code which is pre-written by some other programmer. Modules are basically used to use the code of some other files to use in our file, as simple as that.

For example:-
If we want to use the functions written in the previous file '12_Functions.py', then we firstly we import that particular module int our file like the following:
'''

import L_functions
from L_functions import addition

'''
Now we can use the functions ar any other part of code of that module in our file.

syntax:
imported_filename.function_name()

on executing this code we get the following output:

The sum of  1   2   3  is = 6
The sum of  4   5   6  is = 15
The sum of  7   8   9  is = 24
The sum of  10   11   12  is = 33
The sum of  13   14   15  is = 42
10
The sum of  1   5   10  is = 16 <-- this is the usage of the addition() function we created in another file in our current file.

Note: As we imported the file, the whole code was imported here, and that is why we are able to see the output of that file as well, to avoid this and only use the addition() function we use the following method:
'''


print("As you can see below the whole file was not imported, but only the addition() function:-")
addition(1 , 1 , 1)

'''
Note : If there is a folder named '__pycache__' which is automatically created then let it be and need not worry about it. For now you just need to know that it is created so that the next time this file runs then it need not import the modules again and again. Once this folder is created, the next time we run this program, you might not notice it but it will run faster.

This folder stores compiled versions of your Python files, which helps the program run faster the next time you execute it. You don't need to worry about this folder as Python handles it for you. Just know that it's there to make your programs more efficient.

Pro tip : There are tons of pre-built modules for python which are used by all the programmers. Database connection, folder creation, Digital Art making, making a web app, etc. there is a library(collection of many modules) for almost everything in Python. We will use them one by one in our upcoming programs.
'''