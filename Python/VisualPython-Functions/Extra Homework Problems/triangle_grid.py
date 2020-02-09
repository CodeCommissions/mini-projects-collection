import turtle
from numpy import arccos, degrees

def setup_turtle():
    turtle.clear()
    turtle.speed(0)
    turtle.width(5)

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

def draw_row(total_triangle):
    for x in range(0, 2):
        for y in range(0, total_triangle):
            turtle.color(get_next_color())
            draw_triangle(60, 85, 60)
            turtle.forward(60)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)

setup_turtle()
end = 6
for i in range(end + 1):
    draw_row(end+1)
    if(i == end):
        break
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)

turtle.exitonclick()
