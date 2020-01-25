from time import sleep
import turtle

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        if(value == None):
            self.left_child = None
            self.right_child = None
        else:
            self.left_child = TreeNode()
            self.right_child = TreeNode()

    def __str__(self):
        return f"{self.value} (L: {str(self.left_child)}, R: {str(self.right_child)})"

def populate_binary_tree(current_node, new_value):
    if(current_node.value == None):
        current_node.value = new_value
        turtle.write(current_node.value, align="center",
                     font=("Arial",12,"bold"))
        current_node.left_child = TreeNode()
        current_node.right_child = TreeNode()
    elif(new_value == current_node.value):
        turtle.backward(50)
    elif(new_value > current_node.value):
        turtle.write(current_node.value, align="center",
                     font=("Arial", 8, "bold"))
        turtle.right(45)
        turtle.forward(50)
        populate_binary_tree(current_node.right_child, new_value)
        turtle.backward(50)
        turtle.left(45)
    else:
        turtle.write(current_node.value, align="center",
                     font=("Arial", 8, "bold"))
        turtle.left(45)
        turtle.forward(50)
        populate_binary_tree(current_node.left_child, new_value)
        turtle.backward(50)
        turtle.right(45)


def draw_binary_tree(current_node):
    if(current_node.value == None):
        turtle.write("<empty>", align="center",
                     font=("Arial",12,"normal"))
        return

    #Draw the left branch (even if its blank)
    turtle.left(45)
    turtle.forward(100)
    draw_binary_tree(current_node.left_child)
    turtle.backward(100)
    turtle.right(45)

    turtle.write(current_node.value, align="center",
                 font=("Arial",16,"bold"))

	#Draw the right branch (even if its blank)
    turtle.right(45)
    turtle.forward(100)
    draw_binary_tree(current_node.right_child)
    turtle.backward(100)
    turtle.left(45)


turtle.speed(1)
turtle.left(90)
root = TreeNode(8)
for new_value in [7, 5, 6,7.5, 9, 10,11,]:
    populate_binary_tree(root, new_value)
    sleep(1)
    turtle.clear()
draw_binary_tree(root)

turtle.exitonclick()