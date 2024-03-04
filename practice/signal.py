"""
Write a python program that will check for the following conditions:
If the light is green– Car is allowed to go.
If the light is yellow – Car has to wait.
If the light is red – Car has to stop.
"""
light = input("give the required signal : ")

if light == "Green":
    print("Car is allowed to go")
elif light == "yellow":
    print("car has to wait")
elif light == "red":
    print("car has to stop")
else:
    print("give valid signal")