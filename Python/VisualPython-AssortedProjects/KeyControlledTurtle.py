"""
This basic game of tic tac toe is a mid-point in an ongoing student project.
The TODOs are meant as both plans for upcoming lessons, and homework.
"""
import turtle


next_player = "x"
def draw_x():
    for heading in [45,45+90]:
        turtle.setheading(heading)
        turtle.forward(50)
        turtle.backward(100)
        turtle.forward(50)


def draw_o():
    turtle.setheading(0)
    radius = 50

    turtle.penup()
    x, y = turtle.position()
    turtle.goto(x, y - radius)
    turtle.pendown()

    turtle.circle(radius)


def clickLeft(x, y):
    '''
    Draws an X or O depending on who's turn it is.
    '''
    # TODO - 1 - check if something is already being drawn. If it is, then don't let a new drawing begin.

    # TODO - 2 - Add a counter that tracks how many moves have been made.

    # TODO - 3 - Add a check for various game-over conditions:
    #  If total moves is 9 or more, stop this function.
    #  (once available) If clickRight has been activated its gameover variable will stop this function too.

    # TODO - 4 -  Compare X and Y against the grid's position. Make sure the turtle only draws INSIDE the grid
    #  (exactly where inside the grid doesn't matter yet)

    # TODO - 5 - Adjust the XY coordinates, so that shapes are drawn in the centre of each square.

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    global next_player
    if next_player == "x":
        next_player = "o"
        draw_x()
    else:
        next_player = "x"
        draw_o()


def clickRight(x, y):
    # TODO - 6 - draw a line centered at XY (just horizontal is fine for now). Indicates a win.

    # TODO - 7 - add a game-over variable that gets set to true when a line is drawn.

    # TODO - 8 - The same XY boundary checks as clickLeft, so the line is centred on a row.

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    style = ('Courier', 8, 'normal')
    turtle.write(f'{x},{y}', font=style, align='center')


def end():
    turtle.bye()


def draw_grid():
    coords = [[-200, -70, 200, -70], [-200, 70, 200, 70], [-70, -200, -70, 200], [70, -200, 70, 200]]
    for start_x, start_y, stop_x, stop_y in coords:
        turtle.penup()
        turtle.goto(start_x, start_y)
        turtle.pendown()
        turtle.goto(stop_x, stop_y)


draw_grid()

turtle.onscreenclick(clickLeft, 1)
turtle.onscreenclick(clickRight, 3)
turtle.onkey(end, "Escape")

turtle.listen()
turtle.mainloop()  # This will make sure the program continues to run
