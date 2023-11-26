import pygame

from core.enum.system import WindowParams, StaticPath


class Window:
    @staticmethod
    def init():
        pygame.init()
        pygame.display.set_caption("Pentagon")
        pygame.display.set_icon(pygame.image.load(StaticPath.ICON))
        screen = pygame.display.set_mode((WindowParams.WIDTH, WindowParams.HEIGHT))
        return screen
