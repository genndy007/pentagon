import pygame

from core.enum.color import GUIColor
from core.enum.system import StaticPath


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str = ''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = GUIColor.LIGHT_BEIGE

    def draw(self, screen: pygame.surface.Surface):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text:
            font = pygame.font.Font(StaticPath.FONT, 40)
            text = font.render(self.text, 1, GUIColor.BLACK)
            coords = (
                self.x + (self.width / 2 - text.get_width() / 2),
                self.y + (self.height / 2 - text.get_height() / 2),
            )
            screen.blit(text, coords)

    def is_over(self, pos):
        mouse_x, mouse_y = pos
        if self.x < mouse_x < self.x + self.width and self.y < mouse_y < self.y + self.height:
            return True

        return False



