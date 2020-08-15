import turtle


class KochSnowflakeDrawer:
    def __init__(self, pen=None):
        self.pen = pen or turtle.Turtle()

    def draw_edge(self, order, size):
        if order == 0:
            self.pen.forward(size)
            return

        for angle in [60, -120, 60, 0]:
            self.draw_edge(order - 1, size / 3)
            self.pen.left(angle)

    def draw_snowflake(self, order, size):
        colors = ["red", "maroon", "blue"]
        for i in range(3):
            self.pen.color(colors[i])

            self.pen.right(120)
            self.draw_edge(order, size)


class GenericShapeFractal:
    def __init__(self, pen=None):
        if pen is None:
            self.pen = turtle.Turtle()
            self.pen.speed(0)
            self.pen.up()
            self.pen.goto(-200, -200)
        else:
            self.pen = pen

    def draw(self, size=400, complexity=2, edges=3):
        for edge in range(edges):
            if complexity > 0:
                self.draw(size/2, complexity-1, edges)

            if complexity == 0:
                self.pen.down()
            else:
                self.pen.up()

            self.pen.forward(size/edges)
            self.pen.left(360 / edges)


