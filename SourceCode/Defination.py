import pygame
import Color
import graphics
import json_file_manager
import magic_food_manager
from base_data import GRID_WIDTH, GRID_HEIGHT, CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, GRID_X, GRID_Y
import base_data

pygame.init()

initial_snake_pos = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
snake_pos = [initial_snake_pos]

snake_velocity = [CELL_SIZE, 0]
paused = False

# Common Config
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

food_pos = base_data.random_position_generator()
pause_game_img = graphics.pause_img


def draw_graphics():
    SCREEN.fill(Color.BG_GREEN)

    graphics.load_image(SCREEN, graphics.grid_img, (True, True), (3, 0))
    graphics.load_image(SCREEN, pause_game_img, (25, 556))
    graphics.load_image(SCREEN, graphics.exit_img, (580, 556))
    graphics.load_text(SCREEN, graphics.laser_font, f"SCORE : {base_data.score}", Color.SCORE_COLOR, (GRID_X, 10))
    graphics.load_text(SCREEN, graphics.laser_font, f"HIGH SCORE: {base_data.high_score}", Color.SCORE_COLOR,
                       ((GRID_X + GRID_WIDTH) - graphics.laser_font.size(f"HIGH SCORE: {base_data.high_score}")[0], 10))


def snake_and_food_drawer():
    snake = pygame.draw.rect(SCREEN, Color.DARK_GRAY,
                             (snake_pos[0][0], snake_pos[0][1],
                              CELL_SIZE, CELL_SIZE))
    food = pygame.draw.rect(SCREEN, Color.RED, (food_pos[0], food_pos[1],
                                                CELL_SIZE, CELL_SIZE))
    if magic_food_manager.display_magic_food is True:
        magic_food_manager.spawn_magic_food_and_timer(SCREEN, snake)

    snake_death()
    return snake, food


def snake_velocity_manager():
    snake_pos[0][0] += snake_velocity[0]
    snake_pos[0][1] += snake_velocity[1]


def snake_mover(event):
    global snake_velocity
    if event.key == pygame.K_SPACE:
        pause_game()
    elif event.key == pygame.K_ESCAPE:
        from Home import home_loop
        home_loop()
    if not paused:
        
        if event.key == pygame.K_LEFT and snake_velocity != [CELL_SIZE, 0]:
            snake_velocity = [-CELL_SIZE, 0]
            print("left")
        elif event.key == pygame.K_RIGHT and snake_velocity != [-CELL_SIZE, 0]:
            snake_velocity = [CELL_SIZE, 0]
            print("right")
        elif event.key == pygame.K_UP and snake_velocity != [0, CELL_SIZE]:
            snake_velocity = [0, -CELL_SIZE]
            print("up")
        elif event.key == pygame.K_DOWN and snake_velocity != [0, -CELL_SIZE]:
            snake_velocity = [0, CELL_SIZE]
            print("down")


def create_snake_segment():
    for pos in snake_pos:
        pygame.draw.rect(SCREEN, Color.YELLOW, (pos[0], pos[1], CELL_SIZE, CELL_SIZE))


def high_score_updater():
    if base_data.score >= base_data.high_score:
        json_file_manager.write_json_data('highScore', base_data.score)
        base_data.high_score = base_data.score


def snake_transportation():
    if snake_pos[0][0] <= GRID_X and snake_velocity == [-CELL_SIZE, 0]:
        snake_pos[0][0] = GRID_WIDTH + GRID_X

    elif snake_pos[0][0] >= (GRID_WIDTH + GRID_X) - CELL_SIZE and snake_velocity == [CELL_SIZE, 0]:
        snake_pos[0][0] = GRID_X - CELL_SIZE

    elif snake_pos[0][1] <= GRID_Y and snake_velocity == [0, -CELL_SIZE]:
        snake_pos[0][1] = GRID_HEIGHT + GRID_Y

    elif snake_pos[0][1] >= (GRID_HEIGHT + GRID_Y) - CELL_SIZE and snake_velocity == [0, CELL_SIZE]:
        snake_pos[0][1] = GRID_Y - CELL_SIZE


def snake_death():
    if snake_pos[0] in snake_pos[2:] and not paused:
        from os.path import join
        pygame.mixer_music.load(join('Assets/sound', 'gameOver.wav'))
        pygame.mixer.music.play(0)  # play at once
        from Game_over_screen import game_over_loop
        game_over_loop(base_data.score, base_data.high_score)


def snake_collision_detector(snake, food):
    global food_pos
    if snake.colliderect(food):
        from os.path import join
        pygame.mixer_music.load(join('Assets/sound', 'eat.wav'))
        pygame.mixer.music.play(0)  # play at once
        food_pos = base_data.random_position_generator()
        base_data.score += 1
    else:
        if not paused:
            snake_pos.pop()

    magic_food_manager.magic_food_stimulator()


def reset_game():
    global snake_pos, food_pos, snake_velocity
    base_data.score = 0
    snake_velocity = [CELL_SIZE, 0]
    snake_pos = [[GRID_WIDTH // 2, GRID_HEIGHT // 2]]
    food_pos = base_data.random_position_generator()


temp_snake_velocity = 0


def pause_game():
    global snake_velocity, paused, temp_snake_velocity, pause_game_img
    if not paused:
        pause_game_img = graphics.paused_img
        paused = True
        temp_snake_velocity = snake_velocity
        snake_velocity = [0, 0]
    else:
        pause_game_img = graphics.pause_img
        paused = False
        snake_velocity = temp_snake_velocity


def mouse_event_controller(event):
    if graphics.get_rect_object(graphics.load_image(SCREEN, graphics.pause_img, (25, 556))).collidepoint(event.pos):
        pause_game()
    elif graphics.get_rect_object(graphics.load_image(SCREEN, graphics.exit_img, (580, 556))).collidepoint(event.pos):
        from Home import home_loop
        home_loop()
