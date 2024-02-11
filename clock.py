import turtle

screen = turtle.Screen()
screen.title("Analog clock")
screen.setup(width=600, height=600)
screen.bgcolor("white")

# create a pen
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(1)


def clock():
    pass


while True:
    screen.update()
