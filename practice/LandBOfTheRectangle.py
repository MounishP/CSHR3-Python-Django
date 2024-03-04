"""Take values of length and breadth of a rectangle from user
and check if it is square or not. Also calculate the area"""
l = int(input(" enter the length : "))
b = int(input("enter the breadth : "))
area = l*b
if l == b:
    print("it is a square")
    print(f"{area}is the area")

else:
 print("it is not a square")


