import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BEIGE = (255, 255, 153)
DARK_BEIGE = (255, 255, 102)

class Cell:
    CELL_SIZE = 30
    MARGIN = 1

    def __init__(self, color, x, y):
        self.x = x
        self.y = y
        self.coords = [x, y, self.CELL_SIZE, self.CELL_SIZE]
        self.color = color

    def draw(self, scr):
        pygame.draw.rect(scr, self.color, self.coords)



class Figure:
    # pos_index = 0
    MOVE_LEFT = True
    MOVE_RIGHT = True
    MOVE_UP = True
    MOVE_DOWN = True
    ON_FIELD = False

    def __init__(self, color, colloc, startX, startY, pos_index=0, etalonX=20, etalonY=20, etalonPos=0):
        self.pos_index = pos_index
        self.color = color
        self.colloc = colloc
        self.startX = startX
        self.startY = startY
        self.etalonX = etalonX
        self.etalonY = etalonY
        self.etalonPos = etalonPos

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
    WORD_LENGTH = 310
    WORD_HEIGHT = 100
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

    def menu(self, screen):
        done = True
        font_menu = pygame.font.Font('MenuFont.ttf', 100)
        index = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for item in self.items:
                if mp[0] > item[0] and mp[0] < item[0]+Menu.WORD_LENGTH and mp[1] > item[1] and mp[1] < item[1]+Menu.WORD_HEIGHT:
                    index = item[5]
            
            self.render(screen, font_menu, index)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    # Menu Navigation with keyboard
                    if event.key == pygame.K_UP:
                        if index > 0:
                            index -= 1
                    if event.key == pygame.K_DOWN:
                        if index < len(self.items) - 1:
                            index += 1
                # Navigation with mouse
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if index == 0:
                        done = False
                    elif index == 2:
                        sys.exit()

                    
            pygame.display.flip()

# Here we implement the button

class Button:
    def __init__(self, color=LIGHT_BEIGE, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, scr, outline=None):
        if outline:
            pygame.draw.rect(scr, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(scr, self.color, (self.x, self.y, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.Font('MenuFont.ttf', 60)
            text = font.render(self.text, 1, BLACK)
            scr.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):   # Here we take mouse position and compare it
        mouse_x = pos[0]
        mouse_y = pos[1]
        if mouse_x > self.x and mouse_x < self.x + self.width:
            if mouse_y > self.y and mouse_y < self.y + self.height:
                self.color = DARK_BEIGE
            else:
                self.color = LIGHT_BEIGE
        else:
            self.color = LIGHT_BEIGE