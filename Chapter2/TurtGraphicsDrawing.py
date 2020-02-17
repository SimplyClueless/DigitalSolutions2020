import turtle
turtle.showturtle()
turtle.speed(10)
turtle.bgcolor("blue")

def makesquare():
    turtle.fillcolor("white")
    turtle.begin_fill()
    for x in range (4):
        turtle.forward(90)
        turtle.right(90)
    turtle.end_fill()

turtle.right(45)
makesquare()
turtle.left(180)
makesquare()

turtle.done()
