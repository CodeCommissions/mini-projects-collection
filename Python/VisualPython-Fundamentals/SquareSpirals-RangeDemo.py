import turtle

def get_next_color(index):
    colors = ["maroon","Dark Orange","purple","firebrick","midnight blue", "black","dark green"]
    return colors[index % len(colors)]


turtle.speed(0)
turtle.width(1)

#The number of pixels that go into the longest edge of a very slow-growing spirals
LONGEST_EDGE = 300

#Draw black back-shadow cross
for i in range(LONGEST_EDGE):
    turtle.left(90)
    turtle.forward(i+1)

turtle.penup()
turtle.goto(LONGEST_EDGE+5,0)
turtle.pendown()
#Colours don't show up well on thin turtles, so thicken it up here.
turtle.width(3)

for i in range(LONGEST_EDGE):
    new_color = get_next_color(i)
    turtle.color(new_color)
    turtle.left(90)
    turtle.forward(i+1)

turtle.exitonclick()
