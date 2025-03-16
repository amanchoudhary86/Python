# Note : Do read the Introduction to know the definition of a class
from samba.netcmd.drs import cmd_drs_clone_dc_database


# This is how a class is defined:
class Car:
    def __init__(self, model, year, color, for_sale):  # (Constructor)
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        y = 10  # This is a local variable, not an instance variable

    x = 5  # Class variable

    '''Class variables : Class variables are shared across all instances(objects) of that particular class and they are defined outside of the constructor. For Example, x is a class variable whereas y is an instance variable.'''

    def start(self):
        print(f"You start the {self.model} ")

    def stop(self):
        print(f"You stop the {self.model} ")

# Creating instances of the Car class
car1 = Car("Lamborghini", 2025, "Yellow", False)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car2 = Car("BMW", 2020, "Blue", True)
car3 = Car("Mustang GT", 2021, "Red", True)

print(car2.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.start()
car1.stop()
car2.start()
car2.stop()

'''Following is the usage of a class variable:'''

class Student():

    class_year = 2025
    number_of_students = 0

    def __init__(self, Student_Name, age):
        self.Student_Name = Student_Name
        self.age = age
        Student.number_of_students += 1

student1 = Student("Tom", 15)
student2 = Student("Greg",16)

print("The no. of students enrolled:", Student.number_of_students)

'''Inheritance : '''