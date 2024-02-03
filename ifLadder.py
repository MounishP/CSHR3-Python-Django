"""
if a number is greater than 1 then if the check is less than 100
then check if the number is even number
"""

n = int(input("Enter the number: "))

if n > 1:
    print("n is greater than 1")
    if n < 100:
        print("n is less than 100")
        if n % 2 == 0:
            print("n is a even number")
        else:
            print("n is not an even number")
    else:
        print("n is not less than 100")
else:
    print("n is not greater than 1")
