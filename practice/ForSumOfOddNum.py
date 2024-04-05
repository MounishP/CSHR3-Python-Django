n = int(input("Enter Number: "))
sod = 0
for i in range(0, n + 1):
    if i%2 != 0:
        sod = sod + i
        print(sod)

