import pygame

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STILE = "freesansbold.ttf"
black_color = (0,0,0)
white_color = (255, 255, 255)


def get_score_element(points):
    font = pygame.font.Font(FONT_STILE, 20)

    text = font.render('Points: ' + str(points), True, white_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 40)
    return text, text_rect 

def get_centered_message(message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STILE, 30)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect

