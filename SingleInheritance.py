class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def legs(self):
        print("Dog as 4 legs")


dog = Dog()
dog.sound()
