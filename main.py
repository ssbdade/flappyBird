import sys

from Sprites.Score import score_rect_ls, Scoring
from Sprites.bird import Bird
from config import *

from Sprites.BG import BG
from Sprites.ground import Ground
from Sprites.Pipe import Pipe, pipe_list

pygame.mixer.pre_init()
pygame.init()
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()
bg = BG()
floor = Ground()
bird = Bird()
PIPE = Pipe()
score_box = Scoring()
fpsClock = pygame.time.Clock()
pygame.time.set_timer(spawn_pipe, 1200)
pygame.time.set_timer(bird_flap, 200)


def gameStart_display():
    bg.update()
    floor.draw_ground()
    screen.blit(message, message_rect)


def is_game_over():
    for pipe in pipe_list:
        if bird.bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird.bird_rect.top <= 0 or bird.bird_rect.bottom >= 650:
        hit_sound.play()
        return False
    return True


def gameOver():
    bg.update()
    floor.draw_ground()
    bird.reset()
    screen.blit(bird.ls_bird[bird.ls_bird_index][1], bird.bird_rect)
    screen.blit(score_board_surface, score_board_rect)
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(change_bird_surface, change_bird_rect)
    score_box.score_display('game over')


def main():
    game_active = False
    game_started = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if message_rect.collidepoint(pygame.mouse.get_pos()) and not game_started:
                    game_active = True
                    game_started = True
                if change_bird_rect.collidepoint(pygame.mouse.get_pos()) and game_started and not game_active:
                    bird.change_bird()
                    die_sound.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active and game_started:
                    bird.jump()
                if event.key == pygame.K_SPACE and not game_active and game_started:
                    game_active = True
                    pipe_list.clear()
                    score_rect_ls.clear()
                    score_box.__init__()
            if event.type == spawn_pipe:
                temp_list = PIPE.create_pipe()
                pipe_list.append(temp_list[0])
                pipe_list.append(temp_list[2])
                score_rect_ls.append(temp_list[1])
            if event.type == bird_flap:
                if bird.bird_index < 2:
                    bird.bird_index += 1
                else:
                    bird.bird_index = 0
                bird.bird, bird.bird_rect = bird.bird_animation()
        if not game_started:
            gameStart_display()
        if game_active:
            bg.update()
            bird.update()
            PIPE.update()
            score_box.update(bird)
            score_box.score_display('main game')
            floor.update()
            game_active = is_game_over()
        elif not game_active and game_started:
            gameOver()
        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == '__main__':
    main()
