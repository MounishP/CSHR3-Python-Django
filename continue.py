"""
WAPP print numbers from 1 to 10 but if there is a 5 in the numbers dont print it
"""

for number in range(1, 11):
    if number == 5:
        continue
    else:
        print(number)
