import turtle

turtle.width(10)

#Draw glass east wall
turtle.color("silver")
turtle.left(90)
turtle.forward(170)
#Draw black main door
turtle.color("black")
turtle.left(45)
turtle.forward(60)

#return to origin and point left
turtle.penup()
turtle.goto(0,0)
turtle.right(90+45)
turtle.pendown()

#Draw mini north-facing wall
turtle.color("red")
turtle.forward(80)
turtle.color("orange")
turtle.forward(85)
turtle.color("yellow")
turtle.forward(90)

#Draw east facing wall
turtle.right(90)
turtle.color("blue")
turtle.forward(95)
turtle.color("indigo")
turtle.forward(100)
turtle.color("violet")
turtle.forward(105)

#Draw south wall
turtle.right(90)
turtle.color("red")
turtle.forward(110)
turtle.color("orange")
turtle.forward(115)
turtle.color("yellow")
turtle.forward(120)
turtle.color("blue")
turtle.forward(125)
turtle.color("indigo")
turtle.forward(130)
turtle.color("violet")
turtle.forward(125)

#Draw west wall
turtle.right(90)
turtle.color("red")
turtle.forward(120)
turtle.color("orange")
turtle.forward(115)
turtle.color("yellow")
turtle.forward(110)
turtle.color("blue")
turtle.forward(105)
turtle.color("indigo")
turtle.forward(100)
turtle.color("violet")
turtle.forward(95)

#Draw top north-facing wall
turtle.right(90)
turtle.color("red")
turtle.forward(90)
turtle.color("orange")
turtle.forward(85)
turtle.color("yellow")
turtle.forward(80)
turtle.color("blue")
turtle.forward(75)
turtle.color("indigo")
turtle.forward(70)
turtle.color("violet")
turtle.forward(65)

#Draw corner cuboard east wall
turtle.right(90)
turtle.color("red")
turtle.forward(60)
turtle.color("orange")
turtle.forward(55)

#Draw corner cuboard inner walls
turtle.right(90)
turtle.color("yellow")
turtle.forward(50)
turtle.color("blue")
turtle.forward(45)
turtle.color("indigo")
turtle.forward(40)
turtle.right(90)
turtle.color("red")
turtle.forward(60)

#Draw cuboard doow
turtle.color("black")
turtle.right(45)
turtle.forward(60)

turtle.exitonclick()