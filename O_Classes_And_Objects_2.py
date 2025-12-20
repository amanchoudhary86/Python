''' Now to use the classes and objects there are many other methods as well which we will look here one by one: '''

# Using Dummy or no values:

class Car:
    brand = ""
    model = ""
    year = 0
# As you can see we provided an empty/Dummy values into the attributes of this class. Now we can modify the object or simply create new values using these into an object, just like this:

my_car = Car()
my_car.brand = "Toyota"
my_car.model = "Camry"
my_car.year = 2020

print(vars(my_car)) # vars() function is used to print the attributes of the object in the form of a dictionary.

# Similarily we can create and use more and more objects using the same class.

''' Using __init__() method:-
Whenever we create an object then everytime we use the class's attributes and due to this we have to assign the values to the attributes of the class again and again. To avoid this we can use the __init__() method which is a special method that is called when an object is created. It is used to initialize the attributes of the class. Meaining for each object we can create their own unique attributes'''

print("\nUsing __init__() method:")

class Bike:
    def __init__(self, brand, color, year_bought):
        self.brand = brand
        self.color = color
        self.year_bought = year_bought

# Creating an object of the class Bike
my_bike = Bike("BMW", "White", 2018)
print(vars(my_bike))

# Note that __init__() also uses a separate parameter called self. This represents the object we'll create out of Bike(). We need to include self whenever we want to use __init__(). It's always the first parameter.