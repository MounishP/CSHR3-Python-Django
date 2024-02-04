"""
Assume the card is inserted
Enter the pin
validate the pin
Welcome
"""

originalPin = 9595
for chance in range(1,4):
    pin = int(input("Enter the pin: "))
    if originalPin == pin:
        print("************************************************")
        print("*                                              *")
        print("*           Welcome to Mounish Bank            *")
        print("*                                              *")
        print("************************************************")
        print("Logged in successfully")
        break
    else:
        print("Incorrect pin")
