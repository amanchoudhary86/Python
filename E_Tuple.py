# Tuples:-

# Tuples are same as list but they are immutable(cannot be changed like list) and there is also a slight change in syntax. '()' are used here to contain the elements.
# Tuples are used when we want to store a fixed set of values and we don't want to change them later. Tuples are also used when we want to store a set of values that are related to each other.

tpl = (1,2,3,"String1", "String2","String3",1.23,2.34,3.45)

# tpl.index() returns the index number of the specified element
print('print(tpl.index("String2")) --> ',tpl.index("String2"))
# tpl.index(element value) <-- For reference only

# tpl.count() returns the number of times the specified element occurs in the tuple
print('print(tpl.count("String2")) --> ',tpl.count("String2"))
# tpl.count(element value) <-- For reference only

# Note: a Tuple can also be create without the use of paranthesis '()'
# Example:
tpl2 = 1,2,3,"String1", "String2","String3",1

# Tuple Unpacking:
# Tuple unpacking is a feature in Python that allows us to assign the values of a tuple to multiple variables in a single line of code. It's a way to extract the elements of a tuple and assign them to separate variables.

tpl2 = 1,2,3,4 #This is created without the use of paranthesis () for the ease of understanding. Enclosing the elements in paranthesis is totally up to you.

a,b,c,d = tpl2

print(c)

random_var = -5
print(abs(random_var))

random_var2 = 67
print(abs(random_var2))

# abs() function is a function which always returns the positive value