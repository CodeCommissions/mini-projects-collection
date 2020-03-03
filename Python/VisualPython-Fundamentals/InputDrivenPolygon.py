import turtle

turtle.speed(1)
turtle.width(5)

#Declare a constant. This prevents use of magic numbers
STEP_SIZE = 150

#This *assumes* the user gives valid input. Fine here, not a good idea in general
total_steps = int(input("How many sides do you want?"))
for i in range(total_steps):	
	turtle.forward(STEP_SIZE)
	turtle.left(360/total_steps)

turtle.exitonclick()