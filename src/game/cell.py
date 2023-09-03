import pygame as p
from src.game.settings import CELL_SIZE


class Cell:
    COLORS = {0: ("black", (0, 0, 0)),
              1: ("white", (255, 255, 255))}
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self._state = state
        self._center = self.set_center()

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state

    @property
    def center(self):
        return self._center

    def __repr__(self):
        return f'Cell({self.x}, {self.y}, {self.state})'

    def __str__(self):
        return f'x:{self.x}, y:{self.y}, {self.state}'

    def set_center(self):
        return self.x * CELL_SIZE + CELL_SIZE // 2, self.y * CELL_SIZE + CELL_SIZE // 2

    def get_color(self):
        return self.COLORS[self.state][1]

    def draw_circle(self, screen):
        center_left = self.x * CELL_SIZE
        center_top = self.y * CELL_SIZE
        radius = CELL_SIZE // 2
        p.draw.circle(screen, "black", (center_left, center_top), radius)

    def draw_square(self, screen, border_width=0, border_radius=0, color=None):
        left = self.x * CELL_SIZE
        top = self.y * CELL_SIZE
        height = CELL_SIZE
        width = CELL_SIZE
        if not color:
            color = self.get_color()
        p.draw.rect(screen, color, (left, top, width, height), border_radius=border_radius)
        if border_width:
            p.draw.rect(screen, 'black', (left, top, width, height), width=border_width, border_radius=border_radius)

    def render_text(self, font, text, screen, color=(0, 0, 0)):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=self.center)
        screen.blit(text_surface, text_rect.topleft)
