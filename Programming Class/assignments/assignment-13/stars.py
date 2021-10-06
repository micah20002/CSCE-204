import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
turtle.bgcolor("white")
pen.speed(0)
pen.pensize(2)
pen.width(2)
pen.hideturtle()
colorStar = []



# asking user number of stars
gridSize = int(turtle.numinput("Size", "Enter Number of Stars: ", 1, 1, 10))
widthPadding = turtle.window_width()/gridSize
width= widthPadding * .8
padding = widthPadding * .1

leafWidth = width * .5
appleWidth = leafWidth * .1
stumpWidth = width * .2
stumpHeight = width * .5


for i in range(gridSize):
    color = turtle.textinput("car color", "Enter Color of star").lower().strip() 
    colorStar.append(color)

for row in range(gridSize):
    x = - turtle.window_width()/2 + padding + stumpWidth
    y =  turtle.window_height()/2 - padding - row * widthPadding - stumpHeight

    for col in range(gridSize):
        pen.up()
        pen.setpos(x + (leafWidth - stumpWidth)/2, y)
        pen.down()
        
        #draw star
        pen.color(color)
        for i in range(5):
            pen.forward(width)
            pen.right(144)
            
    x += widthPadding
turtle.done()