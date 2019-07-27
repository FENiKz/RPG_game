# Module used for creating a file on the local filesystem with the provided Username and Password as content

import os

# Beautification variable
Field_Separator = "\n\n------------------------------------------------------------------------------------------\n\n"


def registration():
    Username = input("Username: ")
    if os.path.exists('./' + Username + '.txt'):
        print("Username already Exists")
    else:
        while True:
            Player_Password = input("Password: ")
            Player_Pwd_Confirmation = input("Re-enter Password: ")
            if Player_Pwd_Confirmation == Player_Password:
                break
            else:
                print("The Passwords do not match")

# Creating and saving username + password to the file Username.txt
        profile_data = open(Username + ".txt", "w")
        profile_data.write("Username: " + Username + "\nPassword: " + Player_Password)
        profile_data.close()

        print("Registration successful!")