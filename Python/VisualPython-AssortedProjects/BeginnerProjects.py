import turtle
import random


def get_default_turtle(existing_turtle=None) -> turtle.Turtle:
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


class StickHouseChallenge:
    @staticmethod
    def draw_now(pen=None, size=150):
        from math import sqrt
        size = abs(size)
        pen = get_default_turtle(pen)
        pen.getscreen().bgcolor("black")
        pen.speed(1)
        pen.width(6)
        teleport_turtle(pen, -size/2, -size/2)

        colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "cyan"]
        distances = [size,  sqrt(2*size**2), sqrt(size**2/2), sqrt(size**2/2), size, size, sqrt(2*size**2), size]
        headings = [0, 180-45, 45, -45, 180, 270, 45, 270]
        for heading, distance, color in zip(headings, distances, colors):
            pen.color(color)
            pen.seth(heading)
            pen.forward(distance)

        pen.ht()
        return pen

    @staticmethod
    def print_more_info():
        print("Draw a house with 8 lines that never overlap.")
        print("Unless you know about lists, it's easier to do this project WITHOUT loops.")
        print("You can work out the directions and distances through trial and error. But some Pythagoras will help.")
        print()
        print("For extra challenge add a settable size that scales up correctly. Colors are also optional.")


class NestedShapes:
    @staticmethod
    def draw_now(pen=None, shapes=5, sides=4) -> turtle.Turtle:
        pen = get_default_turtle(pen)
        pen.color("black")
        pen.width(3)

        for shape in range(shapes):
            teleport_turtle(pen, 0, (shape + 1) * 105/sides)
            pen.forward((shape + 1) * 105/sides)

            for side in range(sides-1):
                pen.right(360/sides)
                pen.forward((shape+1) * 210/sides)

            pen.right(360 / sides)
            pen.forward((shape + 1) * 105/sides)

        pen.ht()
        return pen

    @staticmethod
    def print_more_info():
        print("Draw shapes inside each other - gradually getting bigger/smaller.")
        print("You can do this with a helper function (like `draw_shape()`), or you can use nested loops.")


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


class FlagPole:
    @staticmethod
    def draw_now(pen: turtle.Turtle = None, image_address="flag.gif", flag_x=-22, flag_y=120):
        pen = get_default_turtle(pen)

        # Draw pole
        pen.color(0.8, 0.8, 0.8)
        teleport_turtle(pen, -300, -300)
        pen.width(8)
        pen.seth(90)
        pen.forward(600)

        # Draw pole 'head'
        pen.shape("circle")
        pen.shapesize(3)
        pen.color(0.9, 0.9, 0.9)
        pen.stamp()

        # Load flag image
        pen.screen.addshape(image_address)
        pen.shape(image_address)
        teleport_turtle(pen, flag_x, flag_y)

        return pen


class StampArt:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)

        turtle.setup(800, 600)
        pen.shape("turtle")
        pen.speed(0)
        half_width, half_height = turtle.Screen().screensize()

        for i in range(20):
            pen.penup()
            x_pos, y_pos = pen.position()
            while (x_pos < half_width) and (x_pos >= -half_width) and (y_pos < half_height) and (y_pos >= -half_height):
                new_color = (random.random(), random.random(), random.random())
                pen.pencolor(new_color)
                pen.fillcolor("white")
                pen.shapesize(random.randint(1, 4))
                pen.stamp()

                pen.right(random.randint(0, 359))
                pen.forward(random.randint(25, 100))
                x_pos, y_pos = pen.position()

            pen.penup()
            pen.goto(0, 0)
            pen.pendown()

        return pen


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


class AgeGroupTurtle:
    @staticmethod
    def draw_now(pen=None):
        # Turtle setup
        pen = get_default_turtle(pen)
        pen.shape("turtle")
        pen.color("blue")
        pen.seth(90)

        # Get and display age
        max_age = 80
        age = random.randint(0, max_age)
        pen.write(f"I'm {age}...", align="center", font=("Arial", 12, "bold"))

        teleport_turtle(pen, 0, -20)

        # Find the first group that the turtle fits in, and display it.
        ages_groups = [[2, "baby"], [5, "toddler"], [13, "kiddie"], [18, "teen"], [50, "adult"], [max_age+1, "old"]]
        size = 1
        for age_boundary, group in ages_groups:
            pen.shapesize(size)
            if age < age_boundary:
                a_or_an = "a" if group[0] not in "aeiou" else "an"
                pen.write(f"So I'm {a_or_an} {group} turtle!", align="center", font=("Arial", 12, "bold"))
                break
            size += 1

        # Move away from the text so it isn't hidden.
        teleport_turtle(pen, 0, size*-20-20)
        return pen

    @staticmethod
    def print_more_info():
        print("Make a turtle that gives a greeting based on a randomly generated age.")
        print("For example, if the turtle is under 2 years old it might say `I'm a baby`")
        print("")
        print("Needs an `if`. You *can* get away with not using an `elif` or `else`, but you'll need a list instead.")
        print("For extra points, change `shapesize` so the turtle looks bigger when it's older.")


