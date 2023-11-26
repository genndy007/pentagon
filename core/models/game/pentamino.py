import pygame

from core.enum.color import Color
from core.enum.collocation import Collocation
from core.enum.system import WindowParams
from .cell import Cell


class Pentamino:
    MOVE_LEFT = True
    MOVE_RIGHT = True
    MOVE_UP = True
    MOVE_DOWN = True
    ON_FIELD = False

    def __init__(self, start_x: int, start_y: int, color: Color, name: str, collocation: Collocation):
        self.start_x = start_x
        self.start_y = start_y
        self.color = color
        self.name = name
        self.collocation = collocation

        self.perfect_x = 20
        self.perfect_y = 20
        self.perfect_pos = 0
        self.pos_index = 0

        self.cells: list[Cell] | None = None
        self.positions = None

    def create_cells(self) ->  list[tuple[int, int]]:
        cells = []
        positions = []
        for coord in self.collocation[self.pos_index]:
            x = self.start_x + (Cell.SIZE + Cell.MARGIN) * coord[1]
            y = self.start_y + (Cell.SIZE + Cell.MARGIN) * coord[0]
            cell = Cell(x, y, self.color)
            position = (x, y)

            cells.append(cell)
            positions.append(position)

        self.cells = cells

        return positions

    def rotate(self):
        self.pos_index = 0 if self.pos_index >= len(self.collocation) - 1 else self.pos_index + 1

    def draw(self, screen: pygame.surface.Surface):
        for cell in self.cells:
            cell.draw(screen)

    def check_moving(self, coords: list[tuple[int, int]]):
        self.MOVE_LEFT = True
        self.MOVE_RIGHT = True
        self.MOVE_UP = True
        self.MOVE_DOWN = True
        for point in coords:
            x, y = point[0], point[1]
            if x == WindowParams.MIN_BORDER_CORNER:
                self.MOVE_LEFT = False
            if x == WindowParams.MAX_BORDER_CORNER:
                self.MOVE_RIGHT = False
            if y == WindowParams.MIN_BORDER_CORNER:
                self.MOVE_UP = False
            if y == WindowParams.MAX_BORDER_CORNER:
                self.MOVE_DOWN = False

    def check_borders(self, coords: list[tuple[int, int]]):
        out_of_field = False
        for point in coords:
            x, y = point[0], point[1]
            move_distance = Cell.SIZE + Cell.MARGIN
            if self.ON_FIELD:
                if x < WindowParams.MIN_BORDER_CORNER:
                    self.start_x += move_distance
                    out_of_field = True
                if x > WindowParams.MAX_BORDER_CORNER:
                    self.start_x -= move_distance
                    out_of_field = True
                if y < WindowParams.MIN_BORDER_CORNER:
                    self.start_y += move_distance
                    out_of_field = True
                if y > WindowParams.MAX_BORDER_CORNER:
                    self.start_y -= move_distance
                    out_of_field = True

        return out_of_field
