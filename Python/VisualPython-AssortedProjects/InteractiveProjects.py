import turtle


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
        print("Create a basic \n")
        print("Do not attempt this project unless you have at least a basic understanding of trigonometry.")
        print()
        print("A real spirograph actually comes from something called a hypotrochoid")
        print("""https://en.wikipedia.org/wiki/Hypotrochoid""")
        print("This whole project is just connecting small changes in XY coordinates based on that maths.")
        print("To see some more interesting versions, change the default values of magnification, steps, R, r, and d.")
        print("If you change r or R, note that they have to be integers.")

