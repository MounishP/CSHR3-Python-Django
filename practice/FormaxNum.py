"""Write a program that enters n integers (n > 0) and finds the max among them"""
n = int(input("enter integers: "))
max = 0
for i in range(n):
    num = int(input())
    if num > max:
        max = num

print("max of number", max)

