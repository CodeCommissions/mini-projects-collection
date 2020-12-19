import turtle, random

# Setup
pen = turtle.Turtle()
pen.getscreen().bgcolor("grey")
pen.speed(0)


def draw_planet(x, y, size, color, name):
    orbit = (x**2+y**2)**0.5
    pen.up()
    pen.goto(0, -orbit)
    pen.down()
    pen.circle(orbit)

    pen.penup()
    pen.goto(x, y - size)
    pen.pendown()

    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.write(name, align="center", font=("courier", 18, "bold"))


def randomise_turtle(to_randomise):
    to_randomise.shapesize(random.random()+0.2)
    grey = random.random()
    to_randomise.color(grey, grey, grey)


def draw_asteroid_belt(radius):
    offset = 10
    pen.penup()
    pen.goto(0, -radius)
    pen.shape("circle")
    for i in range(100):
        randomise_turtle(pen)
        x_start, y_start = pen.pos()
        x_offset = random.randint(-offset, offset)
        y_offset = random.randint(-offset, offset)
        pen.goto(x_start + x_offset, y_start + y_offset)
        pen.stamp()
        pen.goto(x_start, y_start)
        pen.circle(radius, 3.6)
    pen.pendown()


draw_planet(0, 0, 20, "yellow", "Sun")
draw_planet(0, 55, 10, "dark red", "Mercury")
draw_planet(-50, -60, 18, "orange", "Venus")
draw_planet(120, 20, 20, "light blue", "Earth")
draw_planet(0, -160, 15, "red", "Mars")
draw_planet(-220, 150, 30, "brown", "Jupiter")
draw_planet(190, -230, 28, "goldenrod", "Saturn")
draw_planet(-330, 40, 26, "powder blue", "Uranus")
draw_planet(400, 20, 25, "royal blue", "Neptune")

draw_asteroid_belt(200)

pen.getscreen().exitonclick()
