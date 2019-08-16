# RPG Game 1.0

import Registration
import Login
import Class_Choice
import Variables
import random
import Word_Minigame
import Check_save
import Add_Resources


# This Segment Focuses on Account registration / The first thing to pop up after booting up the game.
while True:
    Player_Login_Choice = input(Variables.menu_login_txt)
    if Player_Login_Choice == "1":
        Registration.registration()


# Login segment that checks if username exists and if the provided password matches with the one in file.
    if Player_Login_Choice == "2":
        Profile_data = Login.login()
        if Profile_data == 1:
            continue
        else:
            break


# Taking a note of the username so that we can address the player.
Username = Profile_data["Username:"]


# Check if the user has a save game file and load the file in a dictionary.
save_game = Check_save.check_save(Username)


# Main game loop that shows the game menu.
while True:
    Main_Menu_Choice = input(Variables.menu_main_txt)


# If the user chose New Game we first check if he has a save game file and ask for overwrite confirmation.
    if Main_Menu_Choice == "1":
        if save_game is not False:
            Choice = input(Variables.save_override_txt)
            if Choice == "1":
                chosen_class = Class_Choice.Class_choice(Username)
            else:
                continue


# Otherwise we go straight to character creation.
        else:
            chosen_class = Class_Choice.Class_choice(Username)


# If the player chose Continue we check for a save file and print a message if the save file is missing.
    elif Main_Menu_Choice == "2":
        if save_game is not False:
            print("\nLoading the game. Please Wait.")

        else:
            print("No save game file found. Please start a new adventure by choosing \"New Game\"")
            continue


# If the player chose Options we display the Options menu.
    elif Main_Menu_Choice == "3":
        print(Variables.options_txt)


# If player chose quit we ask for confirmation and exit out of the game or return to menu.
    elif Main_Menu_Choice == "4":
        Exit_confirmation = input(Variables.exit_confirmation_txt)
        if Exit_confirmation == "1":
            break
        else:
            print("Returning to main menu.")
    else:
        print("Input a valid choice.")


# After New game / Continue this is where the game starts.
    while True:
        menu_game_choice = input(Variables.menu_game_txt)


# When player chooses to enter the Mysterious tower select a random minigame from the list of minigames
        if menu_game_choice == "1":
            choose_difficulty = 1
            game_list = [Word_Minigame.word_minigame, ]
            random_chosen_game = game_list[(random.randint(0, len(game_list[1:])))]
            while True:
                try:
                    choose_difficulty = int(input(Variables.difficulty_txt))
                except ValueError:
                    print("\nPlease choose a number from the list.\n")
                    continue
                break

            game_parameters = [30, 0, 100, choose_difficulty]
            game_result = random_chosen_game(game_parameters[0], game_parameters[1],
                                             game_parameters[2], game_parameters[3])

            if game_result == "Success":
                resource_reward = Add_Resources.give_resources(choose_difficulty, Username, save_game)
                print("\nCongratulations on defeating the Tower floor! You received %d gold!\n"
                      % resource_reward)
            else:
                print("\nChoose a lower difficulty or try to get stronger before challenging that floor again.\n")

# Character
        elif menu_game_choice == "2":
            pass


# Inventory
        elif menu_game_choice == "3":
            pass


# Exiting the game back to Main Menu after confirmation.
        elif menu_game_choice == "4":
            Exit_confirmation = input(Variables.exit_confirmation_txt)
            if Exit_confirmation == "1":
                print("\nGoing back to Main Menu.\n")
                break
            else:
                pass
        else:
            continue


# TO DO:
# Implement the first level of the mysterious tower and use the word_minigame, generate gold as reward.
