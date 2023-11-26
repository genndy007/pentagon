XY = list[int, int]
Collocation = list[list[XY]]


class PentaminoCollocation:
    T = [
        [[0, 0], [0, 1], [0, 2], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2], [1, 1], [1, 0]],
        [[2, 0], [2, 1], [2, 2], [1, 1], [0, 1]],
        [[0, 0], [1, 0], [2, 0], [1, 1], [1, 2]],
    ]
    LADDER = [
        [[2, 0], [2, 1], [1, 1], [1, 2], [0, 2]],
        [[0, 0], [1, 0], [1, 1], [2, 1], [2, 2]],
        [[2, 0], [1, 0], [1, 1], [0, 1], [0, 2]],
        [[0, 0], [0, 1], [1, 1], [1, 2], [2, 2]],
    ]
    SWAN = [
        [[2, 0], [2, 1], [1, 1], [0, 1], [0, 2]],
        [[0, 0], [1, 0], [1, 1], [1, 2], [2, 2]],
    ]
    L = [
        [[0, 0], [1, 0], [2, 0], [3, 0], [3, 1]],
        [[1, 0], [0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [0, 1], [1, 1], [2, 1], [3, 1]],
        [[1, 0], [1, 1], [1, 2], [1, 3], [0, 3]],
    ]
    ARC = [
        [[1, 0], [0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 0], [0, 1], [1, 1], [2, 1], [2, 0]],
        [[0, 0], [1, 0], [1, 1], [1, 2], [0, 2]],
        [[0, 1], [0, 0], [1, 0], [2, 0], [2, 1]],
    ]
    VERTZIG = [
        [[0, 0], [1, 0], [1, 1], [2, 1], [3, 1]],
        [[1, 0], [1, 1], [1, 2], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [2, 0], [2, 1], [3, 1]],
        [[1, 0], [1, 1], [0, 1], [0, 2], [0, 3]],
    ]
    RUG = [
        [[2, 0], [1, 0], [0, 0], [0, 1], [0, 2]],
        [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]],
        [[2, 0], [2, 1], [2, 2], [1, 2], [0, 2]],
        [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]],
    ]
    STAIR = [
        [[1, 0], [1, 1], [1, 2], [0, 2], [0, 1]],
        [[0, 0], [1, 0], [2, 0], [1, 1], [2, 1]],
        [[0, 0], [1, 0], [1, 1], [0, 1], [0, 2]],
        [[0, 0], [1, 0], [0, 1], [1, 1], [2, 1]],
    ]
    ONE = [
        [[1, 0], [0, 1], [1, 1], [2, 1], [3, 1]],
        [[1, 0], [1, 1], [1, 2], [0, 2], [1, 3]],
        [[0, 0], [1, 0], [2, 0], [2, 1], [3, 0]],
        [[0, 0], [0, 1], [1, 1], [0, 2], [0, 3]],
    ]
    ZIGZAG = [
        [[0, 0], [0, 1], [1, 1], [1, 2], [2, 1]],
        [[1, 0], [1, 1], [2, 1], [1, 2], [0, 2]],
        [[1, 0], [0, 1], [1, 1], [2, 1], [2, 2]],
        [[2, 0], [1, 0], [1, 1], [0, 1], [1, 2]],
    ]
    STICK = [
        [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]],
        [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],
    ]
    PLUS = [
        [[1, 0], [1, 1], [0, 1], [1, 2], [2, 1]],
    ]
