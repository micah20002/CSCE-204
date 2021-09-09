import turtle
turtle.setup(1500,1500)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("pink")

shape = turtle.textinput("Shapes","Enter Shape: ").lower().strip()
shapeSize = turtle.window_width()/4

if shape == "circle" :
    pen.circle(200)
elif shape == "square":
 pen.up()
pen.setpos(0, shapeSize/2)
pen.down()
pen.forward(250)
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(250)
pen.left(90)
pen.end_fill()
elif shape == "triangle":
pen.up()
pen.setpos(0, shapeSize/2)
pen.down()
pen.begin_fill()
pen.forward(300)
pen.left(120)
pen.forward(300)
pen.left(120)
pen.forward(300)
pen.left(120)
pen.forward(300)
pen.left(120)
pen.end_fill()


turtle.done()