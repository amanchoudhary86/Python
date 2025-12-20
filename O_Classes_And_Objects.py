'''This section will help you apply the basics you just learned to make the programs more efficient as well as you will also get to learn some new topics related to object oriented programming.

There are generally two types of programming:
1. Procedural Programming: This is the type of programming you have been doing so far. It is based on the concept of procedures or functions that perform certain tasks. The program flow is determined by the sequence of procedures or functions that are called. In simpler terms we break the code into a set of functions and these functions call each other.

2. Object Oriented Programming (OOP): This is a programming paradigm that revolves around the concept of objects and classes. It is based on the idea of encapsulation, inheritance, and polymorphism. In this section, we will learn about the basics of OOP and how to apply it to make your programs more efficient.
'''

'''
What is a class?

A class is a blueprint for creating objects. It is a way to group related data and functions together. A class can have attributes (data) and methods (functions) that operate on the data.

Easy Explaination: It is like a bundle of variables and functions that are related to each other.

Syntax of a class:

class ClassName:
    attributes
    methods

Note: Attributes are simply the variables defined inside a class
Note: Methods are simply the functions that are defined inside a class
    
'''

'''
What is an object?

An object is an instance of a class. It is created using the class blueprint. An object can have its own unique attributes and methods that are defined in the class.

Easy Explaination: It is a way of using the attributes and methods of a class.

Syntax of an object:

object_name = ClassName()


'''

# Example of a class and an object:
# Class:-
class Restaurant:
    Name = "Italian"
    location = "New York"
    rating = 4.5
    delivery = True

# Object of class Restaurant
print("Object's usage:")
my_restaurant = Restaurant()
print("Restaurant Name:", my_restaurant.Name)
print("Location:", my_restaurant.location)
print("Rating:", my_restaurant.rating)
print("Delivery Available:", my_restaurant.delivery)

# using a class and object we can also assign our own values to the attributes of the class like this:
my_restaurant.Name = "Taj"
print("Updated Restaurant Name:", my_restaurant.Name)

print("\nCreating another object and using it:")
your_restaurant = Restaurant()
your_restaurant.location = "San Francisco"
print("Your Restaurant Location:", your_restaurant.location)