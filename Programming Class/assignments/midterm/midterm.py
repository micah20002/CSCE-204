# author Micah Lee
import turtle
import random
turtle.setup(575,575)
pen = turtle.Turtle()
turtle.bgcolor("white")
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

colorCar = []
carName = []

# ask user how many cars
carNum = int(turtle.numinput("cars", "Enter how many cars you have: ", 1, 1, 10))

# respective values (add more variables if needed for sizing)
widthPadding = turtle.window_width()/carNum 
width= widthPadding * .8
padding = widthPadding * .1
length = width * 2
bodyHeight = width * 0.2

# controlls how long horizontally
carWidth = width * 1.3
wheelWidth = carWidth * .15
# controls how long vertically
carLength = width * 0.6
backSquare = carLength + carWidth * 1.3
emptySpace = backSquare *2

for car in range(carNum):
    x = - turtle.window_width()/1.01 + carWidth
    y = - turtle.window_height()/1 + padding + car * widthPadding


for i in range(carNum):
    color = turtle.textinput("car color", "Enter Color of Car")
    colorCar.append(color)
    # ask for car name
    name = turtle.textinput("car name", "Enter Name of Car")
    carName.append(name)
    # draw squares
    pen.up()
    pen.setpos(x+ (width - length)/2 + padding + backSquare * i + padding * i, y)
    pen.down()


    pen.color("dark cyan")
    pen.pensize(4)
    pen.fillcolor("medium turquoise")
    pen.begin_fill()
    for i in range(4):
        pen.forward(backSquare)
        pen.left(90)
    pen.end_fill()
    pen.penup()

    #draw cars
    pen.begin_fill()
    for i in range(4):
        pen.up()
        pen.down()
        pen.color("black")
        pen.pensize(4)
        pen.fillcolor(color)
        if i%2== 0:
            pen.forward(carWidth)
        else:
            pen.forward(carLength)
        pen.left(90)
    pen.end_fill()
    pen.penup()

    # draw wheels
    pen.up()
    pen.down()
    pen.color("black")
    pen.pensize(4)
    pen.fillcolor("grey")
    pen.begin_fill()
    pen.circle(wheelWidth)
    pen.end_fill()
    pen.penup()
    # write name above car
    for i in range(4):
        pen.write(name, move=False, align="left", font=("Times",20,"normal"))
    pen.penup()
    for i in range(4):
        pen.setx(-520)
        pen.sety(150)
        pen.write("Car Listings", move=False, align="left", font=("Times",20,"normal"))
    pen.penup()
turtle.done()