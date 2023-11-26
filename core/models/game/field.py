import pygame

from core.enum.color import GUIColor
from core.enum.system import WindowParams
from .cell import Cell


class Field:
    def __init__(self, size: int):
        self.size = size
        self.cells = self.create_cells()

    def create_cells(self) -> list[Cell]:
        cells = []
        for i in range(self.size):
            for j in range(self.size):
                x = WindowParams.MIN_BORDER_CORNER + (Cell.SIZE + Cell.MARGIN) * i
                y = WindowParams.MIN_BORDER_CORNER + (Cell.SIZE + Cell.MARGIN) * j
                cell = Cell(x, y, GUIColor.WHITE)
                cells.append(cell)

        return cells

    def draw(self, screen: pygame.surface.Surface):
        for cell in self.cells:
            cell.draw(screen)
