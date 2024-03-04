"""
Write a program that reads two integers (n1 and n2) and
an operator that performs a particular Arithmetic operations with them.

"""

n1 = int(input("Enter n1 Value : "))
n2 = int(input("Enter n2 value : "))
operation = input("Enter arithmetic operation : ")

if operation == "add":
    print(n1+n2)
elif operation == "sub":
    print(n1 - n2)
elif operation == "mul":
    print(n1 * n2)
elif operation == "div":
    print(n1 / n2)
else:
    print("enter valid arithmatic operators and positive numbers" )
