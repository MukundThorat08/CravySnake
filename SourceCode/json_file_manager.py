from json import load, dump
from os.path import exists


def check_is_database_exists():
    if not exists('database.json'):
        essential_data = {"highScore": 0, "level": 1, "play_at_once": True}

        # create new file and fill essential data
        with open('database.json', 'w') as new_file:
            dump(essential_data, new_file)


def get_json_data(data: str):
    with open('database.json') as json_file:
        return load(json_file)[data]


def write_json_data(old_data, new_data):
    with open('database.json') as json_file:
        data = load(json_file)
        data[old_data] = new_data  # replacing desired data with new data

    with open('database.json', 'w') as write_file:
        dump(data, write_file)
