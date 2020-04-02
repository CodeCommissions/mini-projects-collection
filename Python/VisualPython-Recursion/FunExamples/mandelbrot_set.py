#This is a very basic implenetation of the Mandelbrot set.
#This beautiful, and infinite, set of numbers is ill-suited
#to the Python Turtle simply because you have to draw 
#1 pixel at a time (which is *very* slow with the Turtle)

#https://en.wikipedia.org/wiki/Mandelbrot_set

#This code was submitted as a course project, and credit goes
#to Mel Methmod. This is beyond the expected complexity level
#for our intro to recursion project.

import turtle
from math import sqrt
from numpy import arange

turtle.hideturtle()
turtle.speed(0)
turtle.width()

def mandelbrotpoint_point(x_start, y_start):
    def mandel_helper(x_old, y_old, depth):
        x_new = x_old ** 2 - y_old ** 2 - x_start
        y_new = 2 * x_old * y_old - y_start
        r = sqrt(x_new ** 2 + y_new ** 2)
        if(depth <= 0 or r > 10000):
            return r
        return mandel_helper(x_new, y_new, depth-1)
    return mandel_helper(x_start, y_start, 100)

magnification = 200
turtle.shape("square")
turtle.shapesize(0.05,0.05,0.05)
turtle.penup()
for x in arange(-1, 2, 0.005):
    for y in arange(-2, 2, 0.005):
        r = mandelbrotpoint_point(x,y)
        if(r < 10000):
            turtle.goto(x*magnification, y*magnification)
            turtle.stamp()

turtle.exitonclick()