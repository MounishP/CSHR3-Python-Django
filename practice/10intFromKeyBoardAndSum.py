"""Take 10 integers from keyboard using loop and print their average value on the screen."""

i = 1
Sum = 0
avg = 0
while i <= 10:
    int = input("Enter Number")
    if Sum <= 10:
        Sum = Sum+i
        i=i+1
        avg = Sum / 10
    print("sum of the integer", (int), ":", Sum, "avg of the integer", (int), ":", avg)