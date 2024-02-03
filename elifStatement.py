"""
if a number is divisible by 3 then print dominos
if a number is divisible by 5 then print pizza hut
if a number is divisible by 15 then print kfc
"""

n = int(input("Enter a number: "))

if n % 3 == 0 and n % 5 == 0:
    print("KFC")
elif n % 5 == 0:
    print("Pizza Hut")
elif n % 3 == 0:
    print("Domino's")
else:
    print("Enter a multiple of 3 or 5 or 15")
