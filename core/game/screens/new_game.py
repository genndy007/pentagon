import sys

import pygame

from core.enum.color import GUIColor
from core.game.internal.obstacles import Obstacles
from core.game.internal.solution import Solution
from core.game.internal.timer import Timer
from core.models.game.field import Field
from core.models.game.pentamino import Pentamino
from core.models.gui.button import Button
from .base import Screen


class NewGameScreen(Screen):
    DESK_POSITIONS = [
        [475, 45], [625, 45], [775, 45],
        [925, 45], [1075, 45], [1225, 45],
        [475, 225], [625, 225], [775, 225],
        [925, 225], [1075, 225],
    ]

    def __init__(self, screen: pygame.surface.Surface, clock: pygame.time.Clock):
        super().__init__(screen, clock)
        self.init_buttons()
        self.init_field()
        self.timer = Timer()
        self.pentamino_activated: Pentamino | None = None

    def init_buttons(self):
        self.back_to_menu_button = Button(600, 450, 250, 75, text='Back to Menu')
        self.quit_button = Button(950, 450, 250, 75, text='Quit')
        self.save_button = Button(600, 550, 250, 75, text='Save')
        self.buttons = [self.back_to_menu_button, self.quit_button, self.save_button]

    def init_field(self):
        self.field = Field(12)
        self.pentaminoes, self.found_positions, self.free_coords = Solution.find(self.screen)
        self.obstacle_coords = Obstacles.create_coords(self.field, self.free_coords)

        for idx in range(len(self.pentaminoes)):
            pentamino = self.pentaminoes[idx]
            pentamino.start_x = self.DESK_POSITIONS[idx][0]
            pentamino.start_y = self.DESK_POSITIONS[idx][1]
            pentamino.create_cells()

    def handle_events(self):
        buttons = [self.back_to_menu_button, self.save_button, self.quit_button]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                lmb_pressed, mmb_pressed, rmb_pressed = pygame.mouse.get_pressed()
                mouse_x, mouse_y = event.pos
                # todo: continue handling clicks

                if self.back_to_menu_button.is_over(event.pos):
                    self.running = False

                if self.save_button.is_over(event.pos):
                    # todo: make saving
                    pass

                if self.quit_button.is_over(event.pos):
                    sys.exit()

            if event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    color = GUIColor.DARK_BEIGE if button.is_over(event.pos) else GUIColor.LIGHT_BEIGE
                    button.color = color

    def draw_content(self):
        self.screen.fill(GUIColor.BLACK)

        self.field.draw(self.screen)
        self.timer.draw(self.screen)
        for pentamino in self.pentaminoes:
            pentamino.draw(self.screen)

        for button in self.buttons:
            button.draw(self.screen)
