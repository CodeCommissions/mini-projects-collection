import turtle, random

# ### ### ### ### ### ###
# # README:
# # This entire module was quickly cobbled togeher to demo the Pythagorean theorem.
# # It's not clean. Or simple. It's just here to share with student's who are interested.
# # The rapid flickering comes from clearing and redrawing the scene many times each second, and toggling screen.tracer
# ### ### ### ### ### ###

# Setup
pen = turtle.Turtle()
pen.getscreen().bgcolor("light blue")
pen.speed(10)
pen.ht()

# Use a class to track each moons state as it moves
# Wraps movement logic and positional logic together
class Moon:
    def __init__(self, x, y, orbit_radius):
        self.x = x
        self.y = y
        self.distance_travelled = 0
        self.orbit_radius = orbit_radius

        self.pen = turtle.Turtle()
        self.pen.speed(0)

        self.pen.fillcolor("black")
        self.pen.shapesize(1)
        self.pen.shape("circle")
        self.pen.up()
        self.pen.goto(x, y-orbit_radius)
        self.pen.down()

        # random.random()*10
        self.speed = 0.25
        self.pen.width(3)

    def draw_step(self):
        from math import hypot, sqrt
        screen = self.pen.getscreen()
        write_color = "dark red"

        x, y = self.pen.pos()
        orbit_size = hypot(x, y)

        r_x_mid = x/2
        r_y_mid = sqrt((orbit_size/2)**2 - r_x_mid**2) * (1 if y>0 else -1)


        screen.tracer(0)
        font=("courier new", 24, "bold")
        self.pen.clear()
        self.pen.circle(self.orbit_radius)

        self.pen.width(2)
        self.pen.goto(r_x_mid, r_y_mid)
        self.pen.pencolor(write_color)
        self.pen.write("r", align="center", font=font)
        self.pen.pencolor("black")
        self.pen.goto(0, 0)

        self.pen.goto(x/2, 0)
        self.pen.pencolor(write_color)
        self.pen.write("x", align="center", font=font)
        self.pen.pencolor("black")
        self.pen.goto(x, 0)

        self.pen.goto(x, y/2)
        self.pen.pencolor(write_color)
        self.pen.write("y", align="right", font=font)
        self.pen.pencolor("black")
        self.pen.goto(x, y)
        self.pen.width(4)
        screen.tracer(1)

        self.pen.circle(self.orbit_radius, self.speed)
        screen.update()



def draw_moons_forever(moons):
    while True:
        for moon in moons:
            moon.draw_step()


# Second (identical) 'moon' redraws the same lines, and reduced flickering from tracer() toggling
jupiter_moons = [Moon(0, 0, 200), Moon(0, 0, 200)]
draw_moons_forever(jupiter_moons)

pen.getscreen().exitonclick()
