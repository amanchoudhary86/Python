# A set is an unordered collection of unique elements. 
# This data type allows you to store a group of elements without duplicates.
# Sets are written with curly brackets '{}'.
# Sets are unordered, meaning they do not maintain the order of elements.
# Sets are mutable, meaning you can add or remove elements after the set has been created.
# However, the elements within the set must be immutable (e.g., numbers, strings, tuples).

# Creating a set
s = {1, 2, 3, "String1", "String2", 1.5, 4.2}
print("Initial set:", s)

# Note that sets automatically remove duplicate values
s_with_duplicates = {1, 2, 2, 3, "String1", "String1", 1.5, 1.5}
print("Set with duplicates removed:", s_with_duplicates)

# Adding elements to a set using add()
s.add("New Element")
print('After adding "New Element":', s)

# Adding multiple elements to a set using update()
s.update([5, 6, 7])
print('After adding multiple elements [5, 6, 7]:', s)

# Removing elements from a set using remove()
s.remove(1)
print("After removing element 1:", s)

# Removing elements using discard() (no error if the element doesn't exist)
s.discard(10)  # No error even if 10 is not in the set
print("After discarding element 10 (not present):", s)

# Removing elements using pop() (removes a random element due to unordered nature)
popped_element = s.pop()
print("After popping a random element:", s)

# Clearing all elements from a set
s.clear()
print("After clearing all elements:", s)

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: combines elements from both sets
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# Intersection: returns elements present in both sets
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# Difference: returns elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b (i.e., set_a - set_b):", difference_set)

# Symmetric Difference: returns elements in either set_a or set_b but not in both
symmetric_difference_set = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b:", symmetric_difference_set)

# Checking membership
print("Is 2 in set_a?", 2 in set_a)
print("Is 5 in set_a?", 5 in set_a)