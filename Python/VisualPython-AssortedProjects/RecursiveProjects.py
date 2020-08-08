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

