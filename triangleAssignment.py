a = int(input("Enter the length of a side: "))
b = int(input("Enter the length of b side: "))
c = int(input("Enter the length of c side: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
