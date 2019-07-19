import os

Field_Separator = "\n\n------------------------------------------------------------------------------------------\n\n"

def registration():
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