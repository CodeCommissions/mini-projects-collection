import turtle as t
import random as r

def setup_turtle():
    t.clear()
    t.speed(10)
    t.hideturtle()
    t.title('Spiral Art')

def draw_spiral(num_segments, length):
	for i in range(1, num_segments + 1):
		new_size = r.randint(1,6)
		t.pensize(new_size)

		#Some detail on RGB colors
		#https://docs.python.org/3/library/turtle.html#turtle.pencolor
		t.pencolor((r.random(), r.random(), r.random()))		
		t.forward(length * i)
		t.right(45 - (i-1)/2)


setup_turtle()
number_of_pixels = 2
number_of_spirals = 3
for i in range(number_of_spirals):
	x = r.randint(-100, 100)
	y = r.randint(-100, 100)
	t.up()
	t.goto(x, y)
	t.down( )
	
	segments = r.randint(20, 20 + 10 * i)
	draw_spiral(segments, number_of_pixels)

t.done( )