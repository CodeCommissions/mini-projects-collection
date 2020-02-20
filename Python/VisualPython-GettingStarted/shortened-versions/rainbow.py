import turtle

turtle.width(20)
for new_color in ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]:
    turtle.color(new_color)
    turtle.forward(200)
    turtle.backward(200)
    turtle.right(90)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()
    turtle.left(90)

turtle.penup()
turtle.goto(-500, 500)

turtle.exitonclick()