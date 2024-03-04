"""Check whether the given number is positive and divisible by 5 or not."""

n = int(input(" enter the number"))
if n>=0:
    print("it is a positive number")
    if n%5==0:
         print("it is divisible by 5")
    else:
        print("it is not divisible by 5")
else:
    print("it is a negative number")

