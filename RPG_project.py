# RPG Game 1.0

import os
import Registration
import Login
import Class_Choice

# Variable used for beautification of the displayed text.
Field_Separator = "\n\n------------------------------------------------------------------------------------------\n\n"

# This Segment Focuses on Account registration / The first thing to pop up after booting up the game.
while True:
    Player_Login_Choice = int(input(Field_Separator +
                                    "[1] Register     [2] Login     [3] Exit" + Field_Separator + "Choice: "))
    if Player_Login_Choice == 1:
        Registration.registration()


# Login segment that checks if username exists and if the provided password matches with the one in file.
    if Player_Login_Choice == 2:
        Profile_data = Login.login()
        if Profile_data == 1:
            continue
        else:
            break

# Taking a note of the username so that we can address the player.
Username = Profile_data["Username:"]


# Main game loop that shows the game menu.
while True:
    print("\nWelcome back " + Username + Field_Separator +
          "[1] New Game\n[2] Continue\n[3] Options\n[4] Quit" + Field_Separator)


# Taking a note of users menu choice.
    Main_Menu_Choice = input("Choice: ")


# If the user chose New Game we first check if he has a save game file and ask for overwrite confirmation.
    if Main_Menu_Choice == "1":
        if os.path.exists('./' + Username + "_save" + ".txt"):
            print("This will override your current save game."
                  "Are you sure you want to continue?\n\n[1] Yes   [2] No")
            Choice = input("\nChoice: ")
            if Choice == "1":
                chosen_class = Class_Choice.Class_choice(Username)
            else:
                continue


# Otherwise we go straight to character creation.
        else:
            chosen_class = Class_Choice.Class_choice(Username)
        continue


# If the player chose Continue we check for a save file and print a message if the save file is missing.
    elif Main_Menu_Choice == "2":
        if os.path.exists('./' + Username + "_save" + ".txt"):
            print("\nLoading the game. Please Wait.")
            continue
        else:
            print("No save game file found. Please start a new adventure by choosing \"New Game\"")
            continue


# If the player chose options we display the options menu.
    elif Main_Menu_Choice == "3":
        print(Field_Separator + "OPTIONS\n\n[1] Resolution:\n[2] Text Size:\n[3] Text Speed:")


# If player chose quit we ask for confirmation and exit out of the game or return to menu.
    elif Main_Menu_Choice == "4":
        Exit_confirmation = input("Are you sure you want to quit? \
                                  \n\n[1] Yes     [2] No" + Field_Separator + "Choice: ")

        if Exit_confirmation == "1":
            break
        else:
            print("Returning to main menu.")
    else:
        print("Input a valid choice.")
