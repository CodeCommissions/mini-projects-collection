import turtle

def setup_turtle():
    turtle.goto(0, -100)
    turtle.clear()
    turtle.speed(0)
    turtle.width(5)

def get_nth_color(n):
    colors = ["maroon", "purple", "black", "green", "cyan"]
    bounded_index = n % len(colors)
    return colors[bounded_index]

def get_next_size(last_size, n):
	return last_size + n//5 #Experiment here

def get_next_angle(last_angle, n):
    return last_angle + n//last_angle #Experiment here

setup_turtle()
next_size = 5 #Experiment here
next_angle = 181 #Experiment here
for i in range(180): #Experiment here
    turtle.color(get_nth_color(i))
    turtle.forward(next_size)
    turtle.left(next_angle)
    next_size = get_next_size(next_size, i)
    next_angle = get_next_angle(next_angle, i)

turtle.exitonclick()