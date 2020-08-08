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
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.speed(10)

        colors = ["red", "light grey"]
        for i in range(6):
            pen.color(colors[i % 2])
            pen.begin_fill()
            for _ in range(3):
                pen.forward(100)
                pen.left(360 / 3)
            pen.end_fill()
            pen.left(60)

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
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.shape("square")
        pen.shapesize(2)
        pen.penup()

        for x in range(8):
            for y in range(8):
                pen.goto(-120 + x * 40, -120 + y * 40)
                pen.color("black" if x % 2 == y % 2 else "light gray")
                pen.stamp()

        return pen


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
        print("Draw a minion from Despicable Me")
        print("You'll need forward(), left()/right(), goto(), color(), penup(), and pendown() at least.")
        print("You can reduce the number of loops you need if you use circle()...")
        print("  ...but you will need at least 1 for the mouth")
