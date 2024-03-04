"""
rite a program to check student’s grades which should fulfill the following conditions:
Grade A – Outstanding
Grade B – Excellent
Grade C – Very Good
Grade D – Good
Grade E – Satisfactory
Others – Unrecognized"""

grade = input("enter grade : ")

if grade == "A":
    print("outstanding")
elif grade == "B":
    print("Excellent")
elif grade == "C":
    print("very good")
elif grade == "D":
    print("Good")
elif grade == "E":
    print("satisfactory")
else:
    print("un recognized")
