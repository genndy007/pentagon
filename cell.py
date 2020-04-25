import pygame

WIN_WIDTH = 1200
WIN_HEIGHT = 768
FPS = 30
MARGIN = 1

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

# Initiate and create a screen surface
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pentagon")
# Handling FPS or smth
clock = pygame.time.Clock()


class Cell:
    CELL_SIZE = 30

    def __init__(self, color, x, y):
        self.coords = [x, y, self.CELL_SIZE, self.CELL_SIZE]
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, self.coords)




class Figure:
    pass

class Field:
    def __init__(self, size):
        self.size = size

# Creating field
field = Field(12)

# Creating field cells
all_cells = []
for i in range(field.size):
    for j in range(field.size):
        x = 20 + (Cell.CELL_SIZE + MARGIN) * i
        y = 20 + (Cell.CELL_SIZE + MARGIN) * j
        all_cells.append(Cell(WHITE, x, y))






running = True
while running:
    screen.fill(LIGHT_BLUE)
    for cell in all_cells:
        cell.draw()

    for event in pygame.event.get():
        # Managing quit
        if event.type == pygame.QUIT:
            running = False

    # Managing framerate
    clock.tick(FPS)
    # Updating the whole picture
    pygame.display.update()