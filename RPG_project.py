#RPG Game 1.0

import os

#This Segment Focuses on Character Creation / The first thing to pop up after booting up the game.

Field_Separator = "\n\n------------------------------------------------------------------------------------------\n\n"

while True:
    Player_Login_Choice = int(input(Field_Separator + "[1] Register     [2] Login     [3] Exit" + Field_Separator + "Choice: "))


    if Player_Login_Choice == 1:
        Player_Name = input("Username: ")
        if os.path.exists('./' + Player_Name + '.txt'):
            print("Username already Exists")
        else:
            while True:
                Player_Password = input("Password: ")
                Player_Pwd_Confirmation = input("Re-enter Password: ")
                if Player_Pwd_Confirmation == Player_Password:
                    break
                else:
                    print("The Passwords do not match")


            while True:
                Classes = ['Y0lo', 'Warrior', 'Rogue', 'Mage', 'Bard', 'Paladin', 'Deprived']
                print(Field_Separator)
                for i in range(1, len(Classes)):
                    print("[%d]" % i, Classes[i], end='     ')
                print("\n" + Field_Separator)
                while True:
                    try:
                        Player_Class_Choice = int(input("Choice: "))
                        if Player_Class_Choice in range(1, len(Classes)):
                            break
                        else:
                            print("Only numbers from 1 to %d" % len(Classes[1:]))
                    except:
                        print("Only numbers are acceptable")
                Player_Class = Classes[Player_Class_Choice]
                break


            Player_Character_Creation_Confirmation = int(input(Field_Separator + "Name: " + Player_Name + "\nClass: " + Player_Class + Field_Separator + "\n\nWould you like to finalize Character Creation?" + Field_Separator + "[1] Yes     [2] Take me back to the Login Page" + Field_Separator + "Choice: "))


            if (Player_Character_Creation_Confirmation == 1):
                Profile_data = open(Player_Name + ".txt", "w")
                Profile_data.write("Name: " + Player_Name + "\nPassword: " + Player_Password + "\nClass: " + Player_Class)
                Profile_data.close()
            else:
                print("Returning to Login Screen...")


#Post Character Creation section where a player gets to start his or her adventure.


    if Player_Login_Choice == 2:
        username = input(Field_Separator + "Name: ")
        Profile_data = {}
        if os.path.exists('./' + username + '.txt'):
            with open(username + ".txt") as f:
                for line in f:
                    (key, val) = line.split()
                    Profile_data[(key)] = val
                Login_Attempts = 3
                while Login_Attempts > 0:
                    password = input("Password: ")
                    print(Field_Separator)
                    if password == Profile_data["Password:"]:
                        break
                    else:
                        Login_Attempts -= 1
                        print("Wrong Password\n You have %d choices left" % Login_Attempts)
                break
        else:
            print("This Username does not exist")

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
