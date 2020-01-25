import turtle

colors = ["pink", "red", "orange", "maroon", "blue"]
def square(edge_length, sides_left = 4):
	turtle.color(colors[sides_left])
	if(sides_left <= 0):
		return
	
	turtle.forward(edge_length)
	turtle.right(90)
	square(edge_length, sides_left-1)


turtle.speed(1)
square(100)
turtle.exitonclick()