# Check if the Player has a save file and save it to a dictionary.

import os


def check_save(Username):
    save_game_data = {}
    if os.path.exists('./' + Username + "_save" + ".txt"):
        with open(Username + "_save.txt") as f:
            for line in f:
                (key, val) = line.split()
                save_game_data[key] = val

        return save_game_data

    else:
        return False
