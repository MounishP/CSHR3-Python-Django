"""There are given n integers a1, a2, …, an. Calculate the sums:
sum1 = a1 + a4 + a7 + … (the numbers are summed, starting from the first one with step of 3).
sum2 = a2 + a5 + a8 + … (the numbers are summed, starting from the second one with step of 3).
sum3 = a3 + a6 + a9 + … (the numbers are summed, starting from the third one with step of 3). """
n = int(input("enter n: "))
sum1 = 0
sum2 = 0
sum3 = 0
for i in range(1,n+1,3):
    sum1 = sum1+i
for i in range(2,n+1,3):
    sum2 = sum2+i
for i in range(3,n+1,3):
    sum3 = sum3+i
print(sum1, sum2, sum3)

