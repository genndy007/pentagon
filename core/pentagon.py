import pygame

from core.game.screens.start import StartScreen
from core.game.window import Window


class Pentagon:
    def run(self):
        screen = Window.init()
        clock = pygame.time.Clock()
        StartScreen(screen, clock).run()
