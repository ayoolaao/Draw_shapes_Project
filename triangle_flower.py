import turtle


def draw_triangle(tri):

    for i in range(0, 3):
        tri.color("red")
        tri.right(120)
        tri.forward(100)


def draw_triangle1(tri):

    for i in range(0, 3):
        tri.color("blue")
        tri.forward(50)
        tri.right(120)


def draw_flower():

    win = turtle.Screen()
    win.bgcolor("white")

    ayo = turtle.Turtle()
    ayo.speed(0.5)
    for i in range(0, 36):
        draw_triangle(ayo)
        draw_triangle1(ayo)
        ayo.right(10)


    win.exitonclick()


draw_flower()