import turtle


class Exosketch:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(5)
        self.pen.width(2)

    def run_now(self):
        def up():
            self.pen.seth(90)
            self.pen.forward(50)

        def down():
            self.pen.seth(-90)
            self.pen.forward(50)

        def left():
            self.pen.seth(180)
            self.pen.forward(50)

        def right():
            self.pen.seth(0)
            self.pen.forward(50)

        self.pen.screen.listen()

        self.pen.write("WASD or arrow keys to move")
        self.pen.screen.onkeypress(up, "Up")
        self.pen.screen.onkeypress(up, "w")
        self.pen.screen.onkeypress(down, "Down")
        self.pen.screen.onkeypress(down, "s")
        self.pen.screen.onkeypress(left, "Left")
        self.pen.screen.onkeypress(left, "a")
        self.pen.screen.onkeypress(right, "Right")
        self.pen.screen.onkeypress(right, "d")

        turtle.mainloop()

    @staticmethod
    def print_more_info():
        print("")


class BasicCursorPainting:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(5)
        self.pen.width(2)

    def run_now(self):
        self.pen = turtle.Turtle()
        self.pen.width(3)

        def goto(x, y):
            if x >= 0 and y >= 0:
                self.pen.color("red")
            elif x < 0 and y < 0:
                self.pen.color("blue")
            elif x > 0:
                self.pen.color("black")
            else:
                self.pen.color("pink")
            self.pen.goto(x, y)

        def size_up():
            w = self.pen.width()
            self.pen.width(w + 1)

        def size_down():
            w = self.pen.width()
            self.pen.width(w - 1)

        def toggle_pen(x, y):
            print("Toggle")
            if self.pen.isdown():
                self.pen.penup()
            else:
                self.pen.pendown()

        self.pen.screen.listen()
        self.pen.write("LMB - go to cursor. RMB - toggle pen-up. '-+' change width.")
        self.pen.screen.onclick(goto, 1)  # Left
        self.pen.screen.onclick(goto, 2)  # Middle
        self.pen.screen.onclick(toggle_pen, 3)  # Right

        self.pen.screen.onkeypress(size_up, "+")
        self.pen.screen.onkeypress(size_down, "-")

        turtle.mainloop()

    @staticmethod
    def print_more_info():
        print("")

