import turtle

turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")


for i in range(100):
    starWidth = random.randint(20,80)
    pen.color(colors[i%len(colors)])
    pen.fillcolor(colors[i%len(colors)])
    x = random.randint(-int(turtle.window_width()/2), int)

turtle.done()