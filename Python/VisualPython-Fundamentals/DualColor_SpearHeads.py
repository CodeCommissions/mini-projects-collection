import turtle

turtle.speed(0)
turtle.width(3)

turtle.left(90)
for i in range(360*4):
    next_length = i % 360
    turtle.color("red")
    if(i > 360 and i < 720 or i > 360 * 3):
        turtle.color("midnight blue")
        next_length = 360 - (i%360)

    turtle.left(0.25)
    turtle.forward(next_length+2)
    turtle.goto(0,0)

turtle.exitonclick()