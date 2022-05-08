import pygame
from config import floor, screen


class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.ground = floor
        self.x_pos = 0

    def draw_ground(self):
        screen.blit(floor, (self.x_pos, 650))
        screen.blit(floor, (self.x_pos + 432, 650))

    def update(self):
        self.draw_ground()
        self.x_pos -= 2
        if self.x_pos <= -432:
            self.x_pos = 0
