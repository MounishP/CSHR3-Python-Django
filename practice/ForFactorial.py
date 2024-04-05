" Sum of n factorial 1!+2!+3!+4!+.........n!"

n = int(input("enter a number"))
factorial = 1
sum = 0
for i in range(1, n+1):
    factorial = factorial * i
    sum = factorial+sum
print(factorial, sum)
