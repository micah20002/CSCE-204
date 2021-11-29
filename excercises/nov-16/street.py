from house import House
import turtle
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

houses = []
houses.append(House("1 A Street", -200,0,50, "medium aquamarine", "hot pink", True, True, 3))
houses.append(House("2 A Street", -300,0,50, "yellow", "hot pink", True, True, 3))

for house in houses:
    house.draw(pen)

turtle.done()