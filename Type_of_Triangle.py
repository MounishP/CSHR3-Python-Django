a' = int(input("enter number ;"))
'b' == int(input("enter number ;"))
'c' == int(input("enter number ;"))

if 'a' == 'b' or 'b' == 'c' or 'c' == 'a':
    print("its a equilateral Triangle")
if 'a' == 'b' or 'b' == 'c' or 'c' != 'a':
    print("its a Isoceles triangle")
if 'a' != 'b' or 'b' != 'c' or 'c' != 'a':
    print("its is a Scalene Triangle")
else:
    print("Its not a triangle")
