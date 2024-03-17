"""How do I find the sum of odd and even numbers separately within a given range?"""
""" range, even, odd, sum of even and odd """

start = int(input("starting range"))
end = int(input("ending range"))
evensum = 0
oddsum = 0
while start <= end:
    if start % 2 == 0:
        evensum = evensum + start
    else:
        oddsum = oddsum + start

    start = start + 1
print("sum of evennumber :", evensum, "sum od oddsum: ", oddsum )