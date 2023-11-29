import pygame
from sys import exit
from base_data import FPS

# local modules
import Defination
from json_file_manager import check_is_database_exists


def game_loop():  # Sequence of execution of functions matters!
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                Defination.snake_mover(event)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                Defination.mouse_event_controller(event)

        Defination.high_score_updater()
        Defination.draw_graphics()
        Defination.snake_transportation()
        Defination.snake_velocity_manager()
        Defination.create_snake_segment()
        snake, food = Defination.snake_and_food_drawer()

        if not Defination.paused:
            new_head = [Defination.snake_pos[0][0], Defination.snake_pos[0][1]]
            Defination.snake_pos.insert(0, new_head)

        Defination.snake_collision_detector(snake, food)
        check_is_database_exists()
        pygame.display.update()
        clock.tick(FPS)
