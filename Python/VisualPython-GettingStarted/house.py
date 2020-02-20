import turtle

turtle.width(5)

#Draw a square
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
    
#Draw the roof
turtle.right(45)
turtle.forward(141)
turtle.goto(200, 0)

#Move offscreen to make things look cleaner
turtle.penup()
turtle.goto(-500, 500)

turtle.exitonclick()