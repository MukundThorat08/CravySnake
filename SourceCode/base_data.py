from json_file_manager import get_json_data
from random import randrange
import graphics

SCREEN_WIDTH, SCREEN_HEIGHT = 645, 600
GRID_WIDTH, GRID_HEIGHT = 600, 500
CELL_SIZE = 25
score = 0
high_score = get_json_data('highScore')
GRID_X, GRID_Y = (SCREEN_WIDTH - graphics.grid_img.get_width()) // 2 + 3,\
    (SCREEN_HEIGHT - graphics.grid_img.get_height()) // 2
FPS = 10


def random_position_generator() -> list:
    random_x = randrange(GRID_X + CELL_SIZE, (GRID_X + GRID_WIDTH))
    random_y = randrange(GRID_Y + CELL_SIZE, (GRID_Y + GRID_HEIGHT))
    return [((random_x // CELL_SIZE) * CELL_SIZE) - CELL_SIZE, ((random_y // CELL_SIZE) * CELL_SIZE) - CELL_SIZE]


