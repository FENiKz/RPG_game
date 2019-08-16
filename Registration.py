# Module used for creating a file on the local filesystem with the provided username and password as content

import os


def registration():
    username = input("username: ")
    if os.path.exists('./' + username + '.txt'):
        print("username already Exists")
    else:
        while True:
            player_password = input("Password: ")
            player_pwd_confirmation = input("Re-enter password: ")
            if player_pwd_confirmation == player_password:
                break
            else:
                print("The passwords do not match")

# Creating and saving username + password to the file username.txt
        profile_data = open(username + ".txt", "w")
        profile_data.write("username: " + username + "\npassword: " + Player_password)
        profile_data.close()

        print("Registration successful!")