class Slinky:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.speed(0)
        pen.seth(-90)

        for i in range(15):
            pen.color(random.random(), random.random(), random.random())

            for j in range(10):
                pen.right(6+14)
                pen.forward(12+j)

            pen.color(random.random(), random.random(), random.random())
            for j in range(10):
                pen.right(12+j)
                pen.forward(12+j)

        pen.ht()
        return pen

    @staticmethod
    def print_more_info():
        print("Draw a slinky")
        print("Avoid using turtle.circle() - you'll want to use nested loops (maybe more than 1).")
        print("Adjust the turtle's right() and forward() arguments so they change as loop variable change.")
        print("")
        print("The code isn't complex, but it may take a lot of experimentation to avoid just creating a spirograph")


class Covid19:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.speed(0)

        pen.color("dark red")
        for i in range(1, 212):
            pen.forward(i)
            pen.left(i)

        pen.color("black")
        for i in range(212, 100, -1):
            pen.forward(i)
            pen.left(i)

        pen.up()
        pen.goto(0, 250)
        pen.write("COVID 19 Mockup", align="center", font=("Courier", 18, "bold"))
        pen.goto(0, 225)
        pen.write("Hint: move by X, turn by X, change X, repeat", align="center", font=("Courier", 14, "bold"))
        pen.goto(0, 200)
        pen.write("X => 1 -> 212 -> 100", align="center", font=("Courier", 14, "bold"))
        pen.ht()
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


class TwoValueBarGraph:
    @staticmethod
    def draw_now(pen=None, value1=0.9, value2=0.1, scaling_factor=100):
        DrawBarGraph.draw_now(pen, data=[int(value1*scaling_factor), int(value2*scaling_factor)])

    @staticmethod
    def print_more_info():
        print("A list-free alternative to DrawBarGraph")
        print("A helper function that draws a single bar at XY means you won't have to do any looping.")
        print("")
        print("You should only need if-elses - but lists will help if you want to use several colors.")


