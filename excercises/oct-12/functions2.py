import turtle
import random

turtle.setpos(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def draw_square():
    length = 50
    x= random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2)- length)
    y= random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2)- length)

    pen.up()
    pen.setpos(x,y)
    pen.down()

    for i in range(4):
        pen.forward(length)
        pen.left(90)

def draw_triangle():
    length = 50
    x= random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2)- length)
    y= random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2)- length)

    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.setheading(0)
    for i in range(3):
        pen.forward(length)
        pen.left(120)

for i in range(10):
    choice = random.randint(0,1)

    if choice == 0:
        draw_triangle()
    else:
        draw_square()

turtle.done()