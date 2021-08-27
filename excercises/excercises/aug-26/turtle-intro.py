import turtle
 
turtle.bgcolor("skyblue")
 
pen = turtle.Turtle()
 
pen.pensize(10)
pen.speed(0)
 
# draw a square
pen.begin_fill()
pen.color("red")
pen.fillcolor("green")
pen.forward(300)
pen.left(90)
pen.forward(300)
pen.left(90)
pen.forward(300)
pen.left(90)
pen.forward(300)
pen.end_fill()
pen.penup()
 
# draw a circle
pen.setpos(-200,300)
pen.pendown()
pen.circle(50)
pen.penup()
 
# draw a triangle
pen.setheading(-90)
pen.forward(400)
pen.down()
pen.setheading(0)
pen.color("yellow")
pen.begin_fill()
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.left(120)
pen.forward(100)
pen.end_fill()
 
# backwards triangle
pen.penup()
pen.setpos(300,-400)
pen.pendown()
pen.color("blue")
pen.setheading(0)
pen.forward(-100)
pen.right(120)
pen.forward(-100)
pen.right(120)
pen.forward(-100)
 
 
turtle.done()