from config import *

score_rect_ls = []
high_score = 0


class Scoring(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.surface = score_box_surface
        self.score_surface = game_font.render(str(self.score), True, (255, 255, 255))
        self.score_rect = self.score_surface.get_rect(center=(216, 100))
        self.score_over_rect = self.score_surface.get_rect(center=(352, 220))
        self.high_score_surface = game_font.render(str(high_score), True, (255, 255, 255))
        self.high_score_rect = self.high_score_surface.get_rect(center=(216, 500))
        self.high_score_over_rect = self.score_surface.get_rect(center=(352, 285))
        self.addScore = True
        self.collision = False

    @staticmethod
    def move_score_box():
        for box in score_rect_ls:
            box.centerx -= 2
            if box.centerx <= -100:
                score_rect_ls.pop(0)
        return score_rect_ls

    def draw(self):
        for box in score_rect_ls:
            screen.blit(self.surface, box)

    def score_display(self, game_state):
        if game_state == 'main game':
            screen.blit(self.score_surface, self.score_rect)
        if game_state == 'game over':
            screen.blit(self.score_surface, self.score_over_rect)
            screen.blit(self.high_score_surface, self.high_score_over_rect)

    def update(self, bird):
        global high_score
        self.score_surface = game_font.render(str(self.score), True, (255, 255, 255))
        self.high_score_surface = game_font.render(str(high_score), True, (255, 255, 255))
        self.move_score_box()
        self.collision = False
        for box in score_rect_ls:
            if bird.bird_rect.colliderect(box):
                self.collision = True
                break
        if self.collision:
            if self.addScore:
                self.score += 1
                score_sound.play()
                if high_score <= self.score:
                    high_score = self.score
            self.addScore = False
        else:
            self.addScore = True
