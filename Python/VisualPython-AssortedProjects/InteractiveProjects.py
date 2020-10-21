import turtle, time
import BeginnerProjects


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

        self.pen.write("LMB - go to cursor. RMB - toggle pen-up. '-+' change width.")

        self.pen.screen.listen()
        self.pen.screen.onclick(goto, 1)  # Left
        self.pen.screen.onclick(goto, 2)  # Middle
        self.pen.screen.onclick(toggle_pen, 3)  # Right

        self.pen.screen.onkeypress(size_up, "+")
        self.pen.screen.onkeypress(size_down, "-")

        turtle.mainloop()

    @staticmethod
    def print_more_info():
        print("")


class TicTacToe:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(5)
        self.pen.width(2)
        self.next_move = "X"

    def run_now(self):
        def draw_move_at(x, y):
            BeginnerProjects.teleport_turtle(self.pen, x, y-40)
            self.pen.write(f"{self.next_move}", align="center", font=("courier", 50, "bold"))

        def make_move(x, y):
            print(x, y)
            draw_move_at(x, y)
            self.next_move = "X" if self.next_move == "O" else "O"

        def draw_grid():
            for x_start, y_start, heading in [[-200, -67, 0], [-200, 67, 0], [-67, 200, -90], [67, 200, -90]]:
                BeginnerProjects.teleport_turtle(self.pen, x_start, y_start)
                self.pen.seth(heading)
                self.pen.forward(400)

        self.pen.screen.listen()
        self.pen.screen.onclick(make_move, 1)  # 1 == Left

        draw_grid()
        self.pen.screen.onkeypress(lambda: make_move(-136, -136), "1")
        self.pen.screen.onkeypress(lambda: make_move(0, -136), "2")
        self.pen.screen.onkeypress(lambda: make_move(136, -136), "3")
        self.pen.screen.onkeypress(lambda: make_move(-136, 0), "4")
        self.pen.screen.onkeypress(lambda: make_move(0, 0), "5")
        self.pen.screen.onkeypress(lambda: make_move(136, 0), "6")
        self.pen.screen.onkeypress(lambda: make_move(-136, 136), "7")
        self.pen.screen.onkeypress(lambda: make_move(0, 136), "8")
        self.pen.screen.onkeypress(lambda: make_move(136, 136), "9")

        turtle.mainloop()

    @staticmethod
    def print_more_info():
        print("")


class SnakeSimplified:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(5)
        self.pen.width(2)
        self.win = self.pen.getscreen()
        self.quit = False

    def run_now(self):
        self.pen = turtle.Turtle()
        self.pen.width(3)

        def forward():
            self.pen.forward(10)

        def left():
            self.pen.left(3.3)

        def right():
            self.pen.right(3.3)

        def end_game():
            self.quit = True

        self.pen.screen.listen()
        self.pen.write("W/Up, A/Left, D/Right, |q|uit")

        self.pen.screen.onkeypress(forward, "Up")
        self.pen.screen.onkeypress(forward, "w")
        self.pen.screen.onkeypress(left, "Left")
        self.pen.screen.onkeypress(left, "a")
        self.pen.screen.onkeypress(right, "Right")
        self.pen.screen.onkeypress(right, "d")
        self.pen.screen.onkeypress(end_game, "q")

        while not self.quit:
            # time.sleep(0.05)
            self.pen.forward(1)
            # self.win.update()

        # turtle.mainloop()
        quit()

    @staticmethod
    def print_more_info():
        print("")

