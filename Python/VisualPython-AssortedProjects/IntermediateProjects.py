## https://en.wikipedia.org/wiki/Hypotrochoid
import turtle
import random
import time
from math import sin, cos, pi, gcd


def teleport_turtle(turt: turtle.Turtle, x, y):
    if turt.isdown():
        turt.penup()
        turt.goto(x, y)
        turt.pendown()
    else:
        turt.goto(x, y)


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


class MazeMaker:
    def __init__(self, width=40, height=40):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.width, self.height = width, height

        self.map_layout = [[False for _ in range(height)] for _ in range(width)]

    def draw_now(self):
        new_x, new_y = 0, 0
        x_offset, y_offset = self.width * 10 / 2, self.height * 10 / 2
        self.draw_border()

        MazeMaker.jump_turtle_to(self.pen, new_x * 10 - x_offset, new_y * 10 - y_offset)
        self.map_layout[new_x][new_y] = True
        while True:
            # Find what directions are available to move.
            possible_directions = self.get_valid_movement_coords(new_x, new_y)
            if len(possible_directions) == 0:
                # If you're trapped, find a new starting spot
                new_coords = MazeMaker.get_valid_start_coords(self.map_layout)
                if new_coords is None:
                    # If there are no more empty starting spots, then stop drawing the maze.
                    break

                # Jump to the new start location, mark it as used before drawing from it.
                new_x, new_y = new_coords
                MazeMaker.jump_turtle_to(self.pen, new_x * 10 - x_offset, new_y * 10 - y_offset)
                self.map_layout[new_x][new_y] = True
                continue

            new_x, new_y = random.choice(possible_directions)
            self.map_layout[new_x][new_y] = True
            self.pen.goto(new_x * 10 - x_offset, new_y * 10 - y_offset)

        self.pen.ht()

    def get_valid_movement_coords(self, curr_x, curr_y):
        directions = []

        if curr_x > 0 and not self.map_layout[curr_x - 1][curr_y]:
            directions.append([curr_x - 1, curr_y])
        if curr_x < self.width - 1 and not self.map_layout[curr_x + 1][curr_y]:
            directions.append([curr_x + 1, curr_y])
        if curr_y > 0 and not self.map_layout[curr_x][curr_y - 1]:
            directions.append([curr_x, curr_y - 1])
        if curr_y < self.height - 1 and not self.map_layout[curr_x][curr_y + 1]:
            directions.append([curr_x, curr_y + 1])

        return directions

    def draw_border(self):
        self.pen.seth(90)
        width, height = self.width * 10, self.height * 10
        MazeMaker.jump_turtle_to(self.pen, -width/2, -height/2)
        for distance in [height, width, height, width]:
            self.pen.forward(distance-10)
            self.pen.right(90)

    @staticmethod
    def jump_turtle_to(pen, x, y):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()

    @staticmethod
    def get_valid_start_coords(visited_spots):
        valid_spots = []
        for row in range(len(visited_spots)):
            for col in range(len(visited_spots[row])):
                if visited_spots[row][col]:
                    continue
                valid_spots.append([row, col])

        if len(valid_spots) == 0:
            return None
        return random.choice(valid_spots)


class CellularAutomaton:
    def __init__(self, survive_counts=[2, 3], breed_counts=[3], height=40):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.width, self.height = 20, 20
        self.survive_counts, self.breed_counts = survive_counts, breed_counts

        self.map_layout = [[random.choice([1, 0]) for _ in range(self.height)] for _ in range(self.width)]

    def draw_now(self):
        while True:
            self.pen.screen.clearscreen()
            self.pen.getscreen().tracer(100, 0)
            teleport_turtle(self.pen, -15, 15)
            self.pen.shapesize(30)
            self.pen.color("grey")
            self.pen.stamp()
            self.pen.color("black")
            self.pen.shapesize(1)
            temp_map = [[0 for _ in range(self.height)] for _ in range(self.width)]
            for row in range(self.height):
                for col in range(self.width):
                    x, y = self._get_valid_movement_coords(row, col)
                    teleport_turtle(self.pen, x, y)
                    neighbors = self._sum_neighbors(row, col)
                    if neighbors in self.survive_counts and self.map_layout[row][col] == 1 or \
                       neighbors in self.breed_counts and self.map_layout[row][col] == 0:
                        temp_map[row][col] = 1
                        self.pen.stamp()
            self.pen.screen.update()
            self.map_layout = temp_map
            time.sleep(1)

    def _get_valid_movement_coords(self, row, col):
        x = row * 30 - 300
        y = 300 - col * 30
        return x, y

    def _sum_neighbors(self, row, col):
        s = 0
        for r in [-1, 0, 1]:
            for c in [-1, 0, 1]:
                if r == c == 0:
                    continue
                if row+r >= 0 and row+r < self.height and col + c >= 0 and col + c < self.width-1:
                    s += self.map_layout[row+r][col+c]
        return s


class PandemicTurtleSimulator:
    def __init__(self, turtle_count=20):
        self.turtles = [turtle.Turtle() for _ in range(turtle_count)]

        for t in self.turtles:
            t.is_sick = False
            t.speed(0)
            t.penup()
            x, y = random.randint(-280,280), random.randint(-280,280)
            t.goto(x, y)
            t.seth(random.randint(0,360))
            t.shape("turtle")
            t.color("black")

        seed_sickness = random.choice(self.turtles)
        seed_sickness.is_sick = True
        seed_sickness.color("red")

    def _spread_sickness(self, t : turtle.Turtle):
        from math import sqrt
        for other in self.turtles:
            if other == t:
                continue

            x, y = t.position()
            new_x, new_y = other.position()
            distance = sqrt((x-new_x)**2 + (y-new_y)**2)

            if distance < 20 and (t.is_sick or other.is_sick):
                other.is_sick = True
                other.color("red")
                t.is_sick = True
                t.color("red")

    def _move_turtle(self, turtle_to_move : turtle.Turtle):
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

        turtle_to_move.goto(x, y)

        angle = random.randint(0, 30)-15

        turtle_to_move.right(angle)

        distance = random.randint(10,30)
        turtle_to_move.forward(distance)

    def draw_single_step(self):
        for t in self.turtles:
            self._move_turtle(t)
            self._spread_sickness(t)

    def draw_now(self):
        turtle.penup()
        turtle.goto(-300, 300)
        turtle.pendown()
        for i in range(4):
            turtle.forward(600)
            turtle.right(90)
        turtle.ht()

        for _ in range(500):
            sick_count = sum([1 for t in self.turtles if t.is_sick])
            print(sick_count)
            if sick_count == len(self.turtles):
                break
            self.draw_single_step()

