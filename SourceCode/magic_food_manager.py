from time import strftime
import base_data


# Magic Food Variables
magic_food_pos = base_data.random_position_generator()
display_magic_food = False
time_counter = 0

# variables required for magic_food_stimulator
run_at_once = False
pre_score = 0


def magic_food_stimulator():
    global display_magic_food, run_at_once, pre_score, magic_food_pos
    if base_data.score % 6 == 0 and base_data.score != 0 and display_magic_food is False:

        if run_at_once is not True and pre_score != base_data.score:
            magic_food_pos = base_data.random_position_generator()
            pre_score = base_data.score
            run_at_once = True
            display_magic_food = True


def remove_magic_food():
    global time_counter, display_magic_food, run_at_once
    display_magic_food = False
    run_at_once = False
    time_counter = 0


def magic_food_collision(snake, magic_food):
    if snake.colliderect(magic_food):
        from os.path import join
        from pygame import mixer, mixer_music
        mixer_music.load(join('Assets/sound', 'magic_food_sound.mp3'))
        mixer.music.play(0)  # play at once
        magic_score_adder()
        remove_magic_food()


def magic_score_adder():
    match time_counter:
        case 0:
            base_data.score += 15
        case 1:
            base_data.score += 12
        case 2:
            base_data.score += 10
        case 3:
            base_data.score += 7
        case 4:
            base_data.score += 5
        case 5:
            base_data.score += 3


# variables required for start_timer function
time_stamp = None
call_at_once = True


def start_timer():
    global time_counter, display_magic_food, time_stamp, call_at_once
    if call_at_once is True:  # initialize time stamp once
        time_stamp = strftime("%S")
        call_at_once = False

    if int(strftime("%S")) != int(time_stamp) and time_counter != 5:
        time_counter += 1
        time_stamp = strftime('%S')
    elif time_counter >= 5:
        remove_magic_food()


def spawn_magic_food_and_timer(screen, snake):
    from graphics import load_text, pilot_font
    from pygame import draw
    from Color import BLUE, GREENISH_BLACK

    start_timer()
    magic_food = draw.rect(screen, BLUE, (magic_food_pos[0], magic_food_pos[1], base_data.CELL_SIZE,
                                          base_data.CELL_SIZE))
    load_text(screen, pilot_font, str(time_counter), GREENISH_BLACK, (50, 50))
    magic_food_collision(snake, magic_food)
