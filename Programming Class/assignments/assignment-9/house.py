# Author: Micah Lee

import turtle
turtle.setup(1500,1500)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("medium slate blue")
shapeWidth = 150
topTriangle = shapeWidth * 1.2
pedals = shapeWidth *.2
star = shapeWidth * .4



pen.up()
pen.begin_fill()
pen.setpos(-shapeWidth/2, -shapeWidth/2)
pen.down()

# square
for i in range(4):
        pen.forward(shapeWidth)
        pen.left(90)
pen.end_fill()

# roof
pen.setheading(0)
pen.fillcolor("salmon")
pen.up()
pen.begin_fill()
pen.setpos(-shapeWidth/1.7, shapeWidth/2)
pen.down()
# square
for i in range(3):
        pen.forward(topTriangle)
        pen.left(120)
pen.end_fill()

# flower stem
pen.up()
pen.setpos(250,-155)
pen.pensize(15)
pen.color("purple")
pen.down()
pen.left(90)
pen.forward(145)

# flower pedals
pen.color("lightpink")
pen.fillcolor("violet")
pen.up()
pen.pensize(3)
pen.begin_fill()
pen.setpos(250,-20)
pen.down()

# pedals
for i in range(4):
        pen.circle(pedals)
        pen.left(90)


pen.end_fill()

# center of flower

pen.color("lightpink")
pen.fillcolor("violet")
pen.up()
pen.pensize(3)
pen.begin_fill()
pen.setpos(285,-20)
pen.down()

pen.circle(35)

pen.end_fill()


# star
pen.color("yellow")
pen.up()
pen.pensize(4)
pen.setpos(-150,200)
pen.down()
# star
for i in range(5):
        pen.forward(star)
        pen.left(144)

turtle.done()