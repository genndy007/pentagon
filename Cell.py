import pygame

# Creating cell class
class Cell:
    CELL_SIZE = 30
    MARGIN = 1

    def __init__(self, color, x, y):  # Constructor
        self.x = x
        self.y = y
        self.coords = [x, y, self.CELL_SIZE, self.CELL_SIZE]
        self.color = color

    def draw(self, scr):  # Draw on surface
        pygame.draw.rect(scr, self.color, self.coords)