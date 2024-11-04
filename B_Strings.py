'''A string is a sequence of characters used to store and represent text.
In Python, strings are created by enclosing text in quotes.
You can use single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
Triple quotes are useful for multi-line strings or strings containing both single and double quotes.'''

# Example of strings:
single_quote_string = 'Hello, world!'
double_quote_string = "Hello, world!"
triple_quote_string = """This is a string
that is in multiple lines."""

print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)

'''Strings can contain letters, numbers, symbols, and spaces.
You can include special characters like newlines (\n) or tabs (\t) using escape sequences.

To define a string, follow these rules:
1. Enclose your text in matching quotes (single, double, or triple).

2. To include a quote character inside a string, use the opposite type of quote or escape it with a backslash (\).
   For example, "She said, 'Hello!'" or 'He said, "Hello!"' or "He said, \"Hello!\""

3. Strings are immutable, which means you cannot change individual characters after the string is created.
However, you can create new strings based on existing ones.'''

# Example of escaping quotes --> \' OR \" :
escaped_string = 'He said, "It\'s a beautiful day!"'
print(escaped_string)

# Example of escaping a backslash itself --> \\
backslash_string = "This is a backslash: \\"
print(backslash_string)

# Example of a raw string:
raw_string = r"This is a raw string with a backslash: C:\Desktop\Python\B_Strings.py "
print(raw_string)
# in order to make a rew string the user needs to put 'r' before the string

'''Strings are commonly used for displaying messages, handling text input/output, and processing textual data.

function : A function is a block of code which is used to perform some predefined or defined task
Ex: print() is a function to print the given content on the console
Types of functions:
1. Pre-defined functions : print(), input() etc. which are already written for us to use
2. User-defined functions : These are the functions which are defined by the user, meaning that their name and the task they perform is also set by the user itself.

Note : In depth study of functions will be done in later modules

id():-
id() function returns the “identity" of the object, which is an integer that is guaranteed to be unique and constant for the object during its lifetime.
It is used to check whether the two variables point to the same object in memory or not.'''
print("print(id(10)) -->",id(10))
print("print(id(10.5)) -->",id(10.5))
print('print(id("Hello")) -->',id("Hello"))

# Note: If you did not understand the above mentioned three points just know that id() simply provides the memory address of what is inside it.
'''
All the alphabet characters, numbers, and special characters are stored in the memory in the form of ASCII values.
ASCII stands for American Standard Code for Information Interchange.

ASCII values are the integer values which are assigned to the characters. For example, the ASCII value of 'A' is 65, 'B' is 66, 'a' is 97, 'b' is 98, '0' is 48, '1' is 49, etc.

1. From 'A' to 'Z' the ASCII values are from 65 to 90.
2. From 'a' to 'z' the ASCII values are from 97 to 122.


ord():-
ord() function returns the ASCII value of the character passed to it.'''
print(ord('A')) # prints 65
print(ord('a')) # prints 97

'''chr():-
chr() function returns the character of the ASCII value passed to it.'''
print(chr(97)) # prints a
print(chr(65)) # prints A

# 'end' parameter in print() functions:
'''Simply put, it specifies what the string ends with:'''
print("An example of end", end=" in print function\n")

# 'sep' parameter in print() functions:
'''It is used to specify the separator between the values to be printed.'''
print("1","9","2024", sep="-")

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

'''
Note : Forward indexing starts from 0 but the Backward indexing starts from -1
Note : If we try to access a character which is not present in the string, it will
throw an error called "IndexError"
'''


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

# Capitalizes the first character of the string and makes the rest lowercase.
print("str.capitalize()--> ", str.capitalize())

# Capitalizes the first character of each word in the string.
print("str.title()--> ", str.title())

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

'''
Simple calculation:
Total characters in the string = 37
Total characters in the field = 45
Total characters to be printed = 45 - 37 = 8 --> 4 on left and 4 on right (because it is str.center())
same thing is also done for the following two functions with some slight change in the position of stars --> (*)
'''

# Left justifies the string in a field of the specified width, padding with the specified character.
print("str.ljust(45, '*')--> ", str.ljust(45, "*"))

# Right justifies the string in a field of the specified width, padding with the specified character.
print("str.rjust(45, '*')--> ", str.rjust(45, "*"))

# Next variable or data type that we are going to study is called 'Boolean'