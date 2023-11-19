import sys
import pygame
import Color
import Defination
import graphics
from common import CreateWindow
import json_file_manager

pygame.init()
instance = CreateWindow()
instance.create("Home")


def level_manager(lvl):
    global easy_color, medium_color, hard_color
    easy_color = Color.GRAY
    medium_color = Color.GRAY
    hard_color = Color.GRAY
    level_value_setter(lvl)


def level_value_setter(lvl):
    global easy_color, medium_color, hard_color
    match lvl:
        case 0:
            easy_color = Color.BG_GREEN
            Defination.FPS = 7
        case 1:
            medium_color = Color.TEXT_ORANGE
            Defination.FPS = 10
        case 2:
            hard_color = Color.RED
            Defination.FPS = 20


# GAME VARIABLES
run = True
level = json_file_manager.get_json_data('level')
easy_color = Color.GRAY
medium_color = Color.TEXT_ORANGE
hard_color = Color.GRAY

level_manager(level)


def draw_graphics():
    graphics.load_image(instance.SCREEN, graphics.snake_img, (True, 5))
    graphics.load_text(instance.SCREEN, graphics.pilot_halftone_font, "SNAKE", Color.WHITE, (True, 230))
    graphics.load_image(instance.SCREEN, graphics.start_button_img, (True, 330))
    graphics.load_image(instance.SCREEN, graphics.rank_button_img, (True, 450))


def show_score_popup():
    json_file_manager.check_is_database_exists()
    graphics.load_image(instance.SCREEN, graphics.setting_bg_img,
                        ((instance.SCREEN_WIDTH - graphics.setting_bg_img.get_width())//2,
                         (instance.SCREEN_HEIGHT - graphics.setting_bg_img.get_height())//2,))
    graphics.load_text(instance.SCREEN, graphics.pilot_font, "EASY", easy_color, (True, 220))
    graphics.load_text(instance.SCREEN, graphics.pilot_font, "MEDIUM", medium_color, (True, 255))
    graphics.load_text(instance.SCREEN, graphics.pilot_font, "HARD", hard_color, (True, 285))
    graphics.load_text(instance.SCREEN, graphics.pilot_font, "HIGH SCORE", Color.WHITE, (True, 360), (-40, 0))
    graphics.load_text(instance.SCREEN, graphics.pilot_font, f": {Defination.high_score}",
                       Color.DARK_RED, (True, 360), (100, 0))
    graphics.load_image(instance.SCREEN, graphics.reset_img, (True, 400))
    graphics.load_image(instance.SCREEN, graphics.close_button, (True, 93))


def radio_click_events(radio1, radio2, radio3):
    global run, easy_color, medium_color, hard_color
    key_press = pygame.mouse.get_pos()

    if radio1.collidepoint(key_press) and run is not True:
        level_manager(0)

    elif radio2.collidepoint(key_press) and run is not True:
        level_manager(1)

    elif radio3.collidepoint(key_press) and run is not True:
        level_manager(2)


def mouse_event_handler(event):
    global run
    if graphics.get_rect_object(graphics.load_image(instance.SCREEN, graphics.start_button_img,
                                                    (True, 330))).collidepoint(event.pos) and run:
        Defination.reset_game()
        from GamePlay import game_loop
        game_loop()
    elif graphics.get_rect_object(graphics.load_image(instance.SCREEN, graphics.reset_img,
                                                      (True, 400))).collidepoint(event.pos) and not run:
        json_file_manager.write_json_data('highScore', 0)
        Defination.high_score = 0
    elif graphics.get_rect_object(graphics.load_image(instance.SCREEN,
                                                      graphics.rank_button_img,
                                                      (True, 450))).collidepoint(event.pos):
        run = False
    elif graphics.get_rect_object(graphics.load_image(instance.SCREEN,
                                                      graphics.close_button,
                                                      (True, 93))).collidepoint(event.pos) and not run:
        run = True


def home_loop():
    global run
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_event_handler(event)

        graphics.load_image(instance.SCREEN, graphics.bg_img, (True, True))
        if run:
            draw_graphics()
        else:
            show_score_popup()
            radio1 = pygame.draw.circle(instance.SCREEN, easy_color, ((instance.SCREEN_WIDTH - 210) // 2, 235), 10)
            radio2 = pygame.draw.circle(instance.SCREEN, medium_color, ((instance.SCREEN_WIDTH - 210) // 2, 270), 10)
            radio3 = pygame.draw.circle(instance.SCREEN, hard_color, ((instance.SCREEN_WIDTH - 210) // 2, 305), 10)
            radio_click_events(radio1, radio2, radio3)
        clock.tick(10)
        pygame.display.update()


if __name__ == '__main__':
    home_loop()
    pygame.quit()
