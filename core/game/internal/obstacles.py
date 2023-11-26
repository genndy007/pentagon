import random

from core.enum.color import GUIColor
from core.models.game.field import Field


class Obstacles:
    # todo: adjust gameplay
    AMOUNT = 300

    @classmethod
    def create_coords(cls, field: Field, free_coords: list[tuple[int, int]]):
        obstacles_coords = []
        obstacles_amount = 0
        while obstacles_amount < cls.AMOUNT:
            cell = random.choice(field.cells)
            if cell.coords in free_coords:
                cell.color = GUIColor.GRAY
                obstacles_amount += 1
                obstacles_coords.append(cell.coords)

        return obstacles_coords
