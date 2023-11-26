from math import sqrt, ceil

from core.enum.system import WindowParams
from core.models.game.cell import Cell


class Rules:
    MINIMUM_WIN_DISTANCE = ceil(sqrt(2 * (Cell.SIZE + Cell.MARGIN) ** 2))

    @classmethod
    def collisions(cls, figure_positions):
        for i in range(len(figure_positions)):
            for point1 in figure_positions[i]:
                x1, y1 = point1[0], point1[1]
                for j in range(len(figure_positions)):
                    if i == j:
                        continue
                    for point2 in figure_positions[j]:
                        x2, y2 = point2[0], point2[1]
                        if sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) < cls.MINIMUM_WIN_DISTANCE:
                            return True

        return False

    @staticmethod
    def outside(coords):
        for point in coords:
            x, y = point[0], point[1]
            if x > WindowParams.MAX_BORDER_CORNER or y > WindowParams.MAX_BORDER_CORNER:
                return True

        return False
