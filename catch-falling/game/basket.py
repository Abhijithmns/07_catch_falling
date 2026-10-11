"""
Basket: the player-controlled catcher at the bottom of the screen.
"""

import pygame


class Basket:
    def __init__(self, x, y, width=90, height=24, speed=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.boosted_frames = 0
        self.normal_speed = speed
        self.boost_speed = speed

    def move(self, direction, bounds_width):
        """Move by `direction` (-1 left, 0 none, +1 right) at the basket's
        speed, keeping the whole basket inside [0, bounds_width]."""
        self.x += direction * self.speed
        half = self.width / 2
        self.x = max(half, min(bounds_width - half, self.x))

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.width / 2), int(self.y - self.height / 2),
            self.width, self.height,
        )
