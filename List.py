# Lists:-

# A list is an ordered collection of items, which can be of any data type. Lists are mutable, meaning that you can change their contents without changing their identity.

ls = ["Python",1,2,3,True,2.5]
lst = ls
print(ls)

# Just like Strings lists also have the concept of indexing for the elements it contais:
print(ls[0:5:2])

# To change an element:
ls[0] = "Programming"
print('ls[0] = "Programming -->"',ls)

# To add an element at the last of a list:
ls.append("This is an added element")
print('ls.append("This is an added element") -->',ls)

# To add an element at a specific position:
ls.insert(3,"New Element")
print(ls)

# ls.insert(Index to be inserted upon,"Element to be added") <-- For reference only

# To delete the last element of a list:
ls.pop()
print(ls)

# To delete a specific element at a given index:
ls.pop(3)
# ls.pop(Index number) <-- for reference only
print(ls)

# OR

del ls[3]
# del ls[Index number] <-- for reference only
print(lst)

# Main Difference: del ls[3] does not return the value of the deleted value (Erases the value  completely) whereas ls.pop(3) removes the value and returns it back(meaning that the removed element can be stored in another variable)

# To delete an element by its value:
ls.remove("New Element")