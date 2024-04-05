n = int(input("enter number"))
square = 1
sum = 0
for i in range(1, n+1):
    square = i*i
    sum = square+sum

print(square, sum)