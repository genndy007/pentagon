import pygame

WHITE = (255, 255, 255)


class Cell:
    CELL_SIZE = 30
    MARGIN = 1

    def __init__(self, color, x, y):
        self.coords = [x, y, self.CELL_SIZE, self.CELL_SIZE]
        self.color = color

    def draw(self, scr):
        pygame.draw.rect(scr, self.color, self.coords)



class Figure:
    pos_index = 0
    MOVE_LEFT = True
    MOVE_RIGHT = True
    MOVE_UP = True
    MOVE_DOWN = True
    ON_FIELD = False

    def __init__(self, color, colloc, startX, startY):
        self.color = color
        self.colloc = colloc
        self.startX = startX
        self.startY = startY

    def creating_cells(self):
        cells = []
        all_poses = []
        for coord in self.colloc[self.pos_index]:
            pos = (self.startX+(Cell.CELL_SIZE+Cell.MARGIN)*coord[1], self.startY+(Cell.CELL_SIZE+Cell.MARGIN)*coord[0])
            cells.append(Cell(self.color, pos[0], pos[1]))
            all_poses.append(pos)
        return cells, all_poses

    def rotate(self):
        if self.pos_index >= len(self.colloc) - 1:
            self.pos_index = 0
        else:
            self.pos_index += 1

    def draw(self, cells, scr):
        for cell in cells:
            cell.draw(scr)

    def check_moving(self, coords):
        self.MOVE_LEFT = True
        self.MOVE_RIGHT = True
        self.MOVE_UP = True
        self.MOVE_DOWN = True
        for point in coords:
            if point[0] == Field.MIN_BORDER_CORNER:
                self.MOVE_LEFT = False
            if point[1] == Field.MIN_BORDER_CORNER:
                self.MOVE_UP = False
            if point[0] == Field.MAX_BORDER_CORNER:
                self.MOVE_RIGHT = False
            if point[1] == Field.MAX_BORDER_CORNER:
                self.MOVE_DOWN = False

    def check_borders(self, coords):
        used = None
        for point in coords:
            if point[0] < Field.MIN_BORDER_CORNER and self.ON_FIELD:
                self.startX += Cell.CELL_SIZE + Cell.MARGIN
                used = True
            if point[1] < Field.MIN_BORDER_CORNER and self.ON_FIELD:
                self.startY += Cell.CELL_SIZE + Cell.MARGIN
                used = True
            if point[0] > Field.MAX_BORDER_CORNER and self.ON_FIELD:
                self.startX -= Cell.CELL_SIZE + Cell.MARGIN
                used = True
            if point[1] > Field.MAX_BORDER_CORNER and self.ON_FIELD:
                self.startY -= Cell.CELL_SIZE + Cell.MARGIN
                used = True
        return used


class Field:
    MIN_BORDER_CORNER = 20
    MAX_BORDER_CORNER = 361
    def __init__(self, size):
        self.size = size

    def creating_cells(self):
        all_cells = []
        for i in range(self.size):
            for j in range(self.size):
                x = self.MIN_BORDER_CORNER + (Cell.CELL_SIZE + Cell.MARGIN) * i
                y = self.MIN_BORDER_CORNER + (Cell.CELL_SIZE + Cell.MARGIN) * j
                all_cells.append(Cell(WHITE, x, y))
        return all_cells

    def draw(self, cells, scr):
        for cell in cells:
            cell.draw(scr)

class Menu:
    def __init__(self, items):
        self.items = items
    # item = (x, y, name, colour, chosen_colour, number)
    def render(self, scr, font, num_item):
        for item in self.items:
            x, y, name, colour, chosen_colour, number = item
            if num_item == number:
                scr.blit(font.render(name, 1, chosen_colour), (x, y))
            else:
                scr.blit(font.render(name, 1, colour), (x, y))
