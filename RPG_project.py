#RPG Game 1.0

import Registration
import Login
import time

#This Segment Focuses on Character Creation / The first thing to pop up after booting up the game.

Field_Separator = "\n\n------------------------------------------------------------------------------------------\n\n"

while True:
    Player_Login_Choice = int(input(Field_Separator + "[1] Register     [2] Login     [3] Exit" + Field_Separator + "Choice: "))


    if Player_Login_Choice == 1:
        Registration.registration()


#Post Character Creation section where a player gets to start his or her adventure.


    if Player_Login_Choice == 2:
        Profile_data = Login.login()
        if Profile_data == 1:
            continue
        else:
            break

Player_Name = Profile_data["Name:"]

print("Welcome " + Player_Name + " To <Insert Title Here>" + Field_Separator + "[1] New Game\n[2] Contiunue\n[3] Options\n[4] Exit" + Field_Separator + "Choice: ")

while True:
    Main_Menu_Choice = input()
    if Main_Menu_Choice == "1":
        print("Under Construction")

    elif Main_Menu_Choice == "2":
        print("Under Construction")

    elif Main_Menu_Choice == "3":
        print(Field_Separator + "OPTIONS\n\n[1] Resolution:\n[2] Text Size:\n[3] Text Speed:")

    elif Main_Menu_Choice == "4":
        Exit_confirmation = input("Are you sure you want to quit?\n\n[1] Yes     [2] No" + Field_Separator + "Choice: ")

        if Exit_confirmation == "1":
            break

        if Exit_confirmation == "2":
            print("Returning to start menu...")
            time.sleep(0.5)
        else:
            print("Ill take that as a no")
    else:
        print("Input a valid choice...")