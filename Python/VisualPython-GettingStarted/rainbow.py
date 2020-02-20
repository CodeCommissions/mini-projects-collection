import turtle

turtle.width(20)

#Draw a red line
turtle.color("red")
turtle.forward(200)
#Turn and move down without drawing a line
turtle.right(90)
turtle.penup()
turtle.forward(20)
turtle.pendown()
#Get ready to move in the other direction
turtle.right(90)

#Repeat the same 3 steps for all 7 lines
turtle.color("orange")
turtle.forward(200)
turtle.left(90)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.left(90)

turtle.color("yellow")
turtle.forward(200)
turtle.right(90)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.right(90)

turtle.color("green")
turtle.forward(200)
turtle.left(90)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.left(90)

turtle.color("blue")
turtle.forward(200)
turtle.right(90)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.right(90)

turtle.color("indigo")
turtle.forward(200)
turtle.left(90)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.left(90)

turtle.color("violet")
turtle.forward(200)
turtle.right(90)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.right(90)

#Move offscreen to make things look cleaner
turtle.penup()
turtle.goto(-500, 500)

turtle.exitonclick()