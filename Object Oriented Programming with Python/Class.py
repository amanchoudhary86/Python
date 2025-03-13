'''This is the basic syntax for creating a class in python and using it'''

class Car:
    def __init__(self, model, year, for_sale, color):
        self.model = model
        self.year = year
        self.for_sale = for_sale
        self.color = color

    def start(self):
        print(f"You start the {self.model} ")

    def stop(self):
        print(f"You stop the {self.model} ")

car1 = Car("BMW LXI", 2025, "Not_For_Sale", "Red")

print(car1.model)

car1.start()
car1.stop()