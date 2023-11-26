import time

import pygame

from core.enum.color import GUIColor
from core.enum.system import StaticPath


class Timer:

    def __init__(self):
        self.start_time = time.time()

    def draw(self, screen: pygame.surface.Surface):
        content = f"Timer: {int(time.time() - self.start_time)}"
        font = pygame.font.Font(StaticPath.FONT, 40)
        text = font.render(content, 1, GUIColor.WHITE)
        screen.blit(text, (100, 475))
