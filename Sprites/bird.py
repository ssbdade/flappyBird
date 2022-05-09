from config import *


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 100
        self.y_pos = 384
        self.ls_bird = ls_bird
        self.ls_bird_index = ls_bird_index
        self.bird_list = self.ls_bird[self.ls_bird_index]
        self.bird_index = 0
        self.bird = bird_mid
        self.bird_rect = self.bird.get_rect(center=(self.x_pos, self.y_pos))
        self.bird_movement = 0

    def bird_animation(self):
        new_bird = self.ls_bird[self.ls_bird_index][self.bird_index]
        new_bird_rect = new_bird.get_rect(center=(100, self.bird_rect.centery))
        return new_bird, new_bird_rect

    def update(self):
        rotated_bird = self.rotate_bird(self.bird)
        screen.blit(rotated_bird, self.bird_rect)
        self.bird_animation()
        self.bird_movement += gravity
        self.bird_rect.centery += self.bird_movement

    def jump(self):
        self.bird_movement = 0
        self.bird_movement -= 7
        flap_sound.play()

    def rotate_bird(self, bird1):
        new_bird = pygame.transform.rotozoom(bird1, -self.bird_movement * 3, 1)
        return new_bird

    def change_bird(self):
        if self.ls_bird_index == 2:
            self.ls_bird_index = 0
        else:
            self.ls_bird_index += 1

    def reset(self):
        self.x_pos = 100
        self.y_pos = 384
        self.bird_index = 0
        self.bird = self.ls_bird[self.ls_bird_index][1]
        self.bird_rect = self.bird.get_rect(center=(self.x_pos, self.y_pos))
        self.bird_movement = 0
