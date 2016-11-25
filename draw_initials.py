import turtle


def draw_initials():

    windows = turtle.Screen()
    windows.bgcolor("#D9742A")

    a = turtle.Turtle()
    a.color("#D9742A")
    a.right(180)
    a.forward(200)
    a.color("black")
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.color("black")

    a.right(180)
    a.forward(200)
    a.right(90)
    a.forward(100)
    a.right(90)
    a.forward(200)
    a.color("#D9742A")

    a.left(90)
    a.forward(50)
    a.color("black")
    a.left(90)
    a.forward(200)
    a.left(180)
    a.forward(100)
    a.left(90)
    a.forward(100)
    a.left(90)
    a.forward(100)

    windows.exitonclick()


draw_initials()