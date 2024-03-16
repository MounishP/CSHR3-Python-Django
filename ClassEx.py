class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Brand:{self.brand} & Model: {self.model}")


myCar = Car("Audi", "A4")
shashank = Car("BMW", "530d")
anudeep = Car("Ford", "Mustang")

anudeep.drive()
