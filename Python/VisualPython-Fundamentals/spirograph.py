## https://en.wikipedia.org/wiki/Hypotrochoid
import turtle
from math import sin, cos, pi, gcd

turtle.hideturtle()
turtle.speed(0)
turtle.width(2)

#How zoomed in and granular should the picture be.
magnification = 50
steps = 500

#Set the spirographs 3 main variables
R = 4
r = 5
d = 1.5

#Get the lowest common multiple of R and r
lcm = abs(r*R) // gcd(r, R)
upper_bound = 2*pi * (lcm/R)

#Use these to connect the first and last points
first_x, first_y = None, None

theta = 0
turtle.penup()
while(theta <= upper_bound):
    x = (R-r)*cos(theta)+d*cos(theta*((R-r)/r))
    y = (R-r)*sin(theta)-d*sin(theta*((R-r)/r))
    turtle.goto(x * magnification, y * magnification)

    if(first_x == None):
        first_x, first_y = x, y
        turtle.pendown()

    theta += upper_bound/steps

#connect the last point to the first point
turtle.goto(first_x * magnification, first_y * magnification)
turtle.exitonclick()