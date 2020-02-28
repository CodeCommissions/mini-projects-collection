import turtle

turtle.speed(0)
turtle.width(1)

turtle.left(90)
turtle.color("red")
for i in range(360*2):
    next_length = i
    if(i > 360):
        next_length = 360 - (i%360)

    turtle.left(0.5)
    turtle.forward(next_length+2)
    turtle.goto(0,0)

turtle.exitonclick()