import pygame

from core.enum.color import Color


class Cell:
    SIZE = 30
    MARGIN = 1

    def __init__(self, x: int, y: int, color: Color):
        self.x = x
        self.y = y
        self.color = color

    @property
    def coords(self):
        return (self.x, self.y)

    def draw(self, screen: pygame.surface.Surface):
        coords = [self.x, self.y, self.SIZE, self.SIZE]
        pygame.draw.rect(screen, self.color, coords)
