import pygame

from core.enum.system import WindowParams
from core.models.game.cell import Cell
from core.models.game.pentamino import Pentamino
from .figures import Pentaminoes
from .rules import Rules
from .utils import array_shuffle


class Solution:
    MAX_ROTATIONS = 4

    @staticmethod
    def cells_in_field_coords():
        coords = []
        start = WindowParams.MIN_BORDER_CORNER
        stop = WindowParams.MAX_BORDER_CORNER + 1
        step = Cell.SIZE + Cell.MARGIN
        for y_pos in range(start, stop, step):
            for x_pos in range(start, stop, step):
                coords.append((x_pos, y_pos))

        return coords

    @classmethod
    def find(cls, screen: pygame.surface.Surface):
        busy_coords, free_coords, found_positions, used_pentaminoes = [], [], [], []
        pentaminoes: list[Pentamino] = array_shuffle(Pentaminoes.init())

        start = WindowParams.MIN_BORDER_CORNER
        stop = WindowParams.MAX_BORDER_CORNER + 1
        step = Cell.SIZE + Cell.MARGIN
        for y_pos in range(start, stop, step):
            for x_pos in range(start, stop, step):
                for pentamino in pentaminoes:
                    if pentamino in used_pentaminoes:
                        continue

                    pentamino.start_x = x_pos
                    pentamino.start_y = y_pos
                    positions = pentamino.create_cells()
                    found_positions.append(positions)
                    num_rotations = 0
                    while (Rules.collisions(found_positions) or Rules.outside(positions)) and num_rotations < cls.MAX_ROTATIONS:
                        pentamino.rotate()
                        num_rotations += 1
                        positions = pentamino.create_cells()
                        found_positions.pop()
                        found_positions.append(positions)
                    if not Rules.collisions(found_positions) and not Rules.outside(positions):
                        used_pentaminoes.append(pentamino)
                        pentamino.perfect_x = x_pos
                        pentamino.perfect_y = y_pos
                        pentamino.perfect_pos = pentamino.pos_index
                    else:
                        found_positions.pop()

        if len(found_positions) != len(pentaminoes):
            pentaminoes, found_positions, free_coords = cls.find(screen)

        for position in found_positions:
            for cell_position in position:
                busy_coords.append(cell_position)

        coords = cls.cells_in_field_coords()
        for cell_position in coords:
            if cell_position not in busy_coords:
                free_coords.append(cell_position)

        return pentaminoes, found_positions, free_coords
