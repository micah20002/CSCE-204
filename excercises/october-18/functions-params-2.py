import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(0)
pen.hideturtle()

def draw_square(x, y, width, color):
    draw_rec(x,y,width,width, color)

def draw_rec(x,y, width, height,color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(color)

    pen.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            pen.forward(width)
        else:
            pen.forward(height)
        pen.left(90)
    pen.end_fill()

def draw_triangle(x,y,width, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

def draw_house(x,y,width, baseColor, roofColor, doorColor):
    roofPadding = width/10
    doorHeight = width/2
    doorWidth = doorHeight/2
    draw_square(x - width/2,y- width/2, width, baseColor)
    draw_triangle(x-width/2-roofPadding/2,y +width/2,width +roofPadding, roofColor)
    draw_rec(x-doorWidth/2,y-width/2,doorWidth,doorHeight, doorColor)

#draw_house(50,50,100, "red", "yellow", "blue")

for i in range(10):
    x = random.randint(-int(turtle.window_width()/2), int(turtle.window_width()/2))
    y = random.randint(-int(turtle.window_height()/2), int(turtle.window_height()/2))
    size = random.randint(20,80)
    draw_house(x,y,size, "red", "yellow", "blue")

turtle.done()