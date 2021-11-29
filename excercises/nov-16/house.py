class House:
    def __init__(self, address, x, y, width, building_color, roof_color, chimney, double_doors, num_windows):
        self.address = address
        self.x = x
        self.y = y
        self.width = width
        self.building_color = building_color
        self.roof_color = roof_color
        self.chimney = chimney
        self.double_doors = double_doors
        self.num_windows = num_windows
        self.style = ("Arial", int(width /4), "bold")

    def draw(self, pen):
        pen.up()
        pen.setpos(self.x- self.width/2, self.y - self.width/2)
        pen.down()
        pen.fillcolor(self.building_color)

        #draw house base
        pen.begin_fill()
        for i in range(4):
            pen.forward(self.width)
            pen.left(90)
        pen.end_fill()

        #draw roof
        roofWidth = self.width *1.2
        pen.up()
        pen.setpos(self.x - roofWidth/2, self.y + self.width/2)
        pen.down()
        pen.fillcolor(self.roof_color)
        pen.begin_fill()
        for i in range(3):
            pen.forward(roofWidth)
            pen.left(120)
        pen.end_fill()


        #optionally draw a chimney
        if self.chimney:
            chimney_width = self.width * .2
            chimney_height = chimney_width * 3
            pen.up()
            pen.setpos(self.x - self.width * .4, self.y + self.width * .7)
            pen.down()
            pen.fillcolor(self.building_color)
            pen.begin_fill()
            for i in range(4):
                if i % 2 == 0:
                    pen.forward(chimney_width)
                else:
                    pen.forward(chimney_height)
                pen.left(90)
            pen.end_fill()
