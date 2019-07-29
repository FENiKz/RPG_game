# # Module that provides resources to the player if he defeated the Mysterious tower floor
#
#
# def give_resources():
#     pass

import Word_Minigame
import Variables
import random

game_list = [Word_Minigame.word_minigame, ]

random_chosen_game = game_list[(random.randint(0, len(game_list[1:])))]

choose_difficulty = int(input(Variables.difficulty_txt))

game_parameters = [30, 0, 100, choose_difficulty]

Word_Minigame.word_minigame(game_parameters[0], game_parameters[1], game_parameters[2], game_parameters[3])
