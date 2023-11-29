import pygame
import os
import alignment

pygame.init()
# images
grid_img = pygame.image.load(os.path.join('Assets/Images', 'grid.png'))
pause_img = pygame.image.load(os.path.join('Assets/Images', 'pause.png'))
paused_img = pygame.image.load(os.path.join('Assets/Images', 'paused.png'))
exit_img = pygame.image.load(os.path.join('Assets/Images', 'exit.png'))
bg_img = pygame.image.load(os.path.join('Assets/Images', 'background.png'))
home_button_img = pygame.image.load(os.path.join('Assets/Images', 'home.png'))
start_button_img = pygame.image.load(os.path.join('Assets/Images', 'play.png'))
score_bg = pygame.image.load(os.path.join('Assets/Images', 'score_display_bg.png'))
setting_bg_img = pygame.image.load(os.path.join('Assets/Images', 'setting_bg.png'))
reset_img = pygame.image.load(os.path.join('Assets/Images', 'reset.png'))
rank_button_img = pygame.image.load(os.path.join('Assets/Images', 'level.png'))
close_button = pygame.image.load(os.path.join('Assets/Images', 'close.png'))

# change it quick
snake_raw_img = pygame.image.load(os.path.join('Assets/Images', 'snake.png'))
snake_img = pygame.transform.scale(snake_raw_img, (238, 238))

# fonts
laser_font = pygame.font.Font(os.path.join('Assets/Fonts', 'PilotCommandLaser.otf'), 30)
laser_font_60 = pygame.font.Font(os.path.join('Assets/Fonts', 'PilotCommandLaser.otf'), 60)
pilot_font = pygame.font.Font(os.path.join('Assets/Fonts', 'PilotCommand.otf'), 25)
pilot_halftone_font = pygame.font.Font(os.path.join('Assets/Fonts', 'PilotCommandHalftone.otf'), 65)

instance = alignment.CreateWindow()
snake_img.get_rect()


def load_image(window, image, co_ordinates: tuple = (False, False), extra: tuple = (0, 0)):
    if co_ordinates[0] is True and co_ordinates[1] is not True:
        x = instance.align_to_center_horizontally(image)
        y = co_ordinates[1]
        return window.blit(image, (x + extra[0], y + extra[1]))

    elif co_ordinates[1] is True and co_ordinates[0] is not True:
        x = co_ordinates[0]
        y = instance.align_to_center_vertically(image)
        return window.blit(image, (x + extra[0], y + extra[1]))

    elif co_ordinates[0] is True and co_ordinates[1] is True:
        x = instance.align_to_center_horizontally(image)
        y = instance.align_to_center_vertically(image)
        return window.blit(image, (x + extra[0], y + extra[1]))

    else:
        x = co_ordinates[0]
        y = co_ordinates[1]
        return window.blit(image, (x + extra[0], y + extra[1]))


def load_text(window, font, text, color, co_ordinates: tuple = (False, False), extra: tuple = (0, 0)):
    raw_font = font.render(text, True, color)

    if co_ordinates[0] is True and co_ordinates[1] is not False:
        x = instance.align_to_center_horizontally(raw_font, True)
        y = co_ordinates[1]
        return window.blit(raw_font, (x + extra[0], y))

    elif co_ordinates[1] is True and co_ordinates[0] is not False:
        x = co_ordinates[0]
        y = instance.align_to_center_vertically(raw_font, True)
        return window.blit(raw_font, (x + extra[0], y + extra[1]))

    elif co_ordinates[0] is True and co_ordinates[1] is True:
        x = instance.align_to_center(raw_font, True)[0]
        y = instance.align_to_center(raw_font, True)[1]
        return window.blit(raw_font, (x + extra[0], y + extra[1]))
    else:
        x = co_ordinates[0]
        y = co_ordinates[1]
        return window.blit(raw_font, (x + extra[0], y + extra[1]))


def get_rect_object(graphic):
    return pygame.Rect(graphic.x, graphic.y, graphic.width, graphic.height)
