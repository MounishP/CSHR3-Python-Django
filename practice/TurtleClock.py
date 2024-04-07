import time
import turtle

screen = turtle.Screen()
screen.title("Analog clock")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# create a pen
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(0)


def clock(pen, h, m, s):
    # base
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("magenta")
    pen.down()
    pen.circle(210)

   # hour lines
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    for i in range(12):
        pen.forward(190)
        pen.down()
        pen.forward(20)
        pen.up()
        pen.goto(0, 0)
        pen.right(30)

    # Hour Hand
    pen.color("red")
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.right(angle)
    pen.down()
    pen.forward(80)

    # Min Hand
    pen.color("blue")
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.right(angle)
    pen.down()
    pen.forward(150)

    # Second Hand
    pen.color("green")
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.right(angle)
    pen.down()
    pen.forward(180)


while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    clock(pen,h, m, s)
    screen.update()
    pen.clear()