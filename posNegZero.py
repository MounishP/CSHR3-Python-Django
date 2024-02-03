"""
WAPP using conditional statements only: take a number and find out if the number is positive,
negative or zero
"""

n = int(input("Enter a number: "))

if n > 0:
    print("n is positive number")
elif n < 0:
    print("n is negative number")
else:
    print("n is zero")
