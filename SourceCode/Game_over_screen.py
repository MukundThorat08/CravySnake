import sys
import pygame
import Defination
import graphics
import Color

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 645, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Over!")


def draw_graphics(score, high_score):
    graphics.load_image(SCREEN, graphics.bg_img, (True, True))
    graphics.load_image(SCREEN, graphics.score_bg, (True, 120))
    graphics.load_text(SCREEN, graphics.laser_font_60, "GAME OVER!", Color.RED, (True, 30))
    graphics.load_text(SCREEN, graphics.laser_font, f"SCORE : {score}", Color.SCORE_COLOR, (True, 150))
    graphics.load_text(SCREEN, graphics.laser_font, f"HIGH SCORE: {high_score}", Color.SCORE_COLOR, (True, 210))
    graphics.load_image(SCREEN, graphics.start_button_img, (True, 320))
    graphics.load_image(SCREEN, graphics.home_button_img, (True, 450))


def play_again_game(event):
    play_btn_rect = graphics.start_button_img.get_rect()
    play_btn_rect.x = (SCREEN_WIDTH - graphics.start_button_img.get_width()) // 2
    play_btn_rect.y = 320
    if play_btn_rect.collidepoint(event.pos):
        Defination.reset_game()
        from GamePlay import game_loop
        game_loop()


def visit_home(event):
    home_button_rect = graphics.home_button_img.get_rect()
    home_button_rect.x = (SCREEN_WIDTH - graphics.home_button_img.get_width()) // 2
    home_button_rect.y = 450
    if home_button_rect.collidepoint(event.pos):
        from Home import home_loop
        home_loop()


def game_over_loop(score, high_score):
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                play_again_game(event)
                visit_home(event)

        draw_graphics(score, high_score)
        clock.tick(10)
        pygame.display.update()
