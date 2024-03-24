class Father:
    def house(self):
        print("Dad's house")


class Son(Father):
    def bike(self):
        print("Son's bike")


class Daughter(Father):
    def car(self):
        print("Daughter's car")


son = Son()
daughter = Daughter()
son.house()
son.bike()
daughter.car()
daughter.house()
