import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()


def draw_picture(x,y):
    drawStar(x,y)
    drawTriangle(x,y)
    drawCloud(x,y)
    drawRainbow(x,y)

def getScene():
    sceneShapes = []
    with open("excercises/nov-02/scene.txt") as file: 
        for line in file:
            sceneShape = line.replace("\n", "").strip().lower()
            sceneShapes.append(sceneShape)
        return sceneShapes

def drawStar(x, width):
    pen.up()
    pen.setpos(-turtle.window_width()/2)
    pen.down()
    pen.fillcolor("yellow")
    pen.begin_fill()
    for i in range(5):
        pen.forward(250)
        pen.left(144)
pen.end_fill()  

def drawTriangle(x,y,size):
    pen.fillcolor("yellow")
pen.begin_fill()
for i in range(5):
    pen.forward(250)
    pen.left(144)
pen.end_fill()   


def drawCloud(x,width):
    pen.fillcolor("yellow")
pen.begin_fill()
for i in range(5):
    pen.circle(15)
    pen.end_fill()
    pen.penup()
    pen.forward(20)
    pen.circle(20)
    pen.left(144)
    pen.end_fill()
    pen.up()
    pen.fillcolor("blue")
    pen.up()



def drawRainbow(x,width):
    pen.begin_fill()
    pen.end_fill()


pen.circle(100,'red')
pen.circle(95,'orange')
pen.circle(90,'yellow')
pen.circle(85,'green')
pen.circle(80,'blue')
pen.circle(75,'indigo')
pen.circle(70,'violet')



turtle.onscreenclick(draw_picture)
turtle.done()