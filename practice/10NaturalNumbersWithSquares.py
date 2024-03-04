""" Can you print 10 natural numbers along with their squares?"""
i = 1
n = int(input("Enter Number: "))

while i < n:
    sq = i * i
    i = i + 1
    print(f"Square of {i} :", sq)

