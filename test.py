"""sum1 = 0
n = int(input("Enter n value"))
for i in range(1,n):
    sum1=sum1+i

"""

def polygonalMenu():
    print("\n -----> MENU <-----")
    print("1. square")
    print("2. triangle")
    print("3. rectangle")
    print("4. circle")
    print("5. Exit")


def display(area):
    print(area)


def Square(side1):
    return side1 ** 2


def triangle(side1, side2, side3):
    return (side1 + side2 + side3) / 2


def rectangle(side1, side2):
    return (side1 * side2)


def circle(r):
    return pi * r ** 2


def checkchoice(operation, side1, side2, side3, r):
    if operation == 1:
        area = square(side, side2)
        dispaly(area)

    elif operation == 2:
        area = triangle(side1, side2, side3)
        display(area)

    elif operation == 3:
        area = rectangle(side1, side2)
    display(area)

    """elif operation == 4:
          area = circle(r)
    display(area)"""

    else:
        print("exiting the programme")

