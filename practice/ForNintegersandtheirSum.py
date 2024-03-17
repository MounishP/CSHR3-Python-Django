""" Write a program that reads n integers and finds their sum"""

n = int(input("enter numbers"))
sum = 0
for i in range(n):
     num = int(input())
     sum = sum + num
print(" sum of integers : ", sum)

