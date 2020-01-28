import turtle
from numpy import arccos, degrees


colors = ["maroon", "purple", "black", "green", "cyan"]
def setup_turtle():
    turtle.goto(0, -100)
    turtle.clear()
    turtle.speed(1)
    turtle.width(5)

def draw_triangle(edge1, edge2 = None, edge3 = None):
    if(edge2 is None or edge3 is None):
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

setup_turtle()
for i in range(3):
    turtle.color(colors[i])
    draw_triangle(220, 70, 200)
    turtle.left(120)

turtle.exitonclick()
#Quit early, because the homework might break something.
quit()

#########################################################################
######### HOMEWORK SOLUTION BEGINS HERE - AVOID SPOILERS ################
#########################################################################

#TODO - Add homework