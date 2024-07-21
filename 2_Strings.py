# A string is a sequence of characters used to store and represent text.
# In Python, strings are created by enclosing text in quotes.
# You can use single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
# Triple quotes are useful for multi-line strings or strings containing both single and double quotes.

# Example of strings:
single_quote_string = 'Hello, world!'
double_quote_string = "Hello, world!"
triple_quote_string = """This is a string
that is in multiple lines."""

print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)

# Strings can contain letters, numbers, symbols, and spaces.
# You can include special characters like newlines (\n) or tabs (\t) using escape sequences.

# To define a string, follow these rules:
# 1. Enclose your text in matching quotes (single, double, or triple).

# 2. To include a quote character inside a string, use the opposite type of quote or escape it with a backslash (\).
#    For example, "She said, 'Hello!'" or 'He said, "Hello!"' or "He said, \"Hello!\""

# 3. Strings are immutable, which means you cannot change individual characters after the string is created.
# However, you can create new strings based on existing ones.

# Example of escaping quotes --> \' OR \" :
escaped_string = 'He said, "It\'s a beautiful day!"'
print(escaped_string)

# Strings are commonly used for displaying messages, handling text input/output, and processing textual data.

# function : A function is a block of code which is used to perform some predefined or defined task
# Ex: print() is a function to print the given content on the console
# Types of functions:
# 1. Pre-defined functions : print(), input() etc. which are already written for us to use
# 2. User-defined functions : These are the functions which are defined by the user, meaning that their name and the task they perform is also set by the user itself.

# Note : In depth study of functions will be done in later modules

# 'end' in print() functions:

# Simply put it specifies what the string ends with:

print("An example of end", end=" in print function\n")


#Indexing: It means, numbering of the characters of a string. It is done in the following way:

st = "This is a sample string"
print(st[0]) # prints T which is the First character of this string
print(st[1]) # prints h
print(st[22]) # prints g
# This is called the Forward/Positive indexing


print(st[-1]) # prints g which is the last character of this string
print(st[-2]) # prints n
print(st[-21]) # prints h
# This is called the Backward/Negative indexing

# Note : Forward indexing starts from 0 but the Backward indexing starts from -1
# Note : If we try to access a character which is not present in the string, it will
# throw an error called "IndexError"


# Following are some pre-defined functions which can be used on strings:
str = "----This is another sample string----"

# len() : This function returns the length of the string
print("str.len()--> ",len(str))  # Prints the length of the string.

# Slicing: prints the string according to the starting, ending, and the jump specified.
print(str[4:15:2])  # Prints characters from index 4 to 15 with a step of 2.
# print(str[starting point: ending point : Jump]) <-- Not an actual code, just for reference

# Converts all characters in the string to lowercase.
print("str.lower()--> ", str.lower())

# Converts all characters in the string to uppercase.
print("str.upper()--> ", str.upper())

# Counts the number of occurrences of the substring "a" in the string.
print('str.count("a")--> ', str.count("a"))

# Finds the index of the first occurrence of the substring "b". Returns -1 if not found.
print('str.find("b")--> ', str.find("b"))

# Removes leading and trailing characters specified (in this case, "-").
print('str.strip("-")--> ', str.strip("-"))

# Removes leading characters specified (in this case, "-").
print('str.lstrip("-")--> ', str.lstrip("-"))

# Removes trailing characters specified (in this case, "-").
print('str.rstrip("-")--> ', str.rstrip("-"))

# Checks if the string starts with the specified substring.
print('str.startswith("----")--> ', str.startswith("----"))

# Checks if the string ends with the specified substring.
print('str.endswith("----")--> ', str.endswith("----"))

# Replaces occurrences of the first substring with the second substring.
print('str.replace("another", "a different")--> ', str.replace("another", "a different"))

# Splits the string into a list of substrings based on the specified delimiter.
print("A,B,C,D,E = str.split() splits the str sring and assigns them in variables A,B,C,D and E")
A,B,C,D,E = str.split()
print(A,"\n",B,"\n",C,"\n",D,"\n",E) # Prints the substrings in the list.

# Checks if all characters in the string are digits.
print("str.isdigit()--> ", str.isdigit())

# Checks if all characters in the string are alphanumeric (letters or numbers).
print("str.isalnum()--> ", str.isalnum())

# Checks if all characters in the string are alphabetic (letters only).
print("str.isalpha()--> ", str.isalpha())

# Centers the string in a field of the specified width, padding with the specified character.
print("str.center(45, '*')--> ", str.center(45, "*"))
# Simple calculation:
# Total characters in the string = 37
# Total characters in the field = 45
# Total characters to be printed = 45 - 37 = 8 --> 4 on left and 4 on right (because it is str.center())
# same thing is also done for the following two functions with some slight change in the position of stars --> (*)

# Left justifies the string in a field of the specified width, padding with the specified character.
print("str.ljust(45, '*')--> ", str.ljust(45, "*"))

# Right justifies the string in a field of the specified width, padding with the specified character.
print("str.rjust(45, '*')--> ", str.rjust(45, "*"))

# Next variable or data type that we are going to study is called 'Boolean'