import sys
import pygame

from core.enum.color import GUIColor
from core.enum.system import StaticPath
from core.game.internal.utils import text_file_lines
from core.models.gui.button import Button
from .base import Screen


class HelpScreen(Screen):
    def __init__(self, screen: pygame.surface.Surface, clock: pygame.time.Clock):
        super().__init__(screen, clock)
        self.back_to_menu_button = Button(100, 600, 300, 100, text='Back to Menu')

    def draw_help(self):
        font = pygame.font.Font(StaticPath.FONT, 30)
        draw_counter = 0
        for line in text_file_lines(StaticPath.HELP):
            help_text = font.render(line, 1, GUIColor.WHITE)
            coords = (50, 100 + draw_counter)
            self.screen.blit(help_text, coords)
            draw_counter += 30

    def draw_content(self):
        self.screen.fill(GUIColor.BLACK)
        self.back_to_menu_button.draw(self.screen)
        self.draw_help()

    def handle_events(self):
        buttons = [self.back_to_menu_button]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_to_menu_button.is_over(event.pos):
                    self.running = False

            if event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    color = GUIColor.DARK_BEIGE if button.is_over(event.pos) else GUIColor.LIGHT_BEIGE
                    button.color = color
