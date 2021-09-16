import turtle
turtle.setup(1500,1500)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(30)
pen.color("sienna")
pen.fillcolor("sienna")
treeHeight = 300
topTriangle = treeHeight * .2
middleTriangle = treeHeight * .3
bottomTriangle = treeHeight *.5
trunk = treeHeight * .2

# set initial position
pen.up()
pen.setpos(-trunk / 2, -treeHeight / 2)
pen.down()

# draw trunk
pen.begin_fill()
for i in range(4):
    pen.forward(trunk)
    pen.left(90)
pen.end_fill()

# set position for bottom triangle
pen.up()
pen.setpos(-bottomTriangle/2, -treeHeight/2 + trunk)
pen.down()
pen.fillcolor("forest green")
pen.color("forest green")

# draw bottom triangle
pen.begin_fill()
for i in range(4):
    pen.forward(bottomTriangle)
    pen.left(120)
pen.end_fill()


turtle.done()