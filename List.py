# Lists

# A list is an ordered collection of items, which can be of any data type. Lists are mutable, meaning that you can change their contents without changing their identity.

ls = ["Python",1,2,3,True,2.5]
print(ls)

# Just like Strings lists also have the concept of indexing for the elements it contais
print(ls[0:5:2])

# To change an element:
ls[0] = "Programming"
print(ls)