'''Dictionary:-

A Dictionary in Python is like a real-world dictionary. Just as a real dictionary connects words to their meanings, a Python dictionary connects keys to values.

Key Features:-

1) Collection of Key-Value Pairs: Each item in a dictionary has a key and a value. You can think of the key as a word and the value as its definition or explanation.

2) Unordered: Unlike a list, where items are in a specific order, dictionaries do not store items in any particular order. This means that when you loop through a dictionary, the items may not come out in the order you added them.

3) Mutable: You can change a dictionary after it's created. You can add new items, change existing ones, or remove them.

4)Indexed: You access the values in a dictionary using their keys, similar to looking up a word in a dictionary to find its meaning.

Note: Every key should be unique.
'''

dictionary = {'A':5, 'B':6, 'C':7}
print(dictionary['A']) # Output: 5

print(dictionary)

# To add an element
dictionary['D'] = 8

print("dictionary['D'] = 8 --> ",dictionary)

# To Change an element:
dictionary['D'] = 10
print("dictionary['D'] = 10 --> ",dictionary)

# To remove an element:
dictionary.pop('D')
print("dictionary.pop('D') --> ",dictionary)

# To print the keys:
print("Keys: ",dictionary.keys())