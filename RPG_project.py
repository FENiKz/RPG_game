#RPG Game 1.0

import os
import Registration
import Login

#This Segment Focuses on Character Creation / The first thing to pop up after booting up the game.

Field_Separator = "\n\n------------------------------------------------------------------------------------------\n\n"

while True:
    Player_Login_Choice = int(input(Field_Separator + "[1] Register     [2] Login     [3] Exit" + Field_Separator + "Choice: "))


    if Player_Login_Choice == 1:
        Registration.registration()


#Post Character Creation section where a player gets to start his or her adventure.


    if Player_Login_Choice == 2:
        Profile_data = Login.login()
        break

Player_Name = Profile_data["Name:"]
Player_Class = Profile_data["Class:"]
print("Welcome " + Player_Class + " " + Player_Name + " To <Insert Title Here>" + Field_Separator + "[0] Start Game\n[1] Options\n[2] Exit" + Field_Separator)
while True:
    Main_Menu_Choice = int(input())
    if Main_Menu_Choice == 0:
        print("Under Construction")
    elif Main_Menu_Choice == 1:
        print("Under Construction")
    elif Main_Menu_Choice == 2:
        break
