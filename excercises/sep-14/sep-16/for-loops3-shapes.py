import turtle
turtle.setup(1500,1500)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("pink")
shapeWidth = 200
shape= turtle.textinput("Shape", "Enter Shape").lower().strip()

pen.up()
pen.setpos(-shapeWidth/2, -shapeWidth/2)
pen.down()

if shape == "square":
    for i in range(4):
        pen.forward(shapeWidth)
        pen.left(90)

elif shape == "triangle":
    for i in range(3):
        pen.forward(shapeWidth)
        pen.left(120)

else:
    print("invalid shape")



turtle.done()