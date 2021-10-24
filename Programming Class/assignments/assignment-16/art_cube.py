import turtle, math, random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

width = 120
length = width * math.sqrt(2)

def draw_art_cube(x,y):
    draw_triangle(x - width/3, y - width/3)
    draw_triangle2(x - width, y - length)
    draw_triangle3(x - width, y - length)
    draw_triangle4(x - width, y - length)

def draw_triangle(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()  
    pen.fillcolor("yellow")
    pen.forward(length)
    pen.left(width)
    pen.forward(length)
    pen.left(width)
    pen.forward(length)
    pen.end_fill()

def draw_triangle2(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()  
    pen.fillcolor("red")
    pen.forward(length)
    pen.left(width)
    pen.forward(length)
    pen.left(width)
    pen.forward(length)
    pen.end_fill()

def draw_triangle3(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()  
    pen.fillcolor("blue")
    pen.forward(length)
    pen.left(width)
    pen.forward(length)
    pen.left(width)
    pen.forward(length)
    pen.end_fill()

def draw_triangle4(x,y):
    pen.up()
    pen.setpos(x,y)
    pen.down()  
    pen.fillcolor("green")
    pen.forward(length)
    pen.left(width)
    pen.forward(length)
    pen.left(width)
    pen.forward(length)
    pen.end_fill()

turtle.onscreenclick(draw_art_cube)

turtle.done()