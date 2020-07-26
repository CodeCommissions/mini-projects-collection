import turtle
import random
import BeginnerProjects
from math import cos, sin, tan, sqrt

class DrawGraph:
    def __init__(self):
        self.color_index = 0

    def setup_turtle(self):
        turtle.clear()
        turtle.speed(0)
        turtle.width(5)

    def draw_line(self, x_start, y_start, x_end, y_end, reset_turtle=True):
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

    def draw_axes(self):
        turtle.width(10)
        turtle.dot()
        turtle.width(5)

        #X axis
        self.draw_line(-400, 0, 400, 0)

        #Y axis
        self.draw_line(0, -400, 0, 400)

    def get_next_color(self):
        colors = ["maroon", "purple", "black", "green", "cyan"]
        bounded_index = self.color_index % len(colors)
        self.color_index += 1
        return colors[bounded_index]

    def draw_scaled_coordinate_pair(self, start_x, start_y, end_x, end_y):
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

        turtle.color(self.get_next_color())
        self.draw_line(start_x, start_y, end_x, end_y, False)

    def draw_graph(self, graph_eq, lower_x, upper_x, step_size):
        last_x = None
        last_y = None

        new_x = lower_x
        while(new_x < upper_x+step_size):
        #for new_x in numpy.arange(lower_x, upper_x+step_size, step_size):
            new_y = graph_eq(new_x)
            self.draw_scaled_coordinate_pair(last_x, last_y, new_x, new_y)
            last_x = new_x
            last_y = new_y

            new_x += step_size

    def tan_cos_sin_equation(self, x):
        return tan(cos(sin(x)))

    def draw_now(self):
        self.setup_turtle()
        self.draw_axes()

        #Just draw a straight diagonal to show how long '1' is on our graph.
        #The function being passed is the same as the equation 'y = x`
        self.draw_graph(lambda x : x, -8, 8, 1)

        #Pass math.cos as an argument.
        self.draw_graph(cos, -8, 8, 0.1)

        #Passing our explicitly defined multi-operation function to be graphed
        self.draw_graph(self.tan_cos_sin_equation, -8, 8, 0.1)

        #And finally, tan, to demo that our long-line-prevention logic serves a purpose
        self.draw_graph(tan, -7.9, 7.9, 0.05)

class DrawGarden:
    def __init__(self, pen=None):
        self.pen = BeginnerProjects.get_default_turtle(pen)
        self.pen.speed(0)

    def draw_now(self):
        total_flowers = 10
        for _ in range(total_flowers):
            x, y = random.randint(-300, 300), random.randint(-300, 300)
            size = random.randint(150, 200)
            self.draw_flower(x, y, size)

    def draw_petals(self, x, y):
        self._teleport_to(x, y)
        sides = 7
        petals = 6
        size = random.randint(40,60)
        self.pen.setheading(random.randint(0, 360))
        for _ in range(petals):
            for _ in range(sides):
                self.pen.forward(size)
                self.pen.left(360 / sides)
            self.pen.left(360 / petals)

    def draw_flower(self, x, y, size):
        self.draw_stem(x, y, size)
        self.draw_petals(x, y)

    def draw_stem(self, x, y, size):
        self._teleport_to(x, y)
        w = self.pen.width()
        self.pen.width(3)
        self.pen.setheading(-90)
        self.pen.forward(size)
        self.pen.width(w)

    def _teleport_to(self, x, y):
        if self.pen.isdown():
            self.pen.penup()
            self.pen.goto(x, y)
            self.pen.pendown()
        else:
            self.pen.goto(x, y)














