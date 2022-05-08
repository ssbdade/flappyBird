import pygame
import random
from config import *

pipe_list = []


def move_pipe():
    for pipe in pipe_list:
        pipe.centerx -= 2
        if pipe_list[0][0] < -300:
            pipe_list.pop(0)
    return pipe_list


class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.blank = BLANK
        self.surface = pipe_surface
        self.blank_surface = score_box_surface

    def draw(self):
        for i in range(len(pipe_list)):
            flip_pipe = pygame .transform.flip(self.surface, False, True)
            if i % 2 == 1:
                screen.blit(flip_pipe, pipe_list[i])
            else:
                screen.blit(self.surface, pipe_list[i])

    def update(self):
        move_pipe()
        self.draw()

    def create_pipe(self):
        random_pipe_pos = random.choice(pipe_height)
        bottom_pipe = self.surface.get_rect(midtop=(500, random_pipe_pos))
        score_rect = self.blank_surface.get_rect(midtop=(550, random_pipe_pos - 234))
        top_pipe = self.surface.get_rect(midtop=(500, random_pipe_pos - self.blank))
        return bottom_pipe, score_rect, top_pipe
