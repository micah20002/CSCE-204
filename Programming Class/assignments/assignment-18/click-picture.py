import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

def draw_scene(x,y):
    draw_sun(x,y)
    draw_cloud(x,y)
    draw_trees(x,y)

def draw_sun(x,y):
    if x > 150 and y > 200:
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.fillcolor("yellow")
        pen.begin_fill()
        pen.circle(30)
        pen.end_fill()

def draw_cloud(x,y):
    if x < 100 and y > 200:
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.fillcolor("blue")
        pen.begin_fill()
        pen.circle(15)
        pen.end_fill()
        pen.penup()
        pen.forward(20)
        pen.begin_fill()
        pen.circle(20)
        pen.end_fill()
        pen.penup()
        pen.begin_fill()
        pen.forward(20)
        pen.circle(15)
        pen.end_fill()
        pen.penup()

def draw_trees(x,y):
    if y < 100:
        pen.color("green")
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.begin_fill()
        for i in range(3):
            pen.forward(50)
            pen.left(120)
        pen.end_fill()
        pen.color("brown")
        pen.fillcolor("brown")
        pen.up()
        pen.setpos(x + 25,y - 25)
        pen.down()
        pen.begin_fill()
        for i in range(4):
            pen.forward(12)
            pen.left(90)
            pen.forward(12)
        pen.end_fill()


turtle.onscreenclick(draw_scene)

turtle.done()