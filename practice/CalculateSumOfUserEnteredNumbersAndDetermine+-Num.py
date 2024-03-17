"""What's the process to calculate the sum of
numbers until the user enters them, and how can I determine the sum of
positive and negative numbers separately?

calculate the sum of numbers until user enters them
determine sum of positive and negative numbers seperately
"""

i = 0
psum = 0
nsum = 0
while i <= 10:
    num = int(input(" Enter Number:"))
    i = i + 1
    if num>=0 :
        psum = num + psum
        print("its a positive number")
    else:
        nsum = num + nsum
        print("its a negative number")

print( "sum of pnumbers :", psum)
print("sum of nnumbers : ", nsum)




