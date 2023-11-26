import sys
from typing import Type

import pygame

from core.enum.color import GUIColor
from core.enum.system import StaticPath
from core.models.gui.button import Button
from .base import Screen
from .help import HelpScreen
from .new_game import NewGameScreen


class StartScreen(Screen):
    def __init__(self, screen: pygame.surface.Surface, clock: pygame.time.Clock):
        super().__init__(screen, clock)
        self.new_game_button = Button(100, 100, 300, 100, text='New Game')
        self.load_game_button = Button(100, 225, 300, 100, text='Load Game')
        self.help_button = Button(100, 350, 300, 100, text='Help')
        self.quit_button = Button(100, 475, 300, 100, text='Quit')
        self.buttons = [self.new_game_button, self.load_game_button, self.help_button, self.quit_button]

    def draw_text(self):
        menu_font = pygame.font.Font(StaticPath.FONT, 120)
        description_font = pygame.font.Font(StaticPath.FONT, 50)
        contents = [
            ('Pentagon', menu_font, (600, 75)),
            ('Puzzle game rewritten in 2024 by', description_font, (600, 400)),
            ('Hennadii Kochev IP-91 -> KNT-213M', description_font, (600, 450))
        ]

        for row in contents:
            text, font, coords = row
            rendered = font.render(text, 1, GUIColor.WHITE)
            self.screen.blit(rendered, coords)

    def draw_content(self):
        self.screen.fill(GUIColor.BLACK)
        self.draw_text()
        for button in self.buttons:
            button.draw(self.screen)

    def handle_events(self):
        button_to_screen: dict[Button, Type[Screen]] = {
            self.new_game_button: NewGameScreen,
            self.load_game_button: HelpScreen,
            self.help_button: HelpScreen,
        }

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.is_over(event.pos):
                    sys.exit()

                for button in button_to_screen:
                    if button.is_over(event.pos):
                        menu = button_to_screen[button]
                        menu(self.screen, self.clock).run()

            if event.type == pygame.MOUSEMOTION:
                for button in self.buttons:
                    color = GUIColor.DARK_BEIGE if button.is_over(event.pos) else GUIColor.LIGHT_BEIGE
                    button.color = color
