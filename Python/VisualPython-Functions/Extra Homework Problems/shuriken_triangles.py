import turtle
from numpy import arccos, degrees

def setup_turtle():
    turtle.clear()
    turtle.speed(3)
    turtle.width(5)

colors = ["maroon", "purple", "black", "green", "cyan"]
def draw_triangle(edge1, edge2 = None, edge3 = None):
    if (edge2 is None or edge3 is None):
        edge2 = edge1
        edge3 = edge1

    #Remember where we started
    start_pos = turtle.position()
    start_angle = turtle.heading()

    #Work out how much the turtle should turn
    temp = (edge1**2 + edge2**2 - edge3**2)/(2*edge1*edge2)
    radians = arccos(temp)
    angle = degrees(radians)

    #Move, turn based on that angle, then move the next length
    turtle.forward(edge1)
    turtle.right(180 - angle)
    turtle.forward(edge2)

    #Reset
    turtle.goto(start_pos)
    turtle.setheading(start_angle)

color_index = 0
def get_next_color():
    global color_index
    colors = ["maroon","Dark Orange","purple","black","midnight blue", "firebrick","dark green"]
    bounded_index = color_index % len(colors)
    color_index += 1
    return colors[bounded_index]

setup_turtle()
for i in range(1,17):
    turtle.color(get_next_color())
    draw_triangle(i*10, i*15, i*20)
    turtle.left(120)

turtle.exitonclick()
