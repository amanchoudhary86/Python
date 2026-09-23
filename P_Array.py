'''An array is a data structure which can hold a collection of elements in contiguous memory locations. All elements in an array are of the same data type.'''

'''Note: For those who believe that Arrays do not exist in python, it is officially claimed that the The official presence of arrays in Python is documented in the Python Standard Library under the section for the array module. You are free to read the documentation with this link: https://docs.python.org/3/library/array.html.'''

'''There are two options to use the arrays in python:

1. Using the array module.
2. Using the NumPy library.

Although we will be bajorly using numpy library for arrays in python, but we will also look at the array module as well just for the understanding of it's functionality. This is because the array module is not as powerful as the numpy library and it is not widely used in real world applications.'''

'''Note: Arrays are although not built-in data structures in python, as they were built on the top of lists.'''

'''Very important Questionaire:
Question: Does array exist in python?
Answer: If you are asking if it is a built in data structure in python, then the answer is No. But if you are asking if it is a data structure in python, then the answer is Yes. It is a data structure in python but it is not built-in. It is built on the top of lists.'''

'''Some more important points about arrays in python:
1. Arrays are of fixed sizes
2. All the elements in an array are of the same data type.
3. Arrays are stored in contiguous memory locations.
4. Arrays are mutable, which means we can change the elements of an array after it is created.'''

'''
Difference between array and list in python:
1. Data Types:

Array: All elements in an array are of the same data type.
List: A list can contain elements of different data types.

2. Flexibility:

Array: An array is less flexible than a list because it has a fixed size.
List: A list is more flexible than an array because it can easily grow and shrink.

3. Performance:
Array: More memory efficient for larger data sets and faster for numerical operations.
List: Slower for larger datasets.

4. Usage in Python:
Array: Can be used used with the help of the array module or the numpy library.
List: Built-in data structure in Python and can be used directly.

'''

'''
NOTE: This file is devised in two sections: The yellow and the green section. The yellow section is about the array module and the green section is about the numpy library. You are free to follow both the sections, although as an experienced developer I suggest you to follow the green section as it is more powerful and widely used in real world applications. Otherwise any section is fine to follow. The choice is yours. 

Also to keep it simple and easy to understand, I also suggest only following one section.
'''

'''🟨 Yellow Section: array module:'''
print("🟨 Yellow Section: array module:")

'''To get started with the array module, we first need to import it in our file. We can do that by using the following code:'''
import array as arr

'''Creating an array using the array module:'''
new_array = arr.array('i', [1, 2, 3, 4, 5])

'''Note: The first argument 'i'(here it defines the array will be of int type) in the array() function is the type of the array. The second argument is the list of elements in the array. The type of the array can be one of the following:'''

'''Type Codes for Arrays in Python:
Type Code	Description
    i	      integer
    f	       float
    d	      double
'''

print("Here is the original array: ", new_array)

new_array[1] = 10
print("Here is the modified array(arrays are mutable, just like lists): ", new_array)

