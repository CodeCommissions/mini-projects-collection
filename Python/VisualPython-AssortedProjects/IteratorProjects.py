import turtle


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
    # For example Permute([1,2,3]) will yield [1,2,3], [2,1,3], [1,3,2], [2,3,1], [3,1,2], [3,2,1]
    # May be too recursion-heavy.
    pass


class RandomColorGenerator:
    # A turtle-friendly beginner-friendly iterator.
    pass
