import pygame

# CONSTANTS
WIN_WIDTH = 1800
WIN_HEIGHT = 768
CELL_SIZE = 30
MARGIN = 1
CELLS_IN_ROW = 12
FPS = 30
FIGURES_START_X = 450
FIGURES_START_Y = 20
# ---------------

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


#### CELLS PARTITION
# Create all cells
all_cells = [[(20 + (CELL_SIZE + MARGIN) * i, 20 + (CELL_SIZE + MARGIN) * j, CELL_SIZE, CELL_SIZE)
              for i in range(CELLS_IN_ROW)] for j in range(CELLS_IN_ROW)]


# All cells colours
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
# ALL the figures
figure_list = ["T", "LADDER", "SWAN", 'L', 'ARC', 'VERTZIG', 'RUG', 'STAIR', 'ONE', 'ZIGZAG', 'STICK', 'PLUS']
# ------------------------

# Draw a new figure at field
def figure_to_field(figure):
    colours = [[WHITE for i in range(CELLS_IN_ROW)] for j in range(CELLS_IN_ROW)]
    for cell in fig_start_pos[figure]:
        colours[cell[0]][cell[1]] = GREEN
    return colours

# Drawing single figure
def drawing_figure(posx, posy, figure):
    square_poses = []
    for cell in figure:
        pos = (posx+(CELL_SIZE+MARGIN)*cell[1], posy+(CELL_SIZE+MARGIN)*cell[0], CELL_SIZE, CELL_SIZE)
        square_poses.append(pos)
        pygame.draw.rect(screen, WHITE, pos)
    return square_poses

# Showing all the figures
def show_all_figures():
    MPX = 0
    MPY = 0
    all_poses = []
    for figure in fig_start_pos:
        if FIGURES_START_X + MPX > 1100:
            MPX = 0
            MPY += 200
        poses = drawing_figure(FIGURES_START_X + MPX, FIGURES_START_Y + MPY, fig_start_pos[figure])
        MPX += 120
        all_poses.append(poses)
    return all_poses

# Running game cycle
running = True
while running:
    # Screen filler
    screen.fill(BLACK)
    # Drawing a field
    for i in range(len(all_cells)):
        for j in range(len(all_cells[i])):
            pygame.draw.rect(screen, colours[i][j], all_cells[i][j])
    # Figure on a field
    all_poses = show_all_figures()

    # Handling events
    for event in pygame.event.get():
        # Managing quit
        if event.type == pygame.QUIT:
            running = False
        # Managing clicks on figures
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(len(all_poses)):
                for el in all_poses[i]:
                    if x > el[0] and x < el[0] + CELL_SIZE and y > el[1] and y < el[1] + CELL_SIZE:
                        colours = figure_to_field(figure_list[i])
    # Managing framerate
    clock.tick(FPS)
    # Updating the whole picture
    pygame.display.update()
