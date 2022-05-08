import pygame
pygame.init()
gravity = 0.25
FPS = 120


screen = pygame.display.set_mode((432, 768))


bg_load_image = pygame.image.load('FileGame/assets/background-night.png').convert()
bg_load_image = pygame.transform.scale2x(bg_load_image)

message = pygame.transform.scale2x(pygame.image.load('FileGame/assets/message.png')).convert_alpha()
message_rect = message.get_rect(center=(216, 284))

floor = pygame.image.load('FileGame/assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)

bird_down = pygame.transform.scale2x(pygame.image.load('FileGame/assets/yellowbird-downflap.png')).convert_alpha()
bird_mid = pygame.transform.scale2x(pygame.image.load('FileGame/assets/yellowbird-midflap.png')).convert_alpha()
bird_up = pygame.transform.scale2x(pygame.image.load('FileGame/assets/yellowbird-upflap.png')).convert_alpha()

blue_bird_down = pygame.transform.scale2x(pygame.image.load('FileGame/assets/bluebird-downflap.png')).convert_alpha()
blue_bird_mid = pygame.transform.scale2x(pygame.image.load('FileGame/assets/bluebird-midflap.png')).convert_alpha()
blue_bird_up = pygame.transform.scale2x(pygame.image.load('FileGame/assets/bluebird-upflap.png')).convert_alpha()

red_bird_down = pygame.transform.scale2x(pygame.image.load('FileGame/assets/redbird-downflap.png')).convert_alpha()
red_bird_mid = pygame.transform.scale2x(pygame.image.load('FileGame/assets/redbird-midflap.png')).convert_alpha()
red_bird_up = pygame.transform.scale2x(pygame.image.load('FileGame/assets/redbird-upflap.png')).convert_alpha()

bird_list = [bird_down, bird_mid, bird_up]
red_bird_list = [red_bird_down, red_bird_mid, red_bird_up]
blue_bird_list = [blue_bird_down, blue_bird_mid, blue_bird_up]

ls_bird = [bird_list, red_bird_list, blue_bird_list]
ls_bird_index = 0
bird_index = 0


pipe_surface = pygame.transform.scale2x(pygame.image.load("FileGame/assets/pipe-green.png")).convert()
score_box_surface = pygame.Surface((10, 234)).convert()
spawn_pipe = pygame.USEREVENT
bird_flap = pygame.USEREVENT + 1
BLANK = 750
pipe_height = [450, 425, 400, 375]
game_font = pygame.font.Font("FileGame/04B_19.TTF", 40)


play_button_surface = pygame.transform.scale2x(pygame.image.load("FileGame/assets/play_button.png")).convert()
play_button_rect = play_button_surface.get_rect(center=(216, 584))

score_board_surface = pygame.image.load('FileGame/assets/score_board.png').convert_alpha()
score_board_rect = play_button_surface.get_rect(center=(104, 184))

game_over_surface = pygame.transform.scale2x(pygame.image.load('FileGame/assets/gameover.png')).convert_alpha()
game_over_rect = game_over_surface.get_rect(center=(216, 84))


change_bird_surface = pygame.transform.scale2x(pygame.image.load('FileGame/assets/change_bird.png')).convert_alpha()
change_bird_rect = change_bird_surface.get_rect(center=(110, 464))

flap_sound = pygame.mixer.Sound('FileGame/sound/sfx_wing.wav')
score_sound = pygame.mixer.Sound('FileGame/sound/sfx_point.wav')
die_sound = pygame.mixer.Sound('FileGame/sound/sfx_die.wav')
hit_sound = pygame.mixer.Sound('FileGame/sound/sfx_hit.wav')






