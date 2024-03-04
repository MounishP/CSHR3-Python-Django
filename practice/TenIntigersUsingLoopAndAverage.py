"""How can I take 10 integers from the keyboard
using a
loop and print their average value on the screen?"""

"""numbers = int(input(" Enter ten integers : "))

i = 1

while i <= 10:
    print(f"{i}")"""

sum = 0
i = 10

while i > 0:
    num = int(input("Enter an integer: "))
    if num > 10:
        print("Number entered is greater than 10. Exiting the loop.")
        break
    sum = sum + num
    i = i - 1

if i == 0:
    print("The average value is:", sum / 10.0)
