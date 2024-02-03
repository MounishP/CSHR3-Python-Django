"""
WAPP to find the maximum of 3 numbers non of the 3 values are same
"""

a = int(input("Enter a value: "))  # 3
b = int(input("Enter b value: "))  # 2

max = a  # max = 3

if b > max:  # 2>3
    max = b

print(f"The greater num is {max}")  # max = 8
