# Note : Do read the Introduction to know the definition of a class

# This is how a class is defined:

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def start(self):
        print(f"You start the {self.model} ")

    def stop(self):
        print(f"You stop the {self.model} ")

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