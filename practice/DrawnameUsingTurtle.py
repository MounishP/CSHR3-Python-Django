import turtle

screen = turtle.Screen()
screen.title("my name")
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.tracer(0)

pen = turtle.Turtle()
pen.pensize(3)
pen.speed(0)
pen.up()

pen.goto(0, 120)
pen.setheading(180)
pen.forward(200)
pen.down()
pen.forward(50)
pen.setheading(270)
pen.forward(50)
pen.setheading(360)
pen.forward(50)
pen.setheading(270)
pen.forward(50)
pen.right(90)
pen.forward(50)
pen.up()

pen.goto(0, 120)
pen.forward(150)
pen.setheading(270)
pen.down()
pen.forward(100)
pen.up()
pen.backward(50)
pen.setheading(360)
pen.down()
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.setheading(270)
pen.forward(100)
pen.up()

pen.goto(0,125)
pen.forward(10)
pen.setheading(250)
pen.down()
pen.forward(100)
pen.up()
pen.goto(-3,115)
pen.setheading(290)
pen.down()
pen.forward(100)
pen.up()
pen.backward(50)
pen.setheading(180)
pen.down()
pen.forward(30)

pen.up()
pen.goto(0,125)
pen.setheading(360)
pen.forward(100)
pen.setheading(270)
pen.down()
pen.forward(100)
pen.up()
pen.backward(100)
pen.setheading(310)
pen.down()
pen.forward(125)
pen.setheading(90)
pen.forward(100)
pen.up()

pen.goto(200,130)
pen.setheading(270)
pen.down()
pen.forward(100)
pen.backward(50)
pen.setheading(320)
pen.forward(80)
pen.backward(80)
pen.setheading(50)
pen.forward(80)












"""def myname(pen, s, h, a, n, k):
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("green")
    pen.down()
    pen.circle(210)"""






while True:
    screen.update()