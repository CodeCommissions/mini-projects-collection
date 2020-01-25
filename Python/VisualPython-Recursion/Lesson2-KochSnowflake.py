import turtle

def koch_edge(order, size):
    if(order == 0):
        turtle.forward(size)
        return

    for angle in [60, -120, 60, 0]:
        #Optional homework - change turtle.width to show which line-edge
        #is currently being drawn. eg width 1 for the first edge
        koch_edge(order-1, size/3)
        turtle.left(angle)

def koch_snowflake(order, size):
    colors = ["red", "maroon","blue"]
    for i in range(3):
        turtle.color(colors[i])
        turtle.right(120);
        koch_edge(order, size)

turtle.speed(1)
koch_snowflake(3,300)
turtle.exitonclick()