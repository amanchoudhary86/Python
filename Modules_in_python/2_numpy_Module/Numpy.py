'''Numpy :-

Firstly, What are arrays?
An array is a data structure that can hold a collection of elements, typically of the same data type, in a contiguous block of memory. Elements in an array are accessed using indices, with the first element typically located at index 0. Arrays are commonly used to store and manipulate sequences of data efficiently.

NumPy is a popular Python library used for working with arrays and numerical data. It provides tools for creating and manipulating large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. NumPy is widely used in scientific computing, data analysis, and machine learning because it enables fast and flexible data processing.

Numpy is usually much faster than lists because it stores fixed data types and also because it stores the data in contiguous memory format (Meaning that there is no memory space between two elements)

Uses of numpy:-
1. Mathematics (MATLAB Replacement)
2. Plotting (Matplotlib)
3. Machine Learning
4. And many more.
'''

# Firstly let's import numpy
import numpy as np

# Now let's create a numpy array
arr = np.array([1, 2, 3, 4, 5])
print("This is a 1-Dimensional OR 1D array-->", arr)
# Output: [1 2 3 4 5]


# Now let's create a 2D numpy array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("This is a 2-Dimensional OR 2D array:-")
print(arr2d)

# Now let's create a multidimensional array:-
arrMulti = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("This is a 3-Dimensional OR 3D array:-")
print(arrMulti)

# To get the dimension of a particular array:-
print("Dimension of the array arr:-")
arr.ndim()

print("Dimension of the array arr:-")
arr2d.ndim()

print("Dimension of the array arr:-")
arrMulti.ndim()

# Work in Progress...⚒️