import turtle
import random


def get_default_turtle(existing_turtle=None):
    if existing_turtle is None:
        existing_turtle = turtle.Turtle()
        existing_turtle.color(0.9, 0.9, 0.9)

    return existing_turtle


def teleport_turtle(turt: turtle.Turtle, x, y):
    if turt.isdown():
        turt.penup()
        turt.goto(x, y)
        turt.pendown()
    else:
        turt.goto(x, y)


class DrawShape:
    def __init__(self, pen):
        self._sides = 4
        self._pen = pen
        self._edge_length = 100

    def _draw(self, sides):
        for _ in range(sides):
            self._pen.forward(self._edge_length)
            self._pen.left(360 / sides)

        self._pen.ht()

    @staticmethod
    def draw_now(sides=4, pen=None) -> turtle.Turtle:
        pen = get_default_turtle(pen)

        traceable = DrawShape(pen)
        traceable._draw(sides)

        return pen

    @staticmethod
    def print_more_info():
        print("Draw a single shape.")
        print("You can do this with nothing but turtle.forward() and turtle.left() calls.")
        print("You *can* go a step further and use a for loop.")


class DrawOverlappingShapes:
    @staticmethod
    def draw_now(start_sides=3, end_sides=5, pen=None):
        pen = get_default_turtle(pen)
        for i in range(start_sides, end_sides + 1):
            DrawShape.draw_now(i, pen)

        return pen


class DrawThreeShapes:
    @staticmethod
    def draw_now(pen=None) -> turtle.Turtle:
        pen = pen or turtle.Turtle()
        pen.width(3)
        drawer = DrawShape(pen)
        for x, y, sides, color in [[-200, -200, 3, "blue"], [0, 0, 4, "violet"], [200, 200, 5, "lavender"]]:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()

            pen.color(color)
            drawer.draw_now(sides, pen)

        return pen

    @staticmethod
    def print_more_info():
        print("Draw 3 shapes, disconnected from each other.")
        print("As well as forward() and left() calls, you'll need penup() and pendown().")
        print("Use of goto(x, y) might make things easier.")
        print("Use of loops is encouraged, but not required.")


class DrawSquareSpiral:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)

        pen.speed(10)
        pen.width(2)
        pen.color("black")

        sides = 40
        length = 10
        for i in range(sides):
            pen.forward(length)
            length += 10

            pen.right(90)

        return pen

    @staticmethod
    def draw_doubled_version(pen1=None, pen2=None):
        pen1 = get_default_turtle(pen1)
        pen2 = get_default_turtle(pen2)

        for p in [pen1, pen2]:
            p.speed(5)
            p.width(2)
            p.color("black")

        sides = 40
        length = 10
        pen1.right(180)
        for i in range(sides):
            pen1.forward(length)
            pen2.forward(length)
            length += 10

            pen1.right(90)
            pen2.left(90)

        return pen1, pen2


class StampedSpiral:
    @staticmethod
    def draw_now(pen=None):
        window = turtle.Screen()
        window = window.bgcolor("light green")

        pen = get_default_turtle(pen)
        pen.shape("turtle")
        pen.color("blue")

        pen.penup()
        size = 20
        for i in range(45):
            pen.stamp()
            size += 3
            pen.forward(size)
            pen.right(24)

        return pen


class Star:
    @staticmethod
    def draw_now(pen=None, size=200, edges=5, bgcolor="midnight blue", turtle_color="gold"):
        window = turtle.Screen()
        window.bgcolor(bgcolor)

        pen = get_default_turtle(pen)
        pen.shape("turtle")
        pen.seth(180)
        pen.width(6)

        if edges%2 == 0:
            print(f"Warning, stars have to have an off number of edges. Rounding up from {edges} to {edges+1}.")
            edges += 1

        # Draw a black outline
        pen.color("black")
        for i in range(edges):
            pen.forward(size)
            pen.left(180 - 360 / (edges * 2))

        # Shrink and reposition the turtle so the inner star will be smaller
        pen.width(0)
        pen.color(turtle_color)
        x, y = pen.position()
        teleport_turtle(pen, x-8, y-2)

        # Draw the inner star
        pen.begin_fill()
        for i in range(edges):
            pen.forward(size-16)
            pen.left(180-360/(edges*2))
        pen.end_fill()

        pen.ht()
        return pen


