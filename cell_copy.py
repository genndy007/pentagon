import pygame
from classes import Cell, Figure, Field, Menu
from math import sqrt, ceil
from random import randint, choice

WIN_WIDTH = 1350
WIN_HEIGHT = 768
FPS = 60
MIN_BORDER_CORNER = 20
MAX_BORDER_CORNER = 361

MIN_WIN_DIST = ceil(sqrt(2*(Cell.CELL_SIZE+Cell.MARGIN)**2))   # Minimal adequate distance for winning



# Standard COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (205, 205, 205)
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
icon = pygame.image.load('Pentagon-512.png')
pygame.display.set_icon(icon)
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
# STICK = Figure(CHILI, fig_start_pos["STICK"], 1050, 200)
PLUS = Figure(LILY, fig_start_pos["PLUS"], 1200, 200)

all_figures = [T, LADDER, SWAN, L, ARC, VERTZIG, RUG, STAIR, ONE, ZIGZAG,  PLUS] # Here was stick

desk_positions = [[475, 45], [625, 45], [775, 45], [925, 45], [1075, 45], [1225, 45], [475, 225], [625, 225], [775, 225], [925, 225], [1075, 225]] # , [1200, 200]

# Creating menu
items = [(120, 140, u'Game', (250, 250, 30), (250, 30, 250), 0),
         (130, 280, u'Help', (250, 250, 30), (250, 30, 250), 1),
         (130, 420, u'Quit', (250, 250, 30), (250, 30, 250), 2)]

game = Menu(items)
game.menu(screen)

def ArrayShuffler(arr):   # Created by me shuffler
    for times in range(20):
        place1 = randint(0, 10)
        place2 = randint(0, 10)
        arr[place1], arr[place2] = arr[place2], arr[place1]


def checking_collisions(figure_positions):    # Here we check collisions for finding
    for i in range(len(figure_positions)):    # the start solution
        for point1 in figure_positions[i]:
            x1 = point1[0]
            y1 = point1[1]
            for j in range(len(figure_positions)):
                if i == j:
                    continue
                for point2 in figure_positions[j]:
                    x2 = point2[0]
                    y2 = point2[1]
                    if sqrt((x2-x1)**2+(y2-y1)**2) < MIN_WIN_DIST:
                        return True
    return False

def checking_outside(coords):   # Checking if figure in field bounds
    for point in coords:
        if point[0] > 361 or point[1] > 361:
            return True
    return False

def CreateCellsInFieldCoords():   # Finding all cells in field coords
    coords = []
    for ypos in range(MIN_BORDER_CORNER, MAX_BORDER_CORNER+1, Cell.CELL_SIZE+Cell.MARGIN):
        for xpos in range(MIN_BORDER_CORNER, MAX_BORDER_CORNER+1, Cell.CELL_SIZE+Cell.MARGIN):
            coords.append((xpos, ypos))
    return coords

def FindingPerfectSolution():    # This will find etalon solution
    all_coords = CreateCellsInFieldCoords()
    busy_coords = []
    free_coords = []
    bot_figure_positions = []
    used_figures = []
    ArrayShuffler(all_figures)  # Shuffle figures to randomize their positions on field
    for ypos in range(MIN_BORDER_CORNER, MAX_BORDER_CORNER+1, Cell.CELL_SIZE+Cell.MARGIN):   # Checking all possible coords
        for xpos in range(MIN_BORDER_CORNER, MAX_BORDER_CORNER+1, Cell.CELL_SIZE+Cell.MARGIN):
            for figure in all_figures:   # Trying to put every figure
                if figure in used_figures:
                    continue
                # Assigning new positions to a figure
                figure.startX = xpos
                figure.startY = ypos
                pos_info = figure.creating_cells()
                # Checking if it's a good position for a figure
                bot_figure_positions.append(pos_info[1])
                num_rotations = 0
                while (checking_collisions(bot_figure_positions) or checking_outside(pos_info[1])) and num_rotations < 4: 
                    # Trying to rotate the figure 
                    figure.rotate()
                    pos_info = figure.creating_cells()
                    bot_figure_positions.pop()
                    bot_figure_positions.append(pos_info[1])
                    num_rotations += 1
                if not checking_collisions(bot_figure_positions) and not checking_outside(pos_info[1]):  # Final checking
                    # If it's a really good position then it's now belonging to the figure
                    used_figures.append(figure)
                    figure.etalonX = xpos    # Assgning etalon positions
                    figure.etalonY = ypos
                    figure.etalonPos = num_rotations
                    figure.draw(pos_info[0], screen)
                else:
                    bot_figure_positions.pop()
    # If not all figures were placed                
    if len(bot_figure_positions) != 11:
        bot_figure_positions, free_coords = FindingPerfectSolution()
        
    # Finding cells that are busy
    for figure in bot_figure_positions:
        for cell_pos in figure:
            busy_coords.append(cell_pos)
    # Now finding cells that are free, some of them will be obstacles
    for cell_pos in all_coords:
        if cell_pos not in busy_coords:
            free_coords.append(cell_pos)
    print(free_coords)
    

    return bot_figure_positions, free_coords


