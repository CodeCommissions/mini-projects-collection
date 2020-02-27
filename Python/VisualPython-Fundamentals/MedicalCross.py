import turtle

turtle.speed(1)
turtle.width(5)

#Declare some constants. This prevents use of 'magic numbers'
STEP_SIZE = 100
TOTAL_SIDES = 4

#Draw black back-shadow cross
for i in range(TOTAL_SIDES*3):
    if(i%3==0):
        turtle.left(90)
    else:
        turtle.right(90)

    turtle.forward(STEP_SIZE)

#Add an offset so the shadow isn't drawn over
turtle.goto(5,4)

#Draw the main, colorful, cross. Identical logic, but adds a list of colors
colors = ["maroon","Dark Orange","purple","firebrick","midnight blue", "pink","dark green"]
for i in range(TOTAL_SIDES*3):
    if(i%3==0):
        #Only change colors when your about to draw an 'up' line
        new_color = colors[i//3]
        turtle.color(new_color)
        turtle.left(90)
    else:
        turtle.right(90)
    turtle.forward(STEP_SIZE)

turtle.exitonclick()