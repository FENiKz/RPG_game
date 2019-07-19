import os

Field_Separator = "\n\n------------------------------------------------------------------------------------------\n\n"

def login():
    username = input(Field_Separator + "Username: ")
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
                    return Profile_data
                else:
                    Login_Attempts -= 1
                    print("Wrong Password\nYou have %d Chances left" % Login_Attempts)
        return 1
    else:
        print("Username does not exist")
        return 1

