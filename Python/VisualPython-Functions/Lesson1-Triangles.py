import turtle


colors = ["maroon", "purple", "black", "green", "cyan"]
def setup_turtle():
    turtle.goto(0, -100)
    turtle.clear()
    turtle.speed(1)
    turtle.width(5)

def draw_triangle():
   for _ in range(3):
       turtle.forward(100)
       turtle.right(120)

setup_turtle()
for i in range(3):
   turtle.color(colors[i])
   draw_triangle()
   turtle.left(120)

turtle.exitonclick()
#Quit early, because the homework might break something.
quit()

#########################################################################
######### HOMEWORK SOLUTION BEGINS HERE - AVOID SPOILERS ################
#########################################################################

def draw_two_turn_triangle():
    for _ in range(2): # One less iteration
        turtle.forward(100)
        turtle.right(120)
    turtle.forward(100) # Moved final forward() call out of the loop

setup_turtle()
for i in range(3):
   turtle.color(colors[i])
   draw_two_turn_triangle()

turtle.exitonclick()