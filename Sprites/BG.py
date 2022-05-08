import pygame

from config import bg_load_image, screen


class BG(pygame.sprite.Sprite):
    def __init__(self):
        self.bg_image = bg_load_image
        self.x_pos = 0

    def update(self):
        screen.blit(self.bg_image, (0, 0))
