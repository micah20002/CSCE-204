# author Micah Lee

import turtle

turtle.bgcolor("skyblue")
 
pen = turtle.Turtle()
 
pen.pensize(10)
pen.speed(0)
 
# grass

pen.color ("medium sea green")
pen.fillcolor ("medium seagreen")

pen.up()
pen.setpos(-turtle.window_width()/2, -turtle.window_height()/2)
pen.down()

pen.begin_fill()
pen.forward(turtle.window_width())
pen.left(90)
pen.forward(turtle.window_height()/4)
pen.left(90)
pen.forward(turtle.window_width())
pen.left(90)
pen.forward(turtle.window_height()/4)
pen.left(90)
pen.end_fill()

# tree trunk
pen.setheading(0)
pen.up()
pen.setpos(-70,70)
pen.down()
pen.color ("sienna")
pen.fillcolor ("sienna")
pen.begin_fill()
pen.forward(100) #top of trunk
pen.right(90)
pen.forward(300) # right side
pen.right(90)
pen.forward(100) # bottom of trunk
pen.right(90)
pen.forward(300) # left side
pen.right(90)
pen.end_fill()




# tree leaves

pen.setheading(0)
pen.up()
pen.setpos(-90,40)
pen.down()
pen.color ("dark green")
pen.fillcolor ("dark green")
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# another leaf

pen.setheading(0)
pen.up()
pen.setpos(-20,70)
pen.down()
pen.color ("dark green")
pen.fillcolor ("dark green")
pen.begin_fill()
pen.circle(125)
pen.end_fill()

# another leaf
pen.setheading(0)
pen.up()
pen.setpos(50,40)
pen.down()
pen.color ("dark green")
pen.fillcolor ("dark green")
pen.begin_fill()
pen.circle(100)
pen.end_fill()


# apples

pen.setheading(0)
pen.up()
pen.setpos(50,70)
pen.down()
pen.color ("red")
pen.fillcolor ("red")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# stem
pen.setheading(0)
pen.up()
pen.setpos(50,95)
pen.down()
pen.color ("sienna")
pen.left(50)
pen.forward(5)

# second apple
pen.setheading(0)
pen.up()
pen.setpos(-80,110)
pen.down()
pen.color ("red")
pen.fillcolor ("red")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# stem
pen.setheading(0)
pen.up()
pen.setpos(-80,135)
pen.down()
pen.color ("sienna")
pen.left(50)
pen.forward(5)


# third apple
pen.setheading(0)
pen.up()
pen.setpos(10,150)
pen.down()
pen.color ("red")
pen.fillcolor ("red")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# stem
pen.setheading(0)
pen.up()
pen.setpos(10,175)
pen.down()
pen.color ("sienna")
pen.left(50)
pen.forward(5)
pen.end_fill()


# fourth apple
pen.setheading(0)
pen.up()
pen.setpos(-60,210)
pen.down()
pen.color ("red")
pen.fillcolor ("red")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# stem
pen.setheading(0)
pen.up()
pen.setpos(-60,235)
pen.down()
pen.color ("sienna")
pen.left(50)
pen.forward(5)
pen.end_fill()

# fifth apple
pen.setheading(0)
pen.up()
pen.setpos(80,155)
pen.down()
pen.color ("red")
pen.fillcolor ("red")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# stem
pen.setheading(0)
pen.up()
pen.setpos(80,180)
pen.down()
pen.color ("sienna")
pen.left(50)
pen.forward(5)
pen.end_fill()


# stems




turtle.done()