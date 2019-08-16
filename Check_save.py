# Check if the Player has a save file and save it to a dictionary.

import os


def check_save(username):
    save_game_data = {}
    if os.path.exists('./' + username + "_save" + ".txt"):
        with open(username + "_save.txt") as f:
            for line in f:
                (key, val) = line.split()
                save_game_data[key] = val

        return save_game_data

    else:
        return False
