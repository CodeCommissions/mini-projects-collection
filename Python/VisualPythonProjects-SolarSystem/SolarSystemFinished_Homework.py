import turtle, random

# ### ### ### ### ### ###
# # README:
# # This module was put together to DEMO several of the homework projects proposed.
# # It uses concepts like classes, and lists of objects. So just hit play and see it run ^_^
# ### ### ### ### ### ###

# Setup
pen = turtle.Turtle()
pen.getscreen().bgcolor("grey")
pen.speed(0)

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
        self._ellipse_divisor = random.randint(1,3)

        grey = random.random()*0.9+0.1

        self.pen.fillcolor(grey,grey,grey)
        self.pen.shapesize(random.random()+0.4)
        self.pen.shape("circle")
        self.pen.up()
        self.pen.goto(x, y-orbit_radius)
        self.pen.circle(orbit_radius, random.random()*360)
        self.pen.down()

        self.speed = random.random()*10

    def draw_step(self):
        default_speed = 5+self.speed
        # When approaching an ellipse-corner, bounded_speed calculates how much distance is left before the corner
        bounded_speed = 90-(self.distance_travelled%90)

        # speed_1 is the primary speed, speed_2 is how much to move after crossing a ellipse's 90 degree mark
        speed_1 = min(default_speed, 90-(self.distance_travelled%90))
        speed_2 = max(default_speed-bounded_speed, 0)

        second_quarter = self.distance_travelled % 360 // 90 in [0, 2]
        if second_quarter:
            self.pen.circle(self.orbit_radius, speed_1)
            self.pen.circle(self.orbit_radius/self._ellipse_divisor, speed_2)
        else:
            self.pen.circle(self.orbit_radius/self._ellipse_divisor, speed_1)
            self.pen.circle(self.orbit_radius, speed_2)
        self.distance_travelled += 5+self.speed


def draw_planet(x, y, size, color, name):
    orbit = (x**2+y**2)**0.5
    pen.up()
    pen.goto(0, -orbit)
    pen.down()
    pen.circle(orbit)

    pen.penup()
    pen.goto(x, y - size)
    pen.pendown()

    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

    pen.penup()
    pen.goto(x, y + size)
    pen.pendown()
    pen.write(name, align="center", font=("courier", 18, "bold"))


def randomise_turtle(to_randomise):
    to_randomise.shapesize(random.random()+0.2)
    grey = random.random()*0.5+0.25
    to_randomise.color(grey, grey, grey)


def draw_asteroid_belt(radius):
    offset = 10
    pen.penup()
    pen.goto(0, -radius)
    pen.shape("circle")
    for i in range(100):
        randomise_turtle(pen)
        x_start, y_start = pen.pos()
        x_offset = random.randint(-offset, offset)
        y_offset = random.randint(-offset, offset)
        pen.goto(x_start + x_offset, y_start + y_offset)
        pen.stamp()
        pen.goto(x_start, y_start)
        pen.circle(radius, 3.6)
    pen.pendown()


def draw_asteroid_belts():
    pen.getscreen().tracer(5)
    for belt_radius in [200, 460, 470, 480, 490, 500]:
        draw_asteroid_belt(belt_radius)
    pen.getscreen().tracer(1)


def draw_moons_forever(moons):
    while True:
        for moon in moons:
            moon.draw_step()


def draw_planets():
    draw_planet(0, 0, 20, "yellow", "Sun")
    draw_planet(0, 55, 10, "dark red", "Mercury")
    draw_planet(-50, -60, 18, "orange", "Venus")
    draw_planet(120, 20, 20, "light blue", "Earth")
    draw_planet(0, -160, 15, "red", "Mars")
    draw_planet(-220, 150, 30, "brown", "Jupiter")
    draw_planet(190, -230, 28, "goldenrod", "Saturn")
    draw_planet(-330, 40, 26, "powder blue", "Uranus")
    draw_planet(400, 20, 25, "royal blue", "Neptune")


draw_planets()

draw_asteroid_belts()

earth_moon = [Moon(120, 20, 40), ]
jupiter_moons = [Moon(0, 0, 100), Moon(-220, 150, 50), Moon(-220, 150, 80), Moon(-220, 150, 80)]
draw_moons_forever(earth_moon + jupiter_moons)

pen.getscreen().exitonclick()
