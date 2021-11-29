from tree import Tree
import turtle
turtle.setup(575,575)
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

trees = []
trees.append(Tree(-200,0,50, "medium aquamarine"))
trees.append(Tree(-300,-100,85, "yellow"))
trees.append(Tree(275,55,105, "red"))
trees.append(Tree(100,270,25, "orange"))
trees.append(Tree(315,115,35, "blue"))
trees.append(Tree(70,80,95, "beige"))
trees.append(Tree(40,12,125, "blueviolet"))
trees.append(Tree(105,95,40, "aliceblue"))
trees.append(Tree(-115,250,50, "burlywood1"))
trees.append(Tree(-250,220,55, "black"))
trees.append(Tree(300,-200,75, "peru"))
trees.append(Tree(220,175,105, "yellowgreen"))
trees.append(Tree(-210,50,115, "light pink"))
trees.append(Tree(170,80,35, "light goldenrod yellow"))
trees.append(Tree(150,15,54, "light coral"))
trees.append(Tree(20,210,50, "medium spring green"))
trees.append(Tree(50,205,15, "indian red"))
trees.append(Tree(88,360,77, "medium slate blue"))
trees.append(Tree(145,90,80, "rosy brown"))
trees.append(Tree(129,10,90, "deep pink"))


for tree in trees:
    tree.draw(pen)

turtle.done()