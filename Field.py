from Cell import Cell

WHITE = (255, 255, 255)
# Here we implement a field class
class Field:
    MIN_BORDER_CORNER = 20
    MAX_BORDER_CORNER = 361
    def __init__(self, size):
        self.size = size

    def creating_cells(self):    # Create cells and get their coordinates
        all_cells = []
        for i in range(self.size):
            for j in range(self.size):
                x = self.MIN_BORDER_CORNER + (Cell.CELL_SIZE + Cell.MARGIN) * i
                y = self.MIN_BORDER_CORNER + (Cell.CELL_SIZE + Cell.MARGIN) * j
                all_cells.append(Cell(WHITE, x, y))
        return all_cells

    def draw(self, cells, scr):   # Draw on surface
        for cell in cells:
            cell.draw(scr)