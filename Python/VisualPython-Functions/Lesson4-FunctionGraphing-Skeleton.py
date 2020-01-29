import turtle
import numpy

def setup_turtle():
    turtle.clear()
    turtle.speed(0)
    turtle.width(5)

def draw_axes():
    pass

def draw_graph():
    for x in numpy.arange(start, stop, step_size):
		pass

def get_y_value(x):
    pass

def draw_line(x_start, y_start, x_end, y_end, reset_turtle=True):
    pass

def draw_scaled_coordinate_pair(start_x, start_y, end_x, end_y):
    turtle.color(get_next_color())

color_index = 0
def get_next_color():
    global color_index
    colors = ["maroon", "purple", "black", "green", "cyan"]
    bounded_index = color_index % len(colors)
    color_index += 1
    return colors[bounded_index]

setup_turtle()
draw_axes()
draw_graph()

turtle.exitonclick()