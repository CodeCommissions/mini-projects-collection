import turtle, random


def teleport_turtle(turt: turtle.Turtle, x, y):
    if turt.isdown():
        turt.penup()
        turt.goto(x, y)
        turt.pendown()
    else:
        turt.goto(x, y)


class RangeRemake:
    @staticmethod
    def Range(lower, upper=None, step=1):
        if upper is None:
            upper = lower
            lower = 0

        if step == 0:
            return

        check = (lambda l, u: l < u) if step > 0 else (lambda l, u: l > u)
        while check(lower, upper):
            yield lower
            lower += step

    @staticmethod
    def demo():
        pass


class ZipTwoCollections:
    # Take two items that can referred to via indexes, and yield pairs of items.
    # This is easier than zip() on two fronts:
    #   - Requiring indexes means (nearly) no state has to be maintained
    #   - Limiting to two collections avoids needing to generalise to n-dimensional inputs.
    # On top of these features, homework challenge items could include:
    #   - A `padding` item that gets returned after the shorter of the two collections is finished
    #   - A `max elements` argument that short circuits the iterator after some threshold is met.
    @staticmethod
    def Zip(collection1, collection2):
        for i in range(min(len(collection1), len(collection2))):
            yield collection1[i], collection2[i]

    @staticmethod
    def demo(pen=None, lengths=[50, 60, 70, 75], angles=[80, 90, 105, 0]):
        pen = pen if pen is not None else turtle.Turtle()

        for l, a in ZipTwoCollections.Zip(lengths, angles):
            pen.forward(l)
            pen.left(a)


class PermutationGenerator:
    # Take a collection of items, and re-arrange it into every possible permutation.
    # For example Permute([1,2,3]) will yield [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
    # May be too recursion-heavy.
    @staticmethod
    def Permute(collection):
        # This version makes multiple copies of `collection`. Essentially 1 for each permutation X total elements.
        # Far from the most efficient, it does still prevent `collection` from being altered.
        if len(collection) <= 1:
            yield collection
            return

        # Extract every element from `collection`, move it to the front, and combine it with permutations of what's left
        for i in range(len(collection)):
            copy = collection[:i] + collection[i+1:]
            for perm in PermutationGenerator.Permute(copy):
                yield [collection[i]] + perm

    @staticmethod
    def demo(pen=None, colors=["red", "blue", "cyan", "purple"]):
        pen = pen if pen is not None else turtle.Turtle()
        pen.width(6)
        teleport_turtle(pen, 0, 200)
        pen.write("Can you spot any duplicate squares?", align="center", font=("arial", 20, "bold"))

        x, y = -300, -300
        for color_set in PermutationGenerator.Permute(colors):
            teleport_turtle(pen, x, y)
            x = x + 100 if x < 200 else -300
            y = y + 100 if x == -300 else y

            for color in color_set:
                pen.color(color)
                pen.forward(80)
                pen.left(90)


class RandomColorGenerator:
    # A turtle-friendly beginner-friendly iterator.
    @staticmethod
    def GetColors(iterations):
        for _ in range(iterations):
            yield random.random(), random.random(), random.random()

    @staticmethod
    def demo(pen=None):
        # A temporary demo that just re-uses the permutations class
        colors = [c for c in RandomColorGenerator.GetColors(4)]
        PermutationGenerator.demo(pen, colors)

