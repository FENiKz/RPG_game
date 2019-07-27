# RPG Game 1.0

import os
import Registration
import Login
import Class_Choice
import Variables

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


# Main game loop that shows the game menu.
while True:
    Main_Menu_Choice = input(Variables.menu_main_txt)


# If the user chose New Game we first check if he has a save game file and ask for overwrite confirmation.
    if Main_Menu_Choice == "1":
        if os.path.exists('./' + Username + "_save" + ".txt"):
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
        if os.path.exists('./' + Username + "_save" + ".txt"):
            print("\nLoading the game. Please Wait.")
        else:
            print("No save game file found. Please start a new adventure by choosing \"New Game\"")
            continue


# If the player chose options we display the options menu.
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
            pass
        elif menu_game_choice == "2":
            pass
        elif menu_game_choice == "3":
            pass
        elif menu_game_choice == "4":
            Exit_confirmation = input(Variables.exit_confirmation_txt)
            if Exit_confirmation == "1":
                print("\nGoing back to Main Menu.\n")
                break
            else:
                pass
        else:
            continue

