## Swiss flag homework

Draw the outline of the swiss flag (or a medical cross). Extra points if you add color.

The primary focus is on getting the conditional correct. As a hint, you're interested in toggling directions every **3rd** turn - modding by 3 can check this for you. Pay attention to the output values of `i` as they'll show you a pattern.

### Original (incorrect) conditional

```python
import turtle

pen = turtle.Turtle()
for i in range(12):
    pen.forward(50)
    pen.write(i, font=("Arial", 14, "bold"))
    pen.forward(50)
    
    if i % 4 == 0: # <-- FIX ME
        pen.left(90)
    else:
        pen.right(90)

turtle.exitonclick()
```

### Solution

```python
import turtle

pen = turtle.Turtle()
for i in range(12):
    pen.forward(50)
    pen.write(i, font=("Arial", 14, "bold"))
    pen.forward(50)

    if i % 3 == 1:
        pen.left(90)
    else:
        pen.right(90)

turtle.exitonclick()
```

Alternative version, that uses lists rather than mod:

```python
import turtle

pen = turtle.Turtle()
for i in range(12):
    pen.forward(50)
    pen.write(i, font=("Arial", 14, "bold"))
    pen.forward(50)

    if i in [1, 4, 7, 10]:
        pen.left(90)
    else:
        pen.right(90)

turtle.exitonclick()
```


## Gradient Color Homework

Add color-changing logic to bottom loop of this skeleton code. We're looking for a gradient that changes only slightly each time the loop is called, but you can use whatever colors you like.

Here are some useful tips:
 - You'll need to use `pen.color(r, g, b)` to set the color. 
 - Don't forget that by default, `color()` expects numbers from 0 to 1.
 - Experiment with different starting values, and types of changes for your `r, g, b` values. Some combination will be awesome, some will be ugly.
 - You can use an `if` to check if your `r, g, b` values go out of bounds, and cap that at 0 and 1 (or 0 and 255 if you change the color mode).

### Original black-only code

```python
import turtle


def draw_rectangle_at(pen, x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()

    pen.begin_fill()
    for i in range(4):
        if i == 0 or i == 2:
            pen.forward(400)
        else:
            pen.forward(20)
        pen.right(90)
    pen.end_fill()


t = turtle.Turtle()
t.speed("fast")
for y in range(-200, 220, 20):
    draw_rectangle_at(t, -200, y)

turtle.exitonclick()
```

### Solution

```python
import turtle


def draw_rectangle_at(pen, x, y):
    pen.up()
    pen.goto(x, y)
    pen.down()

    pen.begin_fill()
    for i in range(4):
        if i == 0 or i == 2:
            pen.forward(400)
        else:
            pen.forward(20)
        pen.right(90)
    pen.end_fill()


t = turtle.Turtle()
t.speed("fast")
r, g, b = 0.0, 0.1, 0.2
for y in range(-200, 220, 20):
    t.color(r, g, b)
    draw_rectangle_at(t, -200, y)
    b = b + 0.025

turtle.exitonclick()
```

## Bubble Homework

Convert the grass-tuft drawing program into one that draws a stream of bubbles

Don't forget to that you have `penup()` and `pendown()`

### Original grass-tuft code

```python
import turtle, random
t=turtle.Turtle()
for i in range(8):
    angle = random.randint(-30, 30)
    distance = random.randint(20, 40)
    color = random.choice(["green2","green3","green4"])
    t.color(color)

    # Which way will the grass-strand be draw?
    t.seth(90-angle)
    # Bubbles will need to change direction AND move before drawing

    # Draw a piece of grass. This should be replaced with a call to `circle(distance)`
    t.forward(distance)
    t.backward(distance)

turtle.exitonclick()
```

### Solution

```python
import turtle, random
t=turtle.Turtle()
for i in range(8):
    angle = random.randint(-30, 30)
    distance = random.randint(20, 40)
    color = random.choice(["green2","green3","green4"])
    t.color(color)
    
    # Point up +- 30 degrees
    t.seth(90-angle)
    # You could also use `t.left(angle)` here for a similar effect

    # Move away from where you were last
    t.penup()
    t.forward(distance+20)
    t.pendown()

    # Draw a bubble
    t.circle(distance)

turtle.exitonclick()
```