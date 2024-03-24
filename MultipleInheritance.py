class Mother:
    def house(self):
        print("Dad's house")


class Father:
    def bike(self):
        print("Son's bike")


class Daughter(Father, Mother):
    def car(self):
        print("Daughter's car")


daughter = Daughter()
daughter.house()
