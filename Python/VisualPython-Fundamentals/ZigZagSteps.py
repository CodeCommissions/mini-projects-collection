import turtle

turtle.speed(1)
turtle.width(5)

#Declare some constants. This prevents use of 'magic numbers'
STEP_SIZE = 50
TOTAL_STEPS = 5

#Draw simple black steps. Every 2 iterations draws 1 step.
for i in range(TOTAL_STEPS*2):
    if(i%2==0):
        turtle.left(90)
    else:
        turtle.right(90)
    turtle.forward(STEP_SIZE)

turtle.penup()
turtle.goto(0, -STEP_SIZE*2)
turtle.pendown()

#Draw a more colorful set of steps. Identical logic, but adds a list of colors
colors = ["maroon","Dark Orange","purple","firebrick","midnight blue", "pink","dark green"]
for i in range(TOTAL_STEPS*2):
    if(i%2==0):
        #Only change colors when your about to draw an 'up' line
        new_color = colors[i//2]
        turtle.color(new_color)
        turtle.left(90)
    else:
        turtle.right(90)
    turtle.forward(STEP_SIZE)

turtle.exitonclick()