class ClockFace:
    @staticmethod
    def draw_now(pen=None, size=200, hours=12, minutes=12):
        pen = get_default_turtle(pen)
        pen.shape("turtle")
        pen.seth(90)
        pen.width(6)

        pen.color("black")
        for i in range(12):
            pen.penup()
            pen.forward(size*0.8)
            pen.pendown()

            pen.forward(size*0.1)
            pen.penup()
            pen.forward(size*0.1)

            pen.stamp()
            pen.backward(size)
            pen.right(360/12)

        pen.shape("circle")
        pen.stamp()

        pen.shape("arrow")
        pen.pendown()
        minute_angle = (minutes % 60) * (360 / 60)
        hour_angle = (hours%12)*(360/12) + minute_angle/12

        for angle, distance in [[minute_angle, size*0.7],
                                [hour_angle, size*0.5]]:
            pen.seth(90-angle)
            pen.forward(distance)
            pen.stamp()
            pen.backward(distance)

        pen.ht()
        return pen


class DrawBarGraph:
    @staticmethod
    def draw_now(pen=None, data=[200,10,50,100,150,200,150]):
        pen = get_default_turtle(pen)

        pen.width(2)
        pen.color("black")
        colors = ["green", "blue",  "yellow", "orange", "red"]

        # Offset the turtle on the x-axis, so the final graph will be roughly centered
        teleport_turtle(pen, -25*len(data)/2, 0)

        for num in data:
            # If any element is above or below our boundaries, hard-code a color
            if num < 0:
                pen.fillcolor("grey")
            elif num // 50 >= len(colors):
                pen.fillcolor("dark red")
            else:
                pen.fillcolor(colors[num // 50])

            # Draw a single bar (may belong in it's own function)
            pen.begin_fill()
            pen.seth(90)
            pen.forward(num)
            pen.seth(0)
            pen.forward(7)
            pen.write(num)
            pen.forward(23)
            pen.seth(-90)
            pen.forward(num)
            pen.end_fill()

            # Separate each bar by 5 pixels.
            x, y = pen.position()
            teleport_turtle(pen, x+5, y)

        pen.ht()
        return pen


class DrawTarget:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        y = -200

        pen.speed(10)

        sides = 7
        for i in range(sides):
            pen.penup()
            pen.goto(0, y)
            pen.pendown()

            # decide which color
            pen.color(['red', 'white'][i % 2])

            # draw circle
            pen.begin_fill()
            pen.circle((sides - i) * 40)
            pen.end_fill()

            y += 40

        return pen


class DrawCaptainShield:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        y = -200

        pen.speed(10)

        for i in range(4):
            pen.penup()
            pen.goto(0, y)
            pen.pendown()

            # decide which color
            pen.color(['red', 'light grey', 'red', 'blue'][i])

            # draw circle
            pen.begin_fill()
            pen.circle((7 - i) * 40)
            pen.end_fill()

            y += 40

        pen.goto(-150, 130)
        pen.color("white")
        pen.begin_fill()
        for i in range(5):
            pen.forward(300)
            pen.right(144)
        pen.end_fill()

        pen.ht()
        return pen


class DrawGrassTuft:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)

        tufts = random.randint(20, 30)
        for i in range(tufts):
            # Choose an angle from 0 to 40, and then apply a deviation that biases angles to 0 to 10 (slightly)
            offset = random.randint(0, 40)
            for sd in range(2, 8):
                offset = offset if offset < sd*5 else offset + random.randint(-5, 5)

            length = random.randint(90, 120)
            pen.setheading(90 + offset*[-1, 1][i % 2])

            # Offset the amount of green by up to 10%
            pen.color(0.2, 0.7+random.random()/10, 0.2)
            pen.width(3)
            pen.forward(length)
            pen.color(0.2, 0.8+random.random()/10, 0.2)
            pen.width(2)
            pen.backward(length)

        return pen


class Bubbles:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.color("blue")
        pen.width(3)
        teleport_turtle(pen, 0, -200)

        bubbles = random.randint(5,7)
        # Scale the starting bubble size from from 0.75 to 1.25
        size = (1+(random.random()-0.5)/2) * (8*bubbles)

        for i in range(bubbles):
            x, y = pen.position()
            pen.color(random.choice(["royalblue1", "royalblue2", "royalblue3", "royalblue4"]))

            pen.circle(size)
            size = int(size*0.8)
            if size <= 5:
                break

            teleport_turtle(pen, random.randint(-size, size), int(y+size*2.2))

        pen.ht()
        return pen


class DrawMedicCross:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.getscreen().bgcolor("red")
        pen.color("white")

        teleport_turtle(pen, 100, 100)

        pen.begin_fill()
        for i in range(12):
            pen.forward(200)
            if i % 3 == 2:
                pen.left(90)
            else:
                pen.right(90)
        pen.end_fill()

        pen.ht()
        return pen


class Wormhole:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.speed(0)
        pen.width(1)
        pen.color("black")

        pen.seth(-90)
        for i in range(1,150):
            pen.color(i/150, i/150, i/150)
            teleport_turtle(pen, i-100, i)
            pen.circle(i)
            pen.right(0.5)

        pen.ht()
        return pen

    @staticmethod
    def print_more_info():
        print("Draw a wormhole.")
        print("This is an exercise is using circle(), right(), and goto().")
        print("The color shift is optional, and can be achieved with an equation like `i/max_circles`.")
        print("You definitely need a loop to do this.")
        print("")
        print("See if you can draw an exit to the existing wormhole. Maybe by linking 2 similar shapes.")


class SnailShell:
    @staticmethod
    def draw_now(pen=None, colors=["blue", "light blue"]):
        pen = get_default_turtle(pen)
        pen.speed(0)
        pen.width(3)
        pen.color("black")

        size = 200

        for i in range(20):
            pen.fillcolor(colors[i % len(colors)])
            pen.begin_fill()
            pen.circle(size)
            pen.end_fill()
            size -= 10
            pen.right(45)

        pen.ht()
        return pen

    @staticmethod
    def print_more_info():
        print("Draw a snail shell from behind.")
        print("You shouldn't use forward() or goto(), they'll just complicate things.")
        print("This is an exercise is using circle(), right(), begin_fill(), and end_fill()")
        print("You'll also either need to use `ifs` or indexable lists to toggle colors.")
        print("You don't *need* a loop to do this - but it will shrink your code from 140+ lines to more like just 20.")
        print("")
        print("For an extra challenge, make the colors customisable:")
        print("\tA call like `draw_now(colors=['red','blue','green'])` will draw a 3 colored shell.")


class DrawGradientBackground:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.speed(0)

        total_lines = 20
        height = 1000/total_lines
        pen.setheading(90)
        for i in range(1, total_lines):
            teleport_turtle(pen, -500, -500+height*i)

            color_offset = 0.3/total_lines * i
            pen.color(0 + color_offset, 0.3 + color_offset, 0.6+color_offset)
            DrawGradientBackground.draw_row(pen, height, 1000)

        return pen

    @staticmethod
    def draw_row(pen, height, width):
        pen.begin_fill()
        for distance in [height, width, height, width]:
            pen.forward(distance)
            pen.right(90)
        pen.end_fill()


class BrickWall:
    @staticmethod
    def draw_brick(pen:turtle.Turtle, color, width, height):
        pen.fillcolor(color)

        pen.begin_fill()
        for distance in [width, height, width, height]:
            pen.forward(distance)
            pen.right(90)
        pen.end_fill()

    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.color("black")
        pen.width(4)
        pen.speed(0)

        for y in range(400, -400, -50):
            for x in range(-600, 500, 100):
                if y % 100 == 0:
                    offset = 50
                else:
                    offset = 0

                c = random.choice(["sienna1","sienna2","sienna3","sienna4","chocolate1","chocolate2","chocolate3"])
                teleport_turtle(pen, x+offset, y)
                BrickWall.draw_brick(pen, c, 100, 50)

        return pen

    @staticmethod
    def draw_row(pen, height, width):
        pen.begin_fill()
        for distance in [height, width, height, width]:
            pen.forward(distance)
            pen.right(90)
        pen.end_fill()


class DrawPencilLead:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.speed(0)

        pen.width(2)
        teleport_turtle(pen, 100, 0)
        pen.color("black")
        pen.begin_fill()
        pen.setheading(90)
        pen.circle(100)
        pen.end_fill()
        teleport_turtle(pen, 0, 0)

        for i in range(400):
            pen.left(3.35)
            shade = random.randint(0,255)/255
            pen.color(shade, shade, shade)
            distance = random.randint(100,110)
            pen.forward(distance)

            if i < 200:
                x, y = pen.position()
                pen.goto(-300, -300)
                pen.color(shade/2,shade/2,shade/2)
                pen.goto(x, y)
            teleport_turtle(pen, 0, 0)

        pen.ht()
        return pen

    @staticmethod
    def print_more_info():
        print("A zoomed in view of clutch pencil lead (i.e. graphite).")
        print("If you change the colors to more beige/khaki tones, you can turn this into a piece of uncooked spaghetti")
        print()
        print("Depending on your approach, you can get away with not using an `if`, but you will need at least 1 loop.")


class Dice:
    @staticmethod
    def draw_now(pen=None, number=0):
        pen = get_default_turtle(pen)
        pen.speed(0)

        if number == 0:
            number = random.randint(1, 6)

        teleport_turtle(pen, -100, 100)
        pen.pencolor("black")
        pen.width(3)
        pen.fillcolor("light grey")

        pen.begin_fill()
        for i in range(4):
            pen.forward(200)
            pen.right(90)
        pen.end_fill()

        teleport_turtle(pen, 0, -15)

        pen.color("white")
        if number in [1, 3, 5]:
            Dice.draw_offset_circle(pen, 0, 0)

        if number == 6:
            Dice.draw_offset_circle(pen, -30, -50)
            Dice.draw_offset_circle(pen, -30, 0)
            Dice.draw_offset_circle(pen, -30, 50)
            Dice.draw_offset_circle(pen, 30, -50)
            Dice.draw_offset_circle(pen, 30, 0)
            Dice.draw_offset_circle(pen, 30, 50)

        if number in [4, 5]:
            Dice.draw_offset_circle(pen, -50, -50)
            Dice.draw_offset_circle(pen, -50, 50)
            Dice.draw_offset_circle(pen, 50, -50)
            Dice.draw_offset_circle(pen, 50, 50)

        if number == 3:
            Dice.draw_offset_circle(pen, -50, -50)
            Dice.draw_offset_circle(pen, 50, 50)

        if number == 2:
            Dice.draw_offset_circle(pen, 0, -40)
            Dice.draw_offset_circle(pen, 0, 40)

        pen.ht()
        return pen

    def draw_offset_circle(pen : turtle.Turtle, x_offset, y_offset):
        start_x, start_y = pen.position()

        teleport_turtle(pen, start_x+x_offset, start_y+y_offset)
        pen.begin_fill()
        pen.circle(15)
        pen.end_fill()

        teleport_turtle(pen, start_x, start_y)


class DrawWhirlpool:
    @staticmethod
    def draw_now():
        colors = ["blue", "dark blue", "navy"]
        pens = []
        for i in range(6):
            new_turtle = turtle.Turtle()
            new_turtle.width(4)
            new_turtle.color(colors[i % 3])
            new_turtle.left(i * 60)
            new_turtle.speed(10)
            pens.append(new_turtle)

        for i in range(1, 8):
            for pen in pens:
                pen.begin_fill()
                pen.forward(i * 15)
                pen.left(30)

        pen.ht()
        return pens


class DrawPieChart:
    @staticmethod
    def draw_now(pen=None, data=[25, 10, 50, 52, 30]):
        from math import pi

        # Circle size calculations
        edges = sum(data)
        circumference = 1000
        radius = circumference / (2 * pi)
        edge_size = circumference / edges

        # Pen setup
        pen = get_default_turtle(pen)
        pen.color("black")
        pen.width(4)
        pen.speed(3)
        teleport_turtle(pen, radius, 0)
        pen.seth(90)

        for segment in data:
            pen.fillcolor(segment/sum(data), random.random(), segment/sum(data))
            # Move to the center, start a fill, move back to the edge, draw the current edge/segment, finish the fill.
            x, y = pen.position()
            # Center the turtle on (0, 0) because it started drawing its far right edge at (radius, 0)
            pen.goto(0, 0)
            pen.begin_fill()
            pen.goto(x, y)
            for i in range(int(round(segment))):
                pen.left(360/edges)
                pen.forward(edge_size)
            pen.end_fill()

        pen.goto(0, 0)
        pen.ht()
        return pen


class RacerTurtles:
    @staticmethod
    def race_now():
        pens = []
        total_pens = 8
        for i in range(total_pens):
            pen = turtle.Turtle()
            pens.append(pen)
            pen.shape("turtle")
            pen.penup()
            pen.goto(-300, 300 - i * 80)
            pen.penup()
            pen.pendown()

        winner_found = False
        finish_line = 400
        while not winner_found:
            mover = random.choice(pens)
            distance = random.randint(1, 10)
            mover.forward(distance)
            x, y = mover.pos()
            if x >= finish_line:
                winner_found = True
                mover.color("red")
                mover.shapesize(4)


class PolygonFromUser:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.width(2)
        pen.color("black")
        pen.write("How many sides?\n(Look at the terminal)")
        raw_input = input("How many sides: ")

        pen.clear()
        try:
            edges = int(raw_input)
        except:
            pen.write("Invalid input. Please quit.")
            return

        size = 1000 / edges
        for _ in range(edges):
            pen.forward(size)
            pen.left(360 / edges)

        return pen


class DrawChessBoard:
    @staticmethod
    def draw_now(pen=None, height=8, width=8):
        pen = get_default_turtle(pen)
        pen.shape("square")
        pen.shapesize(2)
        pen.penup()

        for x in range(width):
            for y in range(height):
                pen.goto(-120 + x * 40, -120 + y * 40)
                pen.color("black" if x % 2 == y % 2 else "light gray")
                # Alternative that avoid ifs (nice for demoing variety of solutions/techniques):
                # pen.color(["black", "light gray"][(x + y) % 2])
                pen.stamp()

        return pen


class DrawCircleOfCircles:
    @staticmethod
    def draw_now(pen=None, circles=6, debug_mode=False):
        pen = get_default_turtle(pen)

        edge_length = 600/circles
        teleport_turtle(pen, -edge_length/2, edge_length/2)

        for edge in range(circles):
            # If we're in debug mode, we want to leave a trail begin so we can see what went wrong
            if debug_mode:
                pen.forward(edge_length / 2)
            else:
                pen.penup()
                pen.forward(edge_length / 2)
                pen.pendown()

            pen.begin_fill()
            pen.circle(edge_length/2)
            pen.end_fill()

            if debug_mode:
                pen.forward(edge_length/2)
            else:
                pen.penup()
                pen.forward(edge_length / 2)
                pen.pendown()

            pen.right(360 / circles)

        pen.ht()
        return pen

    @staticmethod
    def print_more_info():
        print("Draw X circles equally spaces around a centre spot.")
        print("The main goal of this is to introduce `if-else` blocks (with VERY simple conditions).")
        print("Setting debug-mode to True should make the turtle leave behind a trail.")
        print("Setting debug-mode to False should make the turtle only draw circles and nothing else.")
        print()
        print("If you choose not to implement the debug mode, then you don't need `if-else`s")


class LineGraph:
    @staticmethod
    def draw_now(pen: turtle.Turtle = None, data = None):
        # Use given arguments, or generate some defaults
        pen = get_default_turtle(pen)
        if data is None:
            data = [[random.randint(-30, 30)+x, random.randint(-30, 30)+x] for x in range(-400, 400, 98)]

        pen.color('black')
        pen.width(2)

        # Draw the axes
        teleport_turtle(pen, 400, 0)
        pen.goto(-400, 0)
        teleport_turtle(pen, 0, 400)
        pen.goto(0, -400)

        # Plot the data
        pen.shape("circle")
        teleport_turtle(pen, data[0][0], data[0][1])
        for x, y in data:
            pen.goto(x, y)
            pen.stamp()
            pen.write(f"    ({x}, {y})", align="left", font=("Arial", 10, "bold"))

        return pen


class RandomWalking:
    @staticmethod
    def draw_now(pen: turtle.Turtle = None, max_steps=400):
        pen = get_default_turtle(pen)

        # Draw Bounding Box/s
        pen.color("black")
        teleport_turtle(pen, -300, 300)
        for _ in range(4):
            pen.forward(600)
            pen.right(90)

        # Starting position
        pen.speed(0)
        x, y = random.randint(-280,280), random.randint(-280, 280)
        teleport_turtle(pen, x, y)
        pen.seth(random.randint(0,360))
        pen.shape("turtle")
        pen.color("silver")

        for step in range(max_steps):
            RandomWalking.move_bounded_turtle(pen)

        pen.shapesize(2)
        pen.color("grey")
        return pen

    @staticmethod
    def move_bounded_turtle(turtle_to_move : turtle.Turtle):
        x, y = turtle_to_move.position()
        if x > 300:
            turtle_to_move.seth(random.randint(95, 265))
            x = 300
        elif x < -300:
            turtle_to_move.seth(random.randint(95, 265) + 180)
            x = -300

        if y > 300:
            turtle_to_move.seth(random.randint(5, 175)+180)
            y = 300
        elif y < -300:
            turtle_to_move.seth(random.randint(5, 175))
            y = -300

        # Reset to within border
        turtle_to_move.goto(x, y)

        # Move and turn
        angle = random.randint(0, 30)-15
        distance = random.randint(10, 30)

        turtle_to_move.right(angle)
        turtle_to_move.forward(distance)

    @staticmethod
    def print_more_info():
        print("Make a turtle move around inside a bounding box. Motion should be random, but not extreme. ")
        print("For example, gradual changes in direction of up to 30 degrees, rather `set_heading(x % 360)`.")
        print("This projects requires that you fetch turtle state, and change behaviour based on that information.")
        print("A helper function like `move_bounded_turtle()` will make life easier. But it's not essential")
        print()
        print("A reasonable understanding of variables, loops, and if is needed.")
        print("You can add a fill effect to your turtle, and you'll end up drawing abstract paintings.")


class Minion:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.speed(0)

        pen.color("yellow")
        teleport_turtle(pen, -100, -100)
        pen.begin_fill()
        pen.forward(200)
        pen.left(90)
        pen.forward(200)
        for i in range(18):
            pen.forward(18)
            pen.left(10)
        pen.forward(220)
        pen.left(90)
        pen.end_fill()

        pen.color("black")
        teleport_turtle(pen, -105, 115)
        pen.begin_fill()
        for i in range(2):
            pen.forward(205)
            pen.right(90)
            pen.forward(20)
            pen.right(90)
        pen.end_fill()

        pen.color("silver")
        teleport_turtle(pen, -60, 110)
        pen.right(90)
        pen.begin_fill()
        for i in range(36):
            pen.forward(10)
            pen.left(10)
        pen.end_fill()

        pen.color("white")
        teleport_turtle(pen, -38, 110)
        pen.begin_fill()
        for i in range(36):
            pen.forward(6)
            pen.left(10)
        pen.end_fill()

        pen.color("brown")
        teleport_turtle(pen, -15, 110)
        pen.begin_fill()
        for i in range(36):
            pen.forward(2)
            pen.left(10)
        pen.end_fill()
        pen.left(90)
        teleport_turtle(pen, -105, -30)

        pen.begin_fill()
        pen.color("blue")
        for distance, direction in [[30, 90], [50, -90], [150, -90], [50, 90], [25, 90], [70, 90], [207, 90], [70, 0]]:
            pen.forward(distance)
            pen.right(direction)
        pen.end_fill()

        teleport_turtle(pen, -30, 0)
        pen.color("black")
        pen.right(90)
        for i in range(18):
            pen.forward(6)
            pen.left(3)

        teleport_turtle(pen, 0, 210)
        pen.setheading(0)
        for i in range(3):
            pen.left(45)
            pen.forward(70)
            pen.backward(70)

        return pen

    @staticmethod
    def print_more_info():
        print("Draw a minion from Despicable Me.")
        print("This is a long project, but not complex. A good opportunity to demo how messy code can be divided up.")
        print("You'll need forward(), left()/right(), goto(), color(), penup(), and pendown() at least.")
        print("You can reduce the number of loops you need if you use circle()...")
        print("  ...but you will need at least 1 loop to draw the mouth.")


class Spear:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.color("black")
        pen.speed(0)
        pen.width(5)
        size = 60

        teleport_turtle(pen, 0, -300)
        pen.left(90)

        # Draw pommel
        pen.begin_fill()
        pen.circle(size/2)
        pen.end_fill()

        # Draw body
        for i in range(8):
            pen.fillcolor(["sienna3", "sienna1"][i%2])

            # Draw body segment
            pen.begin_fill()
            for edge in range(4):
                pen.forward(size)
                pen.left(90)
            pen.forward(size)
            pen.end_fill()

        # Draw spear head
        pen.fillcolor("light grey")
        pen.begin_fill()
        for angle, distance in [[-30, size/2], [30, size/2], [30, size*1.5], [90+30, size*1.5], [30, size/2], [30, size/2]]:
            pen.left(angle)
            pen.forward(distance)

        pen.end_fill()

        pen.ht()
        return pen

    @staticmethod
    def print_more_info():
        print("Draw a spear with alternating colors.")
        print("You need to be able to divide up the main problem into 3 sub-problems (pommel, body/shaft, and head)")
        print("You'll need circle(), forward(), left()/right(), goto(), color(), penup(), and pendown() at least.")
        print("Loops are essential for the shaft - you can either use nested loops or a rectangle() helper function")
        print("Ifs will help, but can be skipped if you know about lists and the mod operator")
