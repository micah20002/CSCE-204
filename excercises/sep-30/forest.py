import turtle
import random

turtle.setup(575,575)
pen = turtle.Turtle()
turtle.bgcolor("burlywood")
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

gridSize = int(turtle.numinput("Size", "Enter Size: ", 5, 1, 10))
widthPadding = turtle.window_width()/gridSize
width= widthPadding * .8
padding = widthPadding * .1

leafWidth = width * .5
appleWidth = leafWidth * .1
stumpWidth = width * .2
stumpHeight = width * .5

for row in range(gridSize):
    x = - turtle.window_width()/2 + leafWidth
    y = - turtle.window_height()/2 + padding + row * widthPadding

    for col in range(gridSize):
        pen.up()
        pen.setpos(x + (leafWidth - stumpWidth)/2, y)
        pen.down()
        
        #stump
        pen.color("sienna")
        pen.begin_fill()
        for i in range(4):
            if i%2== 0:
                pen.forward(stumpWidth)
            else:
                pen.forward(stumpHeight)
            pen.left(90)
        pen.end_fill()
        #create leaves
        pen.color("forest green")
        pen.up()
        pen.setpos(x + leafWidth /2, y + stumpHeight * .8)
        pen.down()
        pen.begin_fill()
        pen.circle(leafWidth/2)
        pen.end_fill()

        # apples
        for i in range(5):
            appleX = random.randint(int(x), int(x + leafWidth - appleWidth))
            appleY = random.randint(int(y + stumpHeight * .8), int(y + stumpHeight * .8 + leafWidth - appleWidth))
            pen.up()
            pen.setpos(appleX, appleY)
            pen.down()
            pen.color("crimson")
            pen.begin_fill()
            pen.circle(appleWidth/2)
            pen.end_fill()
        x += widthPadding
turtle.done()