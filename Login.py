# This module checks if an account with the provided username exists and checks if the provided password is correct

import os
from Variables import Field_Separator


def login():
    Username = input(Field_Separator + "Username: ")

    Profile_data = {}

    if os.path.exists('./' + Username + '.txt'):
        with open(Username + ".txt") as f:
            for line in f:
                (key, val) = line.split()
                Profile_data[key] = val

            Login_Attempts = 3
            while Login_Attempts > 0:
                password = input("Password: ")
                if password == Profile_data["Password:"]:
                    return Profile_data
                else:
                    Login_Attempts -= 1
                    print("Wrong Password\nYou have %d Chances left" % Login_Attempts)
        return 1
    else:
        print("Username does not exist")
        return 1
