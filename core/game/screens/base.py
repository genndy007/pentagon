import abc
import pygame

from core.enum.system import WindowParams


class Screen(metaclass=abc.ABCMeta):
    def __init__(self, screen: pygame.surface.Surface, clock: pygame.time.Clock):
        self.screen = screen
        self.clock = clock
        self.running = True

    def run(self):
        while self.running:
            self.draw_content()
            self.handle_events()
            self.clock.tick(WindowParams.FPS)
            pygame.display.flip()

    @abc.abstractmethod
    def handle_events(self):
        pass

    @abc.abstractmethod
    def draw_content(self):
        pass
