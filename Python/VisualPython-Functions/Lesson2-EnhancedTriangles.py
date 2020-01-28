import turtle
from numpy import arccos, degrees

colors = ["maroon", "purple", "black", "green", "cyan"]
def setup_turtle():
    turtle.goto(0, -100)
    turtle.clear()
    turtle.speed(1)
    turtle.width(5)

def draw_triangle(edge1, edge2 = None, edge3 = None):
    if (edge2 is None and edge3 is None):
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
    draw_triangle(220, 70)
    turtle.left(120)

turtle.exitonclick()
#Quit early, because the homework might break something.
quit()

#########################################################################
######### HOMEWORK SOLUTION BEGINS HERE - AVOID SPOILERS ################
#########################################################################

def draw_triangle_homework_version(edge1, edge2 = None, edge3 = None):
    '''
    Draws a triangle. Specifying just 1 edge will draw an equilateral triangle.
    Including 2 edge-lengths will draw an issolese triangle.
    Specifying all 3 edges will can draw any type of triangle.
    '''
    if (edge2 is None and edge3 is None):
        edge2 = edge1
        edge3 = edge1

    #The above check ensures that once here you can never have more than 1 blank edge
    if(edge2 is None):
        edge2 = edge1
    if(edge3 is None):
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