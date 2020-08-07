## https://en.wikipedia.org/wiki/Hypotrochoid
import turtle
from math import sin, cos, pi, gcd


class SevenSegmentDrawer:
    def __init__(self):
        self.pen = turtle.Turtle()
        self._setup_layout_maps()
        self.pen

    def _setup_layout_maps(self):
        self._number_map = \
        {1: [0, 0, 0, 1, 0, 0, 1],
         2: [1, 0, 1, 1, 1, 1, 0],
         3: [1, 0, 1, 1, 0, 1, 1],
         4: [0, 1, 1, 1, 0, 0, 1],
         5: [1, 1, 1, 0, 0, 1, 1],
         6: [1, 1, 1, 0, 1, 1, 1],
         7: [1, 0, 0, 1, 0, 0, 1],
         8: [1, 1, 1, 1, 1, 1, 1],
         9: [1, 1, 1, 1, 0, 0, 1],
         0: [1, 1, 0, 1, 1, 1, 1]}
        #    0, 1, 2, 3, 4, 5, 6

        self._segment_positions = \
        [   # X,    Y, W,  Height
            [20,    0, 100, 20],    # Top middle
            [0,     20, 20, 100],   # top left
            [20,    120, 100, 20],   # centre
            [120,   20, 20, 100],   # top right
            [0,     140, 20, 100],   # bottom left
            [20,    240, 100, 20],  # bottom centre
            [120,   140, 20, 100],   # bottom right
        ]

    def _draw_segments(self, row):
        for i in range(len(row)):
            layout = self._segment_positions[i]
            self.pen.fillcolor("light grey" if row[i] == 0 else "red")
            self.pen.penup()
            self.pen.goto(layout[0], -layout[1])
            self.pen.pendown()

            self.pen.begin_fill()
            for distance in [layout[2], layout[3], layout[2], layout[3]]:
                self.pen.forward(distance)
                self.pen.right(90)
            self.pen.end_fill()

    def draw_now(self, number, pen=None):
        self.pen.setheading(0)
        self.pen.speed(0)
        self.pen = pen if pen is not None else self.pen
        segment_layout = self._number_map[number]
        self._draw_segments(segment_layout)


class DrawTrueSpirograph:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.width(2)

        # How zoomed in and granular should the picture be.
        self.magnification = 50
        self.steps = 500

        # Set the spirograph's 3 main variables
        self.R = 4
        self.r = 5
        self.d = 1.5

    def draw_now(self):
        # Get the lowest common multiple of R and r
        lcm = abs(self.r*self.R) // gcd(self.r, self.R)
        upper_bound = 2*pi * (lcm/self.R)

        # Use these to connect the first and last points
        first_x, first_y = None, None

        theta = 0
        self.pen.penup()
        while theta <= upper_bound:
            x = (self.R-self.r)*cos(theta)+self.d*cos(theta*((self.R-self.r)/self.r))
            y = (self.R-self.r)*sin(theta)-self.d*sin(theta*((self.R-self.r)/self.r))
            self.pen.goto(x * self.magnification, y * self.magnification)

            if first_x is None:
                first_x, first_y = x, y
                self.pen.pendown()

            theta += upper_bound/self.steps

        # connect the last point to the first point
        self.pen.goto(first_x * self.magnification, first_y * self.magnification)

    @staticmethod
    def print_more_info():
        print("WARNING: This is a maths-heavy project.\n")
        print("Do not attempt this project unless you have at least a basic understanding of trigonometry.")
        print()
        print("A real spirograph actually comes from something called a hypotrochoid")
        print("""https://en.wikipedia.org/wiki/Hypotrochoid""")
        print("This whole project is just connecting small changes in XY coordinates based on that maths.")
        print("To see some more interesting versions, change the default values of magnification, steps, R, r, and d.")
        print("If you change r or R, note that they have to be integers.")
