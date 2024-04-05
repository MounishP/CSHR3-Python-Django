n = int(input("enter number: "))
product = 1
for i in str(n):

    reminder = n%10
    product = product*reminder
    n = n//10

print(product)