class DrawBarGraph:
    @staticmethod
    def draw_now(pen=None, data=(200, 10, 50, 100, 150, 200, 150)):
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
                pen.fillcolor(colors[int(num // 50)])

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


class TetrisShapes:
    @staticmethod
    def draw_now(pen=None, shape="o", square_width=50):
        pen = get_default_turtle(pen)
        pen.pencolor("black")
        pen.fillcolor(random.random(),random.random(),random.random())
        pen.width(3)

        # 12 13 14 15
        #  8  9 10 11
        #  4  5  6  7
        #  0  1  2  3
        shapes = {"o": [0, 1, 4, 5],
                  "i": [0, 4, 8, 12],
                  "t": [0, 1, 2, 5],
                  "s": [0, 1, 5, 6],
                  "z": [4, 5, 1, 2],
                  "j": [4, 0, 1, 2],
                  "l": [0, 1, 2, 6]}
        shapes["square"] = shapes["o"]
        shapes["line"] = shapes["i"]
        shapes["right snake"] = shapes["s"]
        shapes["left snake"] = shapes["z"]
        shapes["left gun"] = shapes["j"]
        shapes["right gun"] = shapes["l"]
        shapes["pyramid"] = shapes["t"]

        def square_at(x, y):
            pen.seth(0)
            teleport_turtle(pen, x, y)
            pen.begin_fill()
            for i in range(4):
                pen.forward(square_width)
                pen.left(90)
            pen.end_fill()

        for pos in shapes[str.lower(shape)]:
            square_at(pos%4 * square_width, pos//4 * square_width)

        pen.ht()
        return pen


class PeriodicTable:
    @staticmethod
    def draw_now(pen=None, square_width=50):
        pen = get_default_turtle(pen)
        WIDTH = square_width
        pen = turtle.Turtle()

        def draw_element(x, y, name, abbreviation, number, color):
            pen.pencolor("black")
            pen.fillcolor(color)
            pen.width(3)

            teleport_turtle(pen, x, y)
            pen.seth(0)
            pen.begin_fill()
            for i in range(4):
                pen.forward(WIDTH)
                pen.left(90)
            pen.end_fill()

            teleport_turtle(pen, x + WIDTH / 2, y)
            pen.write(name, align="center", font=("courier", 6, "bold"))

            teleport_turtle(pen, x + WIDTH * 0.5, y + WIDTH * 0.25)
            pen.write(abbreviation, align="center", font=("courier", 20, "bold"))

            teleport_turtle(pen, x + WIDTH * 0.95, y + WIDTH * 0.6)
            pen.write(number, align="right", font=("courier", 10, "bold"))

        def get_category_color(category_name):
            colors = {"reactive": "light yellow",
                      "noble": "light blue",
                      "alkali": "pink",
                      "metalloid": "brown",
                      "alkaline": "red",
                      "lanthanide": "yellow",
                      "actinide": "orange",
                      "transition": "green",
                      "post-transition": "grey",
                      "unknown": "dark grey"}
            if category_name not in colors:
                return "white"
            return colors[category_name]

        pen.speed(0)
        LEFT = -450
        TOP = 150

        for i in range(1, 119):
            period, group, name, abbv, category = PeriodicTable.get_element_data(i)
            color = get_category_color(category)
            draw_element(LEFT + period * WIDTH, TOP - group * WIDTH, name, abbv, i, color)

        teleport_turtle(pen, 0, TOP)
        pen.write("Periodic Table", align="center", font=("courier", 20, "bold"))
        teleport_turtle(pen, 0, TOP - 20)
        pen.write("Use PeriodicTable.get_element_data(element_number) to get:", align="center",
                  font=("courier", 14, "bold"))
        teleport_turtle(pen, 0, TOP - 40)
        pen.write("period, group, name, abbreviation, category", align="center", font=("courier", 14, "bold"))

        pen.ht()

    @staticmethod
    def get_element_data(element_number):
        elements = [(1, 1, "Hydrogen", "H", "reactive"),
                    (18, 1, "Helium", "He", "noble"),
                    (1, 2, "Lithium", "Li", "alkali"),
                    (2, 2, "Beryllium", "Be", "alkaline"),
                    (13, 2, "Boron", "B", "metalloid"),
                    (14, 2, "Carbon", "C", "reactive"),
                    (15, 2, "Nitrogen", "N", "reactive"),
                    (16, 2, "Oxygen", "O", "reactive"),
                    (17, 2, "Fluorine", "F", "reactive"),
                    (18, 2, "Neon", "Ne", "noble"),
                    (1, 3, "Sodium", "Na", "alkali"),
                    (2, 3, "Magnesium", "Mg", "alkaline"),
                    (13, 3, "Aluminium", "Al", "post-transition"),
                    (14, 3, "Silicon", "Si", "metalloid"),
                    (15, 3, "Phosphorous", "P", "reactive"),
                    (16, 3, "Sulfur", "S", "reactive"),
                    (17, 3, "Chlorine", "Cl", "reactive"),
                    (18, 3, "Argon", "Ar", "noble"),

                    (1, 4, "Potassium", "K", "alkali"),
                    (2, 4, "Calcium", "Ca", "alkaline"),
                    (3, 4, "Scandium", "Sc", "transition"),
                    (4, 4, "Titanium", "Ti", "transition"),
                    (5, 4, "Vanadium", "V", "transition"),
                    (6, 4, "Chromium", "Cr", "transition"),
                    (7, 4, "Manganese", "Mn", "transition"),
                    (8, 4, "Iron", "Fe", "transition"),
                    (9, 4, "Cobalt", "Co", "transition"),
                    (10, 4, "Nickel", "Ni", "transition"),
                    (11, 4, "Copper", "Cu", "transition"),
                    (12, 4, "Zinc", "Zn", "post-transition"),
                    (13, 4, "Gallium", "Ga", "post-transition"),
                    (14, 4, "Germanium", "Ge", "metalloid"),
                    (15, 4, "Arsenic", "As", "metalloid"),
                    (16, 4, "Selenium", "Se", "reactive"),
                    (17, 4, "Bromine", "Br", "reactive"),
                    (18, 4, "Krypton", "Kr", "noble"),

                    (1, 5, "Rubidium", "Rb", "alkali"),
                    (2, 5, "Strontium", "Sr", "alkaline"),
                    (3, 5, "Yttrium", "Y", "transition"),
                    (4, 5, "Zirconium", "Zr", "transition"),
                    (5, 5, "Niobium", "Nb", "transition"),
                    (6, 5, "Molybdenum", "Mo", "transition"),
                    (7, 5, "Technetium", "Tc", "transition"),
                    (8, 5, "Ruthenium", "Ru", "transition"),
                    (9, 5, "Rhodium", "Rh", "transition"),
                    (10, 5, "Palladium", "Pd", "transition"),
                    (11, 5, "Silver", "Ag", "transition"),
                    (12, 5, "Cadmium", "Cd", "post-transition"),
                    (13, 5, "Indium", "In", "post-transition"),
                    (14, 5, "Tin", "Ti", "post-transition"),
                    (15, 5, "Antimony", "Sb", "metalloid"),
                    (16, 5, "Tellurium", "Te", "metalloid"),
                    (17, 5, "Iodine", "I", "reactive"),
                    (18, 5, "Xenon", "Xe", "noble"),

                    (1, 6, "Caesium", "Cs", "alkali"),
                    (2, 6, "Barium", "Ba", "alkaline"),
                    (3, 6, "Lanthanum", "La", "lanthanide"),
                    (3, 6, "Cerium", "Ce", "lanthanide"),
                    (3, 6, "Praseodymium", "Pr", "lanthanide"),
                    (3, 6, "Neodymium", "Nd", "lanthanide"),
                    (3, 6, "Promethium", "Pm", "lanthanide"),
                    (3, 6, "Samarium", "Sm", "lanthanide"),
                    (3, 6, "Europium", "Eu", "lanthanide"),
                    (3, 6, "Gadolinium", "Gd", "lanthanide"),
                    (3, 6, "Terbium", "Tb", "lanthanide"),
                    (3, 6, "Dysprosium", "Dy", "lanthanide"),
                    (3, 6, "Holmium", "Ho", "lanthanide"),
                    (3, 6, "Erbium", "Er", "lanthanide"),
                    (3, 6, "Thulium", "Tm", "lanthanide"),
                    (3, 6, "Ytterbium", "Yb", "lanthanide"),
                    (3, 6, "Lutetium", "Lu", "lanthanide"),
                    (4, 6, "Hafnium", "Hf", "transition"),
                    (5, 6, "Tantalum", "Ta", "transition"),
                    (6, 6, "Tungsten", "W", "transition"),
                    (7, 6, "Rhenium", "Re", "transition"),
                    (8, 6, "Osmium", "Os", "transition"),
                    (9, 6, "Iridium", "Ir", "transition"),
                    (10, 6, "Platinum", "Pt", "transition"),
                    (11, 6, "Gold", "Au", "transition"),
                    (12, 6, "Mercury", "Hg", "post-transition"),
                    (13, 6, "Thallium", "Tl", "post-transition"),
                    (14, 6, "Lead", "Pb", "post-transition"),
                    (15, 6, "Bismuth", "Bi", "post-transition"),
                    (16, 6, "Polonium", "Po", "post-transition"),
                    (17, 6, "Astatine", "At", "post-transition"),
                    (18, 6, "Radon", "Rn", "noble"),

                    (1, 7, "Francium", "Fr", "alkali"),
                    (2, 7, "Radium", "Ra", "alkaline"),
                    (3, 7, "Actinium", "Ac", "actinide"),

                    (3, 7, "Thorium", "Th", "actinide"),
                    (3, 7, "Protactinium", "Pa", "actinide"),
                    (3, 7, "Uranium", "U", "actinide"),
                    (3, 7, "Neptunium", "Np", "actinide"),
                    (3, 7, "Plutonium", "Pu", "actinide"),
                    (3, 7, "Americium", "Am", "actinide"),
                    (3, 7, "Curium", "Cm", "actinide"),
                    (3, 7, "Berkelium", "Bk", "actinide"),
                    (3, 7, "Californium", "Cf", "actinide"),
                    (3, 7, "Einsteinium", "Es", "actinide"),
                    (3, 7, "Fermium", "Fm", "actinide"),
                    (3, 7, "Mendelevium", "Md", "actinide"),
                    (3, 7, "Nobelium", "No", "actinide"),
                    (3, 7, "Lawrencium", "Lr", "actinide"),

                    (4, 7, "Rutherfordium", "Rf", "transition"),
                    (5, 7, "Dubnium", "Db", "transition"),
                    (6, 7, "Seaborgium", "Sg", "transition"),
                    (7, 7, "Bohrium", "Bh", "transition"),
                    (8, 7, "Hassium", "Hs", "transition"),
                    (9, 7, "Meitnerium", "Mt", "unknown"),
                    (10, 7, "Darmstadtium", "Ds", "unknown"),
                    (11, 7, "Roentgenium", "Rg", "unknown"),
                    (12, 7, "Copernicium", "Cn", "unknown"),
                    (13, 7, "Nihonium", "Nh", "unknown"),
                    (14, 7, "Flerovium", "Fl", "unknown"),
                    (15, 7, "Moscovium", "Mc", "unknown"),
                    (16, 7, "Livermorium", "Lv", "unknown"),
                    (17, 7, "Tennessine", "Ts", "unknown"),
                    (18, 7, "Oganesson", "Og", "unknown")]
        if element_number <= 0 or element_number > len(elements):
            return 0, 0, "Unknown", "?", ""
        return elements[element_number - 1]


class SolarSystem:
    @staticmethod
    def draw_now(pen=None, asteroid_belt_radius=None, comet_rotations=5):
        from math import sqrt
        pen = get_default_turtle(pen)

        def draw_orbit(x, y):
            distance = sqrt(x ** 2 + y ** 2)
            pen.seth(90)
            teleport_turtle(pen, distance, 0)
            pen.circle(distance)

        def draw_planet(x, y, size, color, name=None):
            draw_orbit(x, y)

            teleport_turtle(pen, x, y - size)
            pen.seth(0)
            pen.fillcolor(color)
            pen.begin_fill()
            pen.circle(size)
            pen.end_fill()

            teleport_turtle(pen, x, y + size)
            pen.color("black")
            pen.write(name, align="center", font=("Courier", 20, "bold"))

        def draw_asteroid_belt():
            if asteroid_belt_radius is None:
                return

            t = pen.screen.tracer()
            pen.screen.tracer(50)

            pen.shape("circle")
            for i in range(500):
                grey_amount = random.uniform(0.0, 0.4)
                pen.color(grey_amount, grey_amount, grey_amount)
                down_scaling = random.uniform(0.1, 0.4)
                pen.shapesize(down_scaling)

                # Get a random position along a straight line, and then compute the matching Y position
                y = random.uniform(-asteroid_belt_radius, asteroid_belt_radius)
                x_squared = asteroid_belt_radius**2 - y**2
                # Reintroduce the possibility for a negative sign that had to be stripped out
                x = sqrt(x_squared) * random.choice([-1, 1])

                # Shift the asteroids around a bit so they don't sit on a perfect circle
                x, y = x+random.randint(-10, 10), y+random.randint(-10, 10)

                # Avoid bias associated with quadratic equations approaching 0, by swapping X with Y
                if i % 2 == 0:
                    teleport_turtle(pen, x, y)
                else:
                    teleport_turtle(pen, y, x)

                pen.stamp()

            pen.screen.tracer(t)

        def draw_comet():
            if comet_rotations == 0:
                return

            radius = 180
            pen.speed(3)
            teleport_turtle(pen, radius, 0)
            pen.seth(90)
            pen.shape("circle")
            pen.shapesize(0.25)

            for _ in range(comet_rotations):
                for i in range(2):
                    pen.circle(radius, 90)
                    pen.circle(radius // 2, 90)

        teleport_turtle(pen, 0, 250)
        pen.write("NOT TO SCALE", align="center", font=("Courier", 14, "bold"))
        teleport_turtle(pen, 0, 220)
        pen.write("Missing many details.", align="center", font=("Courier", 14, "bold"))

        pen.speed(0)
        # draw_planet(40, 0, 20, "light blue", "Earth")
        # draw_planet(0, 120, 15, "red", "Mars")
        # draw_planet(-200, -200, 40, "brown", "Jupiter")

        draw_planet(0, 0, 20, "yellow", "Sun")
        draw_planet(0, 55, 10, "dark red", "Mercury")
        draw_planet(-50,-60, 18, "orange", "Venus")
        draw_planet(120, 20, 20, "light blue", "Earth")
        draw_planet(0, -160, 15, "red", "Mars")
        draw_planet(-220, 150, 30, "brown", "Jupiter")
        draw_planet(190, -230, 28, "goldenrod", "Saturn")
        draw_planet(-330, 40, 26, "powder blue", "Uranus")
        draw_planet(400, 20, 25, "royal blue", "Neptune")

        draw_asteroid_belt()
        draw_comet()

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

    @staticmethod
    def draw_now_version2(pen=None):
        pen = get_default_turtle(pen)
        for i in range(8):
            angle = random.randint(-30, 30)
            distance = random.randint(20, 40)
            color = random.choice(["green2","green3","green4"])
            pen.color(color)

            # Which way will the grass-strand be draw?
            pen.seth(90-angle)

            # Draw a piece of grass.
            pen.forward(distance)
            pen.backward(distance)


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

    @staticmethod
    def draw_now_version2(pen=None):
        pen = get_default_turtle(pen)
        for i in range(8):
            angle = random.randint(-30, 30)
            distance = random.randint(20, 40)
            color = random.choice(["green2", "green3", "green4"])
            pen.color(color)

            # Point up +- 30 degrees
            pen.seth(90 - angle)
            # You could also use `t.left(angle)` here for a similar effect

            # Move away from where you were last
            pen.penup()
            pen.forward(distance + 20)
            pen.pendown()

            # Draw a bubble
            pen.circle(distance)

    @staticmethod
    def print_more_info():
        print("Draw series of bubbles.")
        print("Version 2 is a variant that can be made with only small changes to DrawGrassTuft.draw_now_version2().")
        print("")
        print("You definitely need a loop to do this.")
        print("Optionally you can use random to vary sizes, and an if() to check that things don't go out of bounds.")


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

class TriangleSpammer:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.speed(0)
        pen.up()
        pen.getscreen().tracer(100)
        bound = 100

        for i in range(1000):
            pen.color(random.random(), random.random(), random.random())
            pen.goto(random.randint(-bound, bound), random.randint(-bound, bound))
            pen.seth([0, 90, 180, 270][random.randint(0, 3)])

            pen.begin_fill()
            pen.forward(random.randint(50, 150))
            pen.right(90)
            pen.forward(random.randint(50, 150))
            pen.end_fill()

        pen.getscreen().tracer(1)
        pen.ht()

        pen.color("black")
        pen.up()
        pen.goto(0, 275)
        pen.write("90° Triangles", align="center", font=("Courier", 18, "bold"))
        pen.goto(0, 255)
        pen.write("Hint: random() for colors, randint(x, y) for sizes and positions", align="center",
                  font=("Courier", 14, "bold"))
        pen.goto(0, -275)
        pen.write("turtle.getscreen().tracer(100) --> draw every 100th frame --> super speed", align="center",
                  font=("Courier", 14, "bold"))
        return pen

class Wormhole:
    @staticmethod
    def draw_now(pen=None):
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


class ZigZagEdgedShapes:
    @staticmethod
    def draw_now(pen=None, zigzags_per_line=20):
        from math import sqrt

        def zig_zag_line(total_len, zig_zags):
            h_side = total_len/zig_zags
            z_len = sqrt(h_side**2 / 2)

            pen.right(45)
            for i in range(zig_zags*2):
                pen.forward(z_len)
                pen.left(90 if i % 2 == 0 else -90)
            pen.left(45)

        pen = get_default_turtle(pen)
        pen.speed(0)
        pen.width(3)
        pen.color("black")
        teleport_turtle(pen, -100, -100)

        for edges in range(3, 7):
            for _ in range(edges):
                zig_zag_line(200, zigzags_per_line)
                pen.left(360/edges)

        return pen



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


class ColourPalette:
    @staticmethod
    def draw_now(pen=None, pixels_between_stamps=2):
        pen = get_default_turtle(pen)
        starting_tracer_rate = pen.screen.tracer()

        # This solution ends up with 65,536 calls to stamp.
        # By telling the turtle to only update its screen every x frames, we speed things up A LOT (more than speed(0))
        update_every_x_frames = 256 * 10
        pen.screen.tracer(update_every_x_frames)

        # A shrunken square shape will let the turtle draw at a pixel-level of detail.
        pen.shape("square")
        pen.shapesize(0.05)

        pen.screen.bgcolor("black")
        pen.penup()
        for x in range(-255, 256, pixels_between_stamps):
            for y in range(-255, 256, pixels_between_stamps):
                r = (x + 255) / 512
                g = (y + 255) / 512

                pen.color(r, g, 0.5)
                pen.goto(x, y)
                pen.stamp()

        # Make sure the tracer is reset otherwise the screen may seem glitchy
        pen.screen.tracer(starting_tracer_rate)
        return pen

    @staticmethod
    def print_more_info():
        print("A 2D version of DrawGradientBackground")
        print("Requires use of turtle.screen.tracer() or the draw speed will be unworkable.")
        print("Requires use of coordinate conversion logic and turtle shapesize changes.")
        print("Requires nested loops.")
        print("")
        print("Warning - our default solution draws about 65000 squares, and will result in a SLOW turtle-screen.")


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


class Jellyfish:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.color("blue")
        pen.width(4)
        pen.fillcolor("light blue")

        pen.setheading(70)
        pen.pendown()

        pen.begin_fill()
        for i in range(45):
            pen.forward(15)
            pen.left(5)

        pen.seth(30)
        bottom_coords = []
        for i in range(30):
            pen.forward(11)
            x, y = pen.position()
            bottom_coords.append((x, y))
            pen.right(2.1)

        pen.end_fill()

        pen.color("silver")
        for i in range(3, len(bottom_coords)-2, 4):
            x, y = bottom_coords[i]
            teleport_turtle(pen, x, y-2)
            pen.seth(270)
            for i in range(100):
                pen.left(random.random()*4-2)
                pen.forward(random.randint(2,4))

        pen.ht()
        return pen


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


class FakeButton:
    @staticmethod
    def draw_now(pen=None, message="Button Text"):
        pen = get_default_turtle(pen)

        pen.color("black")
        pen.width(3)

        width, height, corner_radius = 200, 50, 20
        teleport_turtle(pen, -width//2, -height//2)
        pen.seth(0)
        for distance in [width, height, width, height]:
            pen.forward(distance)
            pen.circle(corner_radius, 90)

        teleport_turtle(pen, 0, corner_radius*0.75)
        pen.write(message, align="center", font=("courier", 14, "bold"))

        pen.ht()
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


class TruthTable:
    @staticmethod
    def draw_now(pen=None):
        pen = get_default_turtle(pen)
        pen.speed(0)
        pen.width(1)
        pen.color("black")

        # Draw the main truth table
        pen.seth(-90)
        row = 0
        for a in [True, False]:
            for b in [True, False]:
                for c in [True, False]:
                    teleport_turtle(pen, 0, row*35)
                    TruthTable.draw_row(pen, a, b, c)
                    row += 1

        # Draw column headings
        teleport_turtle(pen, 0, row * 35 - 35)
        pen.seth(0)
        pen.penup()
        pen.backward(16)
        for message in ["a", "b", "c", "All?", "Any?", "ONLY\n  b?"]:
            pen.write(message, align="center", font=("Arial", 10, "bold"))
            pen.forward(37)

        # Draw a dividing line between the values, and the results
        pen.color("dark red")
        pen.down()
        pen.width(2)
        teleport_turtle(pen, 35*2+3, -30)
        pen.seth(90)
        pen.forward(280)

        pen.ht()
        return pen

    @staticmethod
    def draw_row(pen:turtle.Turtle, a, b, c):
        x, y = pen.position()
        for bool_value in [a, b, c, a and b and c, a or b or c, b and not c and not a]:
            teleport_turtle(pen, x, y)
            color = "black" if bool_value else "light grey"
            pen.fillcolor(color)

            pen.begin_fill()
            for _ in range(4):
                pen.forward(30)
                pen.right(90)
            pen.end_fill()

            x += 35

    @staticmethod
    def print_more_info():
        print("Draw a truth table.")
        print("Good practice for using conditionals, and boolean logic.")
        print("Depending on your approach, you may need many nested loops.")
        print("")
        print("There are ways to decrease the amount of nesting (like using helper functions). ")
        print("But you don't technically need them.")
        print("Extra challenges include adding spaces between blocks, and including labels for each column")


class RightAngleCalculator:
    @staticmethod
    def draw_now(pen: turtle.Turtle = None, a=3, b=3, c=None):
        from math import sqrt
        pen = get_default_turtle(pen)
        pen.color("black")

        f = ("Arial", 14, "bold")
        if None not in [a, b, c] and a**2+b**2 != c**2:
            pen.write(f"{a}² + {b}² != {c}²\nInvalid right angle triangle.", align="center", font=f)
            return

        if sum([1 for val in [a, b, c] if val is None]) > 1:
            pen.write(f"Need at least 2 values", align="center", font=f)
            return

        if a is None:
            a = sqrt(c**2 - b**2)

        if b is None:
            b = sqrt(c ** 2 - a ** 2)

        if c is None:
            c = sqrt(a ** 2 + b ** 2)

        if a == 0 or b == 0 or c == 0:
            pen.write("At least 1 edge was worked out to have a length of 0.\n" +
                      "Therefore your triangle will be a line.\nCheck that c is greater than a and b.",
                      align="center", font=f)
            return

        pen.seth(0)

        for x_mid, y_mid, x_end, y_end, letter, val in [[a/2, 0, a, 0, "a", a],
                                                        [a, b / 2, a, b, "b", b],
                                                        [a/2, b/2, 0, 0, "c", c]]:
            pen.goto(x_mid, y_mid)
            pen.write(f"{letter}={val}", align="left", font=f)
            pen.goto(x_end, y_end)

    @staticmethod
    def print_more_info():
        print("Calculate and draw a right-angle triangle from 2 edges.")
        print("You'll need to use ifs to check which of a/b/c are missing.")
        print("Drawing the triangle can just use a, b, and/or c as XY coordinates in several goto()s.")
        print("")
        print("https://en.wikipedia.org/wiki/Pythagorean_theorem")
        print("Displaying the lengths you calculate in the middle of each line is an extra challenge.")
        print("Just displaying sizes to the console is more than enough.")


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


class ParallelShapeFilling:
    @staticmethod
    def draw_now(pen=None, sides=8):
        pen = get_default_turtle(pen)
        pen.color("black")
        pen.speed(0)
        teleport_turtle(pen, -150, -150)

        # Track XY positions for the outer edges of the shape
        # coordinate_sets will end up looking like this [[(0,0),(0,1)], [(0,1),(1,1)], [(1,1),(0,0)]]
        # The above example draws a triangle (3 edges), where each is divided into ONLY a start and end (the tuples)
        coordinate_sets = []
        for i in range(sides):
            coordinate_set = []
            for segment in range(8):
                x, y = pen.position()
                coordinate_set.append((x, y))
                pen.forward(20)
            x, y = pen.position()
            coordinate_set.append((x, y))
            pen.left(360/sides)
            coordinate_sets.append(coordinate_set)

        # Connect the dots between each of the lines
        for starting_line in coordinate_sets:
            for ending_line in coordinate_sets:
                # Don't bother connecting dots that are on the same line
                if starting_line == ending_line:
                    continue

                for i in range(len(starting_line)):
                    x_start, y_start = starting_line[i]
                    x_end, y_end = ending_line[-i-1]
                    teleport_turtle(pen, x_start, y_start)
                    pen.goto(x_end, y_end)

        pen.ht()
        return pen

    @staticmethod
    def print_more_info():
        print("Draw a regular polygon where the inside is filled with parallel lines.")
        print("This is not an easy problem, and requires use of 2D lists, triply nested loops, and more.")
        print("")
        print("Suggested solution: draw a regular shape using several smaller lines.")
        print("\tFor example, when drawing a square, you might draw 20 lines in total (5 mini lines per edge).")
        print("\tTrack the XY coordinates of each of the mini-lines.")
        print("\tUse goto(x_start, y_start) and goto(x_end, y_end) to connect your various tracked coordinates.")


class AbstractAngularArt:
    @staticmethod
    def draw_now(pen: turtle.Turtle = None, background_color="light blue", colors=["dark red", "navy", "black"]):
        pen = get_default_turtle(pen)

        # Draw Bounding Box / Canvas
        pen.color("black")
        pen.fillcolor(background_color)
        pen.width(4)
        teleport_turtle(pen, -300, 300)
        pen.begin_fill()
        for _ in range(4):
            pen.forward(600)
            pen.right(90)
        pen.end_fill()

        pen.speed(0)
        # Add "art" scribbles to canvas
        for color in colors*2:
            x, y = random.randint(-300, 300), random.randint(-300, 300)
            teleport_turtle(pen, x, y)
            pen.color(color)

            pen.begin_fill()
            for i in range(random.randint(5, 15)):
                pen.goto(random.randint(-300, 300), random.randint(-300,300))
            pen.end_fill()

        pen.ht()
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

class PoolBalls:
    @staticmethod
    def draw_now(pen=None, layers=5):
        pen = get_default_turtle(pen)
        LEFT = 90 + 45
        RIGHT = 45

        pen = turtle.Turtle()

        def linear_circles(depth):
            pen.seth(RIGHT)
            pen.up()
            for i in range(depth):
                for j in range(depth - i):
                    layer = (i+j)%depth+1
                    pen.color(0.5/layer+0.1, 0.2/layer, 0.8/layer)
                    pen.stamp()
                    pen.forward(50)
                pen.backward(50 * (depth - i))
                pen.left(90)
                pen.forward(50)
                pen.right(90)
            pen.ht()
            pen.goto(0, 0)

        pen.shape('circle')
        pen.shapesize(2.5)
        pen.speed(2)
        linear_circles(layers)
        return pen

class PythagorasProof:
    @staticmethod
    def draw_now(pen=None, horizontal_edge=100, vertical_edge=200):
        from math import sqrt, acos, degrees
        pen = get_default_turtle(pen)
        pen.color("black")

        c = horizontal_edge
        b = vertical_edge

        teleport_turtle(pen, 0, -c-20)
        message = f"Warning: this problem requires trigonometry to generalise (specifically arccos)"
        pen.write(message, align="center", font=("courier", 10, "normal"))
        teleport_turtle(pen, 0, 0)

        a = sqrt(b ** 2 + c ** 2)

        # Angle between hypotenuse and first edge:
        B = acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
        B = degrees(B)

        for start_angle, distance in [[0, c], [180-B, a], [-90, b]]:
            pen.seth(start_angle)
            for i in range(5):
                pen.forward(distance / 2)
                pen.write(f"{distance:.1f}", align="center", font=("courier", 10, "bold"))
                pen.forward(distance / 2)
                pen.right(90)

        teleport_turtle(pen, -150, -50)
        pen.write(f"{c}² + {b}² == {a:.1f}²", align="center", font=("courier", 14, "bold"))
        teleport_turtle(pen, -150, -70)
        pen.write(f"{c ** 2} + {b ** 2} == {a ** 2:.1f}", align="center", font=("courier", 14, "bold"))

        pen.ht()
        return pen


class OneOverXGraph:
    @staticmethod
    def draw_now(pen=None, zoom_factor=100):
        pen = get_default_turtle(pen)
        pen.color("black")
        pen.speed(0)

        def scale_up_xy(x_value, y_value):
            return x_value * zoom_factor, y_value * zoom_factor

        def draw_axes():
            pen.shape("square")

            pen.shapesize(0.5, 0.1)

            for alignment, initial_heading in [["center", 180], ["left", 270]]:
                pen.seth(initial_heading)
                for sign in [-1, 1]:
                    pen.penup()
                    pen.goto(0, 0)
                    pen.down()
                    for i in range(1, 500 // zoom_factor+1):
                        pen.forward(zoom_factor)
                        pen.stamp()
                        pen.write(i * sign, align=alignment, font=("courier", 14, "bold"))
                    pen.right(180)

        draw_axes()

        pen.shape("circle")
        pen.shapesize(0.25)
        pen.penup()

        steps = 0
        boundary = 500//zoom_factor

        x = -boundary
        x_increment = 0.025
        while x < boundary:
            x += x_increment
            # y = 0.5*x + 2     # Y = MX + C
            # y = (2*x)**2 - 5  # Parabola
            # y = abs(x)        # Absolute value
            y = 1/x if x > 0 else 1/-x
            # y = 1/(x**2)
            y = x**3 + 2*x**2

            x_pix, y_pix = scale_up_xy(x, y)
            if abs(y_pix) > 500 or abs(y_pix) > 500:
                continue

            pen.goto(x_pix, y_pix)
            pen.stamp()

            if steps % 30 == 0:
                pen.write(f"({x:.3f}, {y:.3f})")
            steps += 1

        return pen
