import turtle
import numpy
from math import cos, sin, tan, sqrt

def setup_turtle():
    turtle.clear()
    turtle.speed(0)
    turtle.width(5)

def draw_line(x_start, y_start, x_end, y_end, reset_turtle=True):
    '''
    Draws a line between 2 sets of turtle coordinates.
    Resetting the turtle returns it to wherever it was before the draw
    line function was called.
    '''
    turtle_start = turtle.position()
    turtle.up()
    turtle.setpos(x_start, y_start)
    turtle.down()

    turtle.setpos(x_end, y_end)

    if(reset_turtle):
        turtle.up()
        turtle.setpos(turtle_start)
        turtle.down()

def draw_axes():
    turtle.width(10)
    turtle.dot()
    turtle.width(5)

    #X axis
    draw_line(-400, 0, 400, 0)

    #Y axis
    draw_line(0, -400, 0, 400)

color_index = 0
def get_next_color():
    global color_index
    colors = ["maroon", "purple", "black", "green", "cyan"]
    bounded_index = color_index % len(colors)
    color_index += 1
    return colors[bounded_index]

def draw_scaled_coordinate_pair(start_x, start_y, end_x, end_y):
    #Make sure you don't try to draw None as a coordinate
    if(None in [start_x, start_y, end_x, end_y]):
        return

    x_scale = 50
    y_scale = 50

    start_x *= x_scale
    start_y *= y_scale
    end_x *= x_scale
    end_y *= y_scale

    #An optional way of ensuring that VERY far apart coordinates don't get connected
    #This is good when 2 positions are on opposite sides of an infinite point (like tan(90))
    distance = sqrt((start_x-end_x)**2 + (start_y-end_y)**2)
    if(distance >= 800):
        return

    turtle.color(get_next_color())
    draw_line(start_x, start_y, end_x, end_y, False)

def draw_graph(graph_eq, lower_x, upper_x, step_size):
    last_x = None
    last_y = None
    for new_x in numpy.arange(lower_x, upper_x+step_size, step_size):
        new_y = graph_eq(new_x)
        draw_scaled_coordinate_pair(last_x, last_y, new_x, new_y)
        last_x = new_x
        last_y = new_y

def tan_cos_sin_equation(x):
    return tan(cos(sin(x)))

setup_turtle()
draw_axes()

#Just draw a straight diagonal to show how long '1' is on our graph.
#The function being passed is the same as the equation 'y = x`
draw_graph(lambda x : x, -8, 8, 1)

#Pass math.cos as an argument.
draw_graph(cos, -8, 8, 0.1)

#Passing our explicitly defined multi-operation function to be graphed
draw_graph(tan_cos_sin_equation, -8, 8, 0.1)

#And finally, tan, to demo that our long-line-prevention logic serves a purpose
draw_graph(tan, -7.9, 7.9, 0.05)

turtle.exitonclick()