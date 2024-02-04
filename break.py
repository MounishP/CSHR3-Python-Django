"""
WAPP print numbers from 1 to 10 but if there is a 5 in the numbers stop the loop
"""

print("program started")

for number in range(1, 11):
    if number == 5:
        break
    else:
        print(number)

print("program ended")