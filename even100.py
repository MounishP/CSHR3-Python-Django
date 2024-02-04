"""
WAPP to print only the even numbers from 1 to 100
1. get numbers from 1 to 100
2. get a single number from the range of 100
3. check if the that number is even or not
4. print the number only if it is even
"""

for number in range(1,101):    #number = 1,2
    if number % 2 == 0:        # 2 % 2
        print(number)          #2