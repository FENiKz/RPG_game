# RPG Game 1.0

import os
import Registration
import Login
import Class_Choice
import Variables
import random
import Word_Minigame


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


# Check if the user has a save game file.
save_game = ""
if os.path.exists('./' + Username + "_save" + ".txt"):
    save_game = True
else:
    save_game = False


# Main game loop that shows the game menu.
while True:
    Main_Menu_Choice = input(Variables.menu_main_txt)


# If the user chose New Game we first check if he has a save game file and ask for overwrite confirmation.
    if Main_Menu_Choice == "1":
        if save_game:
            Choice = input(Variables.save_override_txt)
            if Choice == "1":
                chosen_class = Class_Choice.Class_choice(Username)
            else:
                pass


# Otherwise we go straight to character creation.
        else:
            chosen_class = Class_Choice.Class_choice(Username)


# If the player chose Continue we check for a save file and print a message if the save file is missing.
    elif Main_Menu_Choice == "2":
        if save_game:
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
            game_list = [Word_Minigame.word_minigame, ]
            random_chosen_game = game_list[(random.randint(0, len(game_list[1:])))]
            game_result = random_chosen_game(30, 0, 100, 1)
            if game_result == "Success":
                print("Congratulations on defeating the Tower floor! You received %d gold!" % (100))


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
