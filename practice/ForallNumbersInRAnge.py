""" Write a program that finds all numbers in the range [1 … 1000], that end in 7."""

for num in range(1, 1000):
     if num % 10 == 7:
        print(num)