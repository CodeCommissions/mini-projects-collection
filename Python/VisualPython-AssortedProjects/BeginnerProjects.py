import turtle
import random


def get_default_turtle(existing_turtle=None):
    if existing_turtle is None:
        existing_turtle = turtle.Turtle()
        existing_turtle.color(0.9, 0.9, 0.9)

    return existing_turtle


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
        for x, y, sides, color in [[-200,-200,3,"blue"], [0,0,4,"violet"], [200,200,5,"lavender"]]:
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
            pen.circle((sides-i)*40)
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
            pen.circle((7-i)*40)
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


class DrawWhirlpool:
    @staticmethod
    def draw_now():
        colors = ["blue", "dark blue", "navy"]
        pens = []
        for i in range(6):
            new_turtle = turtle.Turtle()
            new_turtle.width(4)
            new_turtle.color(colors[i%3])
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
            pen.color(colors[i%2])
            pen.begin_fill()
            for _ in range(3):
                pen.forward(100)
                pen.left(360/3)
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
    def draw_now():
        pen = get_default_turtle()
        pen.color("black")
        pen.write("How many sides?\n(Look at the terminal)")
        raw_input = input("How many sides: ")

        pen.clear()
        try:
            edges = int(raw_input)
        except:
            pen.write("Invalid input. Please quit.")
            return

        size = 1000/edges
        for _ in range(edges):
            pen.forward(size)
            pen.left(360/edges)

        return pen


class DrawChessBoard:
    @staticmethod
    def draw_now():
        pen = get_default_turtle()
        pen.shape("square")
        pen.shapesize(2)
        pen.penup()

        for x in range(8):
            for y in range(8):
                pen.goto(-120 + x*40, -120 + y*40)
                pen.color("black" if x % 2 == y % 2 else "light gray")
                pen.stamp()

        return pen
