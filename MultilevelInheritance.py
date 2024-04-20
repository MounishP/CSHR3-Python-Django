class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def legs(self):
        print("Dog as 4 legs")

    def sound(self):
        print("Bark")


class Labrador(Dog):
    def color(self):
        print("Brown")


lab = Labrador()
denver = Dog()
denver.sound()

lab.sound()