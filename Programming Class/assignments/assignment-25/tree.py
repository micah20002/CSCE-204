


class Tree:
    def __init__(self, x, y, height, color):
        self.x = x
        self.y = y
        self.height = height
        self.color = color
        self.style = ("Arial", int(height /4), "bold")

    def draw(self, pen):
        pen.up()
        pen.setpos(self.x- self.height/2, self.y - self.height/2)
        pen.down()
        pen.fillcolor("brown")

        #draw tree trunk
        pen.begin_fill()
        for i in range(4):
            pen.forward(self.height/2)
            pen.left(90)
        pen.end_fill()

        pen.up()
        pen.setpos(self.x - self.height/1.2, self.y + self.height/24)
        pen.down()
        pen.fillcolor(self.color)
        pen.begin_fill()
        for i in range(3):
            pen.forward(self.height)
            pen.left(120)
        pen.up()
        pen.sety(pen.ycor() + self.height/2)
        pen.down()
        for i in range(3):
            pen.forward(self.height/1.2)
            pen.left(120)
        pen.up()
        pen.sety(pen.ycor() + self.height/2)
        pen.down()
        for i in range(3):
            pen.forward(self.height/1.4)
            pen.left(120)
        pen.end_fill()