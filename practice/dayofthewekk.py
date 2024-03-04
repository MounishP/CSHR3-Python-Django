"""
Write a program that prints the day of the week depending on the given number (1 as Monday … 7 as Sunday)
or "Error!" if invalid input is given
"""
day = int(input("Enter the day : "))

if day == 1:
    print("monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
elif day == 7:
    print("sunday")
else:
    print("enter the numbers in between 1 to 7")
