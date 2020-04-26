import pygame
from classes import Cell, Figure, Field

WIN_WIDTH = 1350
WIN_HEIGHT = 768
FPS = 30

# Standard COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (255, 0, 0)
# ----------------
# Trendy colours
GREENERY = (136, 176, 75)
ROSE = (247, 202, 201)
SERENITY = (146, 168, 209)
MARSALA = (149, 82, 81)
ORCHID = (181, 101, 167)
EMERALD = (0, 155, 119)
TANGO = (221, 65, 36)
HONEY = (214, 80, 118)
TURQ = (68, 184, 172)
MIMOSA = (239, 192, 80)
CHILI = (155, 35, 53)
LILY = (225, 93, 68)
# ----------

# Initiate and create a screen surface
pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pentagon")
# Handling FPS or smth
clock = pygame.time.Clock()




# Creating field
field = Field(12)
field_cells = field.creating_cells()

# All figures relative cell position
fig_start_pos = {
    "T": [[[0,0], [0,1], [0,2], [1,1], [2,1]], [[0,2], [1,2], [2,2], [1,1], [1,0]], [[2,0], [2,1], [2,2], [1,1], [0,1]], [[0,0], [1,0], [2,0], [1,1], [1,2]]],

    "LADDER": [[[2,0], [2,1], [1,1], [1,2], [0,2]], [[0,0], [1,0], [1,1], [2,1], [2,2]], [[2,0], [1,0], [1,1], [0,1], [0,2]], [[0,0], [0,1], [1,1], [1,2], [2,2]]],

    "SWAN": [[[2,0], [2,1], [1,1], [0,1], [0,2]], [[0,0], [1,0], [1,1], [1,2], [2,2]]],

    "L": [[[0,0], [1,0], [2,0], [3,0], [3,1]], [[1,0], [0,0], [0,1], [0,2], [0,3]], [[0,0], [0,1], [1,1], [2,1], [3,1]], [[1,0], [1,1], [1,2], [1,3], [0,3]]],

    "ARC": [[[1,0], [0,0], [0,1], [0,2], [1,2]], [[0,0], [0,1], [1,1], [2,1], [2,0]], [[0,0], [1,0], [1,1], [1,2], [0,2]], [[0,1], [0,0], [1,0], [2,0], [2,1]]],

    "VERTZIG": [[[0,0], [1,0], [1,1], [2,1], [3,1]], [[1,0], [1,1], [1,2], [0,2], [0,3]], [[0,0], [1,0], [2,0], [2,1], [3,1]], [[1,0], [1,1], [0,1], [0,2], [0,3]]],

    "RUG": [[[2,0], [1,0], [0,0], [0,1], [0,2]], [[0,0], [0,1], [0,2], [1,2], [2,2]], [[2,0], [2,1], [2,2], [1,2], [0,2]], [[0,0], [1,0], [2,0], [2,1], [2,2]]],

    "STAIR": [[[1,0], [1,1], [1,2], [0,2], [0,1]], [[0,0], [1,0], [2,0], [1,1], [2,1]], [[0,0], [1,0], [1,1], [0,1], [0,2]], [[0,0], [1,0], [0,1], [1,1], [2,1]]],

    "ONE": [[[1,0], [0,1], [1,1], [2,1], [3,1]], [[1,0], [1,1], [1,2], [0,2], [1,3]], [[0,0], [1,0], [2,0], [2,1], [3,0]], [[0,0], [0,1], [1,1], [0,2], [0,3]]],

    "ZIGZAG": [[[0,0], [0,1], [1,1], [1,2], [2,1]], [[1,0], [1,1], [2,1], [1,2], [0,2]], [[1,0], [0,1], [1,1], [2,1], [2,2]], [[2,0], [1,0], [1,1], [0,1], [1,2]]],

    "STICK": [[[0,0], [1,0], [2,0], [3,0], [4,0]], [[0,0], [0,1], [0,2], [0,3], [0,4]]],

    "PLUS": [[[1,0], [1,1], [0,1], [1,2], [2,1]]]
}
# Template for fig pos: [[], [], [], [], []]

# Creating figures
T = Figure(GREENERY, fig_start_pos["T"], 450, 20)
LADDER = Figure(ROSE, fig_start_pos["LADDER"], 600, 20)
SWAN = Figure(SERENITY, fig_start_pos["SWAN"], 750, 20)
L = Figure(MARSALA, fig_start_pos["L"], 900, 20)
ARC = Figure(ORCHID, fig_start_pos["ARC"], 1050, 20)
VERTZIG = Figure(EMERALD, fig_start_pos["VERTZIG"], 1200, 20)
RUG = Figure(TANGO, fig_start_pos["RUG"], 450, 200)
STAIR = Figure(HONEY, fig_start_pos["STAIR"], 600, 200)
ONE = Figure(TURQ, fig_start_pos["ONE"], 750, 200)
ZIGZAG = Figure(MIMOSA, fig_start_pos["ZIGZAG"], 900, 200)
STICK = Figure(CHILI, fig_start_pos["STICK"], 1050, 200)
PLUS = Figure(LILY, fig_start_pos["PLUS"], 1200, 200)

all_figures = [T, LADDER, SWAN, L, ARC, VERTZIG, RUG, STAIR, ONE, ZIGZAG, STICK, PLUS]



activated = None

running = True
while running:
    # Filling screen
    screen.fill(BLACK)
    # Drawing field
    field.draw(field_cells, screen)
    # Placing figures and getting their positions
    figure_positions = []
    for figure in all_figures:
        pos_info = figure.creating_cells()
        figure.draw(pos_info[0], screen)
        figure_positions.append(pos_info[1])

    for event in pygame.event.get():
        # Managing quit
        if event.type == pygame.QUIT:
            running = False
        # Managing clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(len(figure_positions)):
                for el in figure_positions[i]:
                    if x > el[0] and x < el[0] + Cell.CELL_SIZE and y > el[1] and y < el[1] + Cell.CELL_SIZE:
                        activated = all_figures[i]
                        if x > 20 and x < 400 and y > 20 and y < 400:
                            continue
                        else:
                            all_figures[i].startX = 20
                            all_figures[i].startY = 20
        # Managing figure movement
        if event.type == pygame.KEYDOWN:
            if activated is not None:
                if event.key == pygame.K_RIGHT:
                    activated.startX += Cell.CELL_SIZE + Cell.MARGIN
                if event.key == pygame.K_LEFT:
                    activated.startX -= Cell.CELL_SIZE + Cell.MARGIN
                if event.key == pygame.K_UP:
                    activated.startY -= Cell.CELL_SIZE + Cell.MARGIN
                if event.key == pygame.K_DOWN:
                    activated.startY += Cell.CELL_SIZE + Cell.MARGIN
                if event.key == pygame.K_SPACE:
                    activated.rotate()


    # Managing framerate
    clock.tick(FPS)
    # Updating the whole picture
    pygame.display.update()