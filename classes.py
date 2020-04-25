import pygame
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
# ----------------


class Cell:
    CELL_SIZE = 30
    MARGIN = 1

    def __init__(self, color, x, y):
        self.coords = [x, y, self.CELL_SIZE, self.CELL_SIZE]
        self.color = color

    def draw(self, scr):
        pygame.draw.rect(scr, self.color, self.coords)




class Figure:
    def __init__(self, color, colloc, startX, startY):
        self.color = color
        self.colloc = colloc
        self.startX = startX
        self.startY = startY

    def creating_cells(self):
        cells = []
        for coord in self.colloc:
            pos = (self.startX+(Cell.CELL_SIZE+Cell.MARGIN)*coord[1], self.startY+(Cell.CELL_SIZE+Cell.MARGIN)*coord[0])
            cells.append(Cell(self.color, pos[0], pos[1]))
        return cells

    def draw(self, cells, scr):
        for cell in cells:
            cell.draw(scr)



class Field:
    def __init__(self, size):
        self.size = size

    def creating_cells(self):
        all_cells = []
        for i in range(self.size):
            for j in range(self.size):
                x = 20 + (Cell.CELL_SIZE + Cell.MARGIN) * i
                y = 20 + (Cell.CELL_SIZE + Cell.MARGIN) * j
                all_cells.append(Cell(WHITE, x, y))
        return all_cells

    def draw(self, cells, scr):
        for cell in cells:
            cell.draw(scr)