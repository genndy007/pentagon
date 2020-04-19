import pygame

# CONSTANTS
WIN_WIDTH = 800
WIN_HEIGHT = 600
CELL_SIZE = 30
MARGIN = 1
CELLS_IN_ROW = 12
FPS = 30
# ---------------

# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
# ----------------


# Initiate and create a screen surface
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pentagon")
# Handling FPS or smth
clock = pygame.time.Clock()


#### CELLS PARTITION
# Create all rects
all_rects = [[(20 + (CELL_SIZE + MARGIN) * i, 20 + (CELL_SIZE + MARGIN) * j, CELL_SIZE, CELL_SIZE)
              for i in range(CELLS_IN_ROW)] for j in range(CELLS_IN_ROW)]

# All rects colours
colours = [[WHITE for i in range(CELLS_IN_ROW)] for j in range(CELLS_IN_ROW)]
# -------------------


##### FIGURES PARTITION
# Create all figures start positions
fig_start_pos = {
    "T": [(0, 0), (0, 1), (0, 2), (1, 1), (2, 1)],
    "LADDER": [(2, 0), (2, 1), (1, 1), (1, 2), (0, 2)],
    "SWAN": [(2, 0), (2, 1), (1, 1), (0, 1), (0, 2)],
    "L": [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)],
    "ARC": [(1, 0), (0, 0), (0, 1), (0, 2), (1, 2)],
    "VERTZIG": [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)],
    "RUG": [(2, 0), (1, 0), (0, 0), (0, 1), (0, 2)],
    "STAIR": [(1, 0), (1, 1), (1, 2), (0, 2), (0, 1)],
    "ONE": [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1)],
    "ZIGZAG": [(0, 0), (0, 1), (1, 1), (1, 2), (2, 1)],
    "STICK": [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
    "PLUS": [(1, 0), (1, 1), (0, 1), (1, 2), (2, 1)]
}
# ------------------------



# Running game cycle
running = True
while running:
    # Screen filler
    screen.fill(BLACK)
    # Drawing a field
    for i in range(len(all_rects)):
        for j in range(len(all_rects[i])):
            pygame.draw.rect(screen, colours[i][j], all_rects[i][j])
    # Drawing a figure
    for cell in fig_start_pos['PLUS']:
        colours[cell[0]][cell[1]] = GREEN
    # Handling quit ability
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Managing framerate
    clock.tick(FPS)
    # Updating the whole picture
    pygame.display.update()
