import turtle

pen = turtle.Turtle()


def draw_planet(x, y, size):
    pen.penup()
    pen.goto(x, y-size)
    pen.pendown()
    pen.circle(size)


draw_planet(0, 0, 50)
draw_planet(60, 60, 10)

pen.getscreen().exitonclick()
