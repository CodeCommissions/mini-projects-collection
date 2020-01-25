import turtle

colors = ["orange", "red", "blue", "green", "maroon", "black","black","yellow","pink"]
def binary_tree(depth, size):
    if (depth==-1):
        return
    
    start_heading = turtle.heading()
    turtle.setheading(270) 

    for angle in [45, -45]:
        #Draw the current branch
        turtle.right(angle)
        turtle.color(colors[depth])
        turtle.forward(size)
        
        #Draw a sub-tree
        binary_tree(depth-1, size*0.5)
        
        #Back-up so that sibling branches start in the same place
        turtle.color(colors[depth])
        turtle.backward(size)
        turtle.right(-angle)
    
    turtle.setheading(start_heading)


turtle.speed(1)
binary_tree(4,200)

turtle.exitonclick()