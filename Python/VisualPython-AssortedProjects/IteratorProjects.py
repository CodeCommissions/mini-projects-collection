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
    # Take two items that can referred to via indexes, and return pairs of items.
    # This is easier than zip() on two fronts:
    #     - Requiring indexes means (nearly) no state has to be maintained
    #     - Limiting to two collections avoids needing to generalise to n-dimensional inputs.
    pass


class PermutationGenerator:
    # Take a collection of items, and re-arrange it into every possible permutation.
    # For example Permute([1,2,3]) will yield [1,2,3], [2,1,3], [1,3,2], [2,3,1], [3,1,2], [3,2,1]
    # May be too recursion-heavy.
    pass


class RandomColorGenerator:
    # A turtle-friendly beginner-friendly iterator.
    pass
