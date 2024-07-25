# Modules:-

# A module is nothing but a python file which contain some python code which is pre-written by some other programmer. Modules are basically used to use the code of some other files to use in our file, as simple as that.

# For example:-
# If we want to use the functions written in the previous file '12_Functions.py', then we firstly we import that particular module int our file like the following:

import L_functions

# Now we can use the functions ar any other part of code of that module in our file.

# syntax:
# imported_filename.function_name()

L_functions.addition(1,5,10)

# on executing this code we get the following output:

# The sum of  1   2   3  is = 6
# The sum of  4   5   6  is = 15
# The sum of  7   8   9  is = 24
# The sum of  10   11   12  is = 33
# The sum of  13   14   15  is = 42
# 10
# The sum of  1   5   10  is = 16 <-- this is the usage of the addition() function we created in another file in our current file.

# Note: As we imported the file, the whole code was imported here, and that is why we are able to see the output of that file as well, to avoid this and only use the addition() function we use the following method:

from L_functions import addition

print("As you can see below the whole file was not imported, but only the addition() function:-")
addition(1 , 1 , 1)
