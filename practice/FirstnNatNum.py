"""Sum of First n Natural Numbers"""

i = 1
sum = 0
n = int(input("enter n: "))
while i <= n:
    sum = sum + i
    i = i + 1
    print("sum of n :", sum)


n