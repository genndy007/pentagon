from Cell import Cell
from Field import Field
# Declaring figure class
class Figure:
    # pos_index = 0
    MOVE_LEFT = True
    MOVE_RIGHT = True
    MOVE_UP = True
    MOVE_DOWN = True
    ON_FIELD = False

    # Constructor
    def __init__(self, color, colloc, startX, startY, name, pos_index=0, etalonX=20, etalonY=20, etalonPos=0):
        self.pos_index = pos_index
        self.color = color
        self.colloc = colloc
        self.startX = startX
        self.startY = startY
        self.name = name
        self.etalonX = etalonX
        self.etalonY = etalonY
        self.etalonPos = etalonPos

    def creating_cells(self):   # Create cells and find their coordinates
        cells = []
        all_poses = []
        for coord in self.colloc[self.pos_index]:
            pos = (self.startX+(Cell.CELL_SIZE+Cell.MARGIN)*coord[1], self.startY+(Cell.CELL_SIZE+Cell.MARGIN)*coord[0])
            cells.append(Cell(self.color, pos[0], pos[1]))
            all_poses.append(pos)
        return cells, all_poses

    def rotate(self):   # Rotate a figure by 90 degrees
        if self.pos_index >= len(self.colloc) - 1:
            self.pos_index = 0
        else:
            self.pos_index += 1

    def draw(self, cells, scr):   # Draw cells on a surface
        for cell in cells:
            cell.draw(scr)

    def check_moving(self, coords):   # Check if figure can move in any direction on a field
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

    def check_borders(self, coords):  # Check if figure goes away out of field
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
