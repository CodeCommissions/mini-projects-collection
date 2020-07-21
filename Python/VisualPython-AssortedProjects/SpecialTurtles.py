import turtle


class CongaTurtle(turtle.Turtle):
    def __init__(self, length, *args, **kwargs):
        self.trailing_turtle = None
        self._parents_left_at_x = []
        self._parents_left_at_y = []
        self._parents_left_angles = []

        if length > 1:
            self.trailing_turtle = CongaTurtle(length-1)

        super().__init__(*args, **kwargs)

        colors = ["red", "magenta", "cyan", "blue", "maroon", "violet", "sienna", "turquoise"]
        c = colors[length % len(colors)]
        self.color(c)
        super().penup()
        super().forward(22*length)
        super().shape('turtle')
        super().pendown()

    def forward(self, distance):
        for i in range(distance//22):

            super(CongaTurtle, self).forward(22)
            self._belated_turn()

            if self.trailing_turtle is not None:
                self.trailing_turtle.forward(22)

        super(CongaTurtle, self).forward(distance % 22)
        self._belated_turn()

        if self.trailing_turtle is not None:
            self.trailing_turtle.forward(distance % 22)

    def _belated_turn(self):
        x,y = self.pos()

        if len(self._parents_left_at_x) > 0 and self._parents_left_at_x[-1] == x and self._parents_left_at_y[-1] == y:
            self.left(self._parents_left_angles.pop())
            self._parents_left_at_x.pop()
            self._parents_left_at_y.pop()

    def speed(self, spd):
        super().speed(spd)
        if self.trailing_turtle is not None:
            super().speed(spd)

    def left(self, angle):
        if self.trailing_turtle is not None:
            x, y = self.pos()
            self.trailing_turtle._parents_left_at_x.append(x)
            self.trailing_turtle._parents_left_at_y.append(y)
            self.trailing_turtle._parents_left_angles.append(angle)

        super().left(angle)

    def right(self, angle):
        self.left(-angle)


class RainbowTurtle(turtle.Turtle):
    def __init__(self, colors=None, *args, **kwargs):
        self._forward_steps = 0

        if colors is None:
            self._colors = ["red", "orange", "black", "blue", "indigo"]
        else:
            self._colors = colors

        super().__init__(*args, **kwargs)
        self.width(4)

    def forward(self, distance):
        color_index = self._forward_steps % len(self._colors)
        self.color(self._colors[color_index])
        self._forward_steps += 1

        super().forward(distance)

    def backward(self, distance):
        self.forward(-distance)


class Demos:
    @staticmethod
    def conga_turtle_demo():
        pen = CongaTurtle(5)

        pen.speed(10)
        for i in range(6):
            pen.forward(22 * 6)
            pen.left(60)

    @staticmethod
    def rainbow_turtle_demo():
        pen = RainbowTurtle()
        pen.speed(1)
        screen = turtle.Screen()

        for i in range(5, 15):
            pen.forward(i*20)
            pen.left(90)

        return pen, screen