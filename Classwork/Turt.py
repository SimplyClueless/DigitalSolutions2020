import turtle
turtle.showturtle()
turtle.speed(1000000000000000000000000000000000)
turtle.bgcolor("blue")

def star_seven(size, sides):
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    for x in range (7):
        turtle.forward(size)
        angle = 180.0 - 180.0 / sides
        turtle.right(angle)
    turtle.end_fill()

turtle.penup()
turtle.goto(100, -30)
turtle.pendown()
turtle.right(180)
star_seven(100, 7)
turtle.penup()
turtle.goto(120, 60)
turtle.pendown()
star_seven(20, 5)
turtle.penup()
turtle.goto(200, 120)
turtle.pendown()
star_seven(60, 7)
turtle.penup()
turtle.goto(60, 220)
turtle.pendown()
star_seven(60, 7)
turtle.penup()
turtle.goto(-40, 100)
turtle.pendown()
star_seven(50, 7)

turtle.done()

