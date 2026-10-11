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
        self.normal_speed = speed
        self.boost_speed = speed * 2
        self.speed = self.normal_speed
        self.boost_duration_frames = 150
        self.boost_cooldown_frames = 60
        self.boosted_frames = 0
        self.cooldown_frames = 0

    def activate_boost(self):
        """Activate temporary speed boost if available."""
        if self.can_boost:
            self.boosted_frames = self.boost_duration_frames
            self.speed = self.boost_speed
            return True
        return False

    def update(self):
        """Update boost timers and restore normal speed when expired."""
        if self.boosted_frames > 0:
            self.boosted_frames -= 1
            if self.boosted_frames == 0:
                self.speed = self.normal_speed
                self.cooldown_frames = self.boost_cooldown_frames
        elif self.cooldown_frames > 0:
            self.cooldown_frames -= 1

    @property
    def is_boosted(self):
        return self.boosted_frames > 0

    @property
    def can_boost(self):
        return self.boosted_frames == 0 and self.cooldown_frames == 0

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
