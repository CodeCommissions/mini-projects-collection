## Bubble homework

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