# Now finding that solution
bot_figure_positions, free_coords = FindingPerfectSolution()
# Getting figures back to desk
for i in range(len(all_figures)):
    all_figures[i].startX = desk_positions[i][0]
    all_figures[i].startY = desk_positions[i][1]
    all_figures[i].pos_index = 0
    

# GAMEPLAY ------------

activated = None
did_graying = False
running = True
while running:
    # Filling screen
    screen.fill(BLACK)
    # Drawing field
    field.draw(field_cells, screen)
    # Putting obstacles onto field 
    num_obstacles = 30
    obstacles = 0
    if not did_graying:
        did_graying = True
        while obstacles < num_obstacles:
            cell = choice(field_cells)
            if (cell.x, cell.y) in free_coords:
                cell.color = GRAY
                obstacles += 1
    # Supposing all figures are on field    
    all_on_field = True
    # Placing figures and getting their positions
    figure_positions = []
    for figure in all_figures:
        # Create figure cells
        pos_info = figure.creating_cells()
        # Collecting their positions
        figure_positions.append(pos_info[1])
        # Check if able to move
        figure.check_moving(pos_info[1])
        # Check if figure is inside the borders
        used = figure.check_borders(pos_info[1])
        # Draw figure if it is inside the borders
        if used is None:
            figure.draw(pos_info[0], screen)
        # Checking if figure is on field
        if not figure.ON_FIELD:
            all_on_field = False
        # if figure.colloc == fig_start_pos["STICK"]:
        #     print(pos_info[1])

    


    for event in pygame.event.get():
        # Managing quit
        if event.type == pygame.QUIT:
            running = False
        # Managing clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Button status
            lmb, mmb, rmb = pygame.mouse.get_pressed()
            # Where clicked
            x, y = event.pos
            
            for i in range(len(figure_positions)):
                for el in figure_positions[i]:
                    if x > el[0] and x < el[0] + Cell.CELL_SIZE and y > el[1] and y < el[1] + Cell.CELL_SIZE:
                        # Managing LMB (Choosing and selecting)
                        if lmb:
                            activated = all_figures[i]
                            # Placing figure on the field if it's not on
                            if x > MIN_BORDER_CORNER and x < MAX_BORDER_CORNER + Cell.CELL_SIZE and y > MIN_BORDER_CORNER and y < MAX_BORDER_CORNER + Cell.CELL_SIZE:
                                continue
                            else:
                                all_figures[i].ON_FIELD = True
                                all_figures[i].startX = MIN_BORDER_CORNER
                                all_figures[i].startY = MIN_BORDER_CORNER
                        # Managing RMB (Putting figure back to desk)
                        elif rmb and activated is not None and activated == all_figures[i]:
                            activated.startX = desk_positions[i][0]
                            activated.startY = desk_positions[i][1]
                            activated.ON_FIELD = False
                            activated = None
                        # Managing MMB (Putting figure to etalon place)
                        elif mmb and activated is not None and activated == all_figures[i]:
                            activated.startX = activated.etalonX
                            activated.startY = activated.etalonY
                            activated.pos_index = activated.etalonPos

        # Managing figure movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.menu(screen)
            if activated is not None:
                if event.key == pygame.K_RIGHT and activated.MOVE_RIGHT:
                    activated.startX += Cell.CELL_SIZE + Cell.MARGIN
                if event.key == pygame.K_LEFT and activated.MOVE_LEFT:
                    activated.startX -= Cell.CELL_SIZE + Cell.MARGIN
                if event.key == pygame.K_UP and activated.MOVE_UP:
                    activated.startY -= Cell.CELL_SIZE + Cell.MARGIN
                if event.key == pygame.K_DOWN and activated.MOVE_DOWN:
                    activated.startY += Cell.CELL_SIZE + Cell.MARGIN
                # Rotating the figure
                if event.key == pygame.K_SPACE:
                    activated.rotate()
    # Checking figures positions if they all on field
    if all_on_field:
        win = True
        for i in range(len(figure_positions)):
            for point1 in figure_positions[i]:
                x1 = point1[0]
                y1 = point1[1]
                for j in range(len(figure_positions)):
                    if i == j:
                        continue
                    for point2 in figure_positions[j]:
                        x2 = point2[0]
                        y2 = point2[1]
                        if sqrt((x2-x1)**2+(y2-y1)**2) < MIN_WIN_DIST:
                            win = False
        if win:
            print("YOUUUU WIINNN")



    # Managing framerate
    clock.tick(FPS)
    # Updating the whole picture
    # pygame.display.update()
    pygame.display.flip()