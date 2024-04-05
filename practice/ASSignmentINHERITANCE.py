"""1. Define a base class Product that represents a generic product.
It should have attributes such as name, price, and quantity.

Implement subclasses for different types of products, such as Electronics, Clothing, and Books.
Each subclass should inherit from the Product class and include additional attributes and methods
specific to the product type.

Problem Statement: Online Shopping System

You are tasked with developing an online shopping system that allows users to browse products,
add them to a shopping cart, and place orders. The system should support different types of products,
such as electronics, clothing, and books.

Requirements:

1. Define a base class Product that represents a generic product.
It should have attributes such as name, price, and quantity.

2. Implement subclasses for different types of products, such as Electronics, Clothing, and Books.
Each subclass should inherit from the Product class and include additional attributes and methods
specific to the product type.

3. Implement a class ShoppingCart that allows users to add products, remove products, view the total price,
and place orders. It should utilize inheritance to inherit common functionality from a base class.

4. Implement a class User that represents a user of the online shopping system.
It should have attributes such as name, email, and address.

5. Extend the User class to create subclasses for different types of users, such as Customer and Admin.
Each subclass should inherit from the User class and include additional attributes and methods specific to
the user type.

6. Implement appropriate methods for displaying information about products, users, and orders.

Tasks:

1. Design a class hierarchy for the online shopping system, incorporating inheritance, encapsulation, and
polymorphism.

2. Implement the classes based on the defined class hierarchy.
3. Create sample instances of products, users, and shopping carts to test the functionality of the system.
4. Ensure that the system handles different types of products and users correctly, providing appropriate
functionality and behavior for each.

Additional Considerations:

Handle edge cases and error conditions gracefully.
Implement validation for user input and data integrity.
Optimize the system for performance and scalability.
Provide clear documentation and comments to explain the purpose and usage of each class and method."""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product Name : {self.name}, price :{self.price}, Quantity : {self.quantity}")


class Electronics(Product):

    def __init__(self, name, price, model, quantity):
        super().__init__(name, price, quantity)
        self.model = model

    def display_info(self):
        print(f"Product Name : {self.name}, Price :{self.price}, Quantity : {self.quantity}, Model: {self.model}")


class Clothing(Product):

    def __init__(self, name, price, size, quantity):
        super().__init__(name, price, quantity)
        self.size = size

    def display_info(self):
        print(f"Product Name : {self.name}, Price :{self.price}, Quantity : {self.quantity}, Size: {self.size}")


class Books(Product):
    def __init__(self, name, price, gener, author, quantity):
        super().__init__(name, price, quantity)
        self.gener = gener
        self.author = author

    def display_info(self):
        print(
            f"Product Name : {self.name}, Price :{self.price},Quantity : {self.quantity}, Author : {self.author}, Genere : {self.gener}")


class Shoppingcart:
    def __init__(self):
        self.products = []

    def addProducts(self, product):
        self.products.append(product)

    def removeProducts(self, product):
        self.products.remove(product)

    def totalPrice(self):
        for product in self.products:
            sum = sum + product.price
        return sum


class User():
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def display_info(self):
        print(f"Name : {self.name}, Email: {self.email}, address : {self.address}")

class Customer(User):
    def __init__(self, name, email, address, gender):
        super().__init__(name, email, address)
        self.gender = gender
    def display_info(self):
        print(f"Name : {self.name}, Email: {self.email}, address : {self.address}, Gender: {self.gender}")

class Admin(User):
    def __init__(self, name, email, address, pin):
        super().__init__(name, email, address)
        self.pin = pin
    def display_info(self):
        print(f"Name : {self.name}, Email: {self.email}, address : {self.address}, Pin: {self.pin}")


product1 = Product("laptop", 799, 1)
    product1.display_info()
appliances = Electronics("Teleivision", 990, "xyz", 2 )
    appliances.display_info()
appearl = Clothing("Levis", 600, "M", 1)
    appearl.disply_info()
saga = Books("Manfrotto", 180, 'Romance',"Shashank", 1)
    saga.display_info()
user1 = User("Shaaz", "shaazd@xyz.com", "174 Lurline st")
    user1.display_info()
customer1 = Customer("Rahul", "Rahul@xyz.com", "2 Half St","M")
    customer1.display_info()
admin1 = Admin("Anudeep","anud@xyz.com","28 Queens rd")
    admin1.display_info()