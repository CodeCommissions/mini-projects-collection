import turtle

def setup_turtle():
    turtle.clear()
    turtle.speed(0)
    turtle.width(5)

def draw_square(size, extra_angle):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.left(extra_angle)

color_index = 0
def get_next_color():
    global color_index
    colors = ["maroon","Dark Orange","purple","black","midnight blue", "firebrick","dark green"]
    bounded_index = color_index % len(colors)
    color_index += 1
    return colors[bounded_index]

setup_turtle()
for i in range(100):
    turtle.color(get_next_color())
    draw_square(200,33)

turtle.exitonclick()

































