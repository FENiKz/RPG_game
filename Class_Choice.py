# Module where the Player chooses a class from the Classes lis
# and the class choice gets appended to his Username.txt file.

# Beautification variable.
Field_Separator = "\n\n------------------------------------------------------------------------------------------\n\n"


def Class_choice(Username):
    while True:
        Classes = ['Warrior', 'Rogue', 'Mage', 'Bard', 'Paladin', 'Deprived']
        print(Field_Separator)
        for i in range(0, len(Classes)):
            print("[%d]" % (i + 1), Classes[i], end='    ')
        print("\n" + Field_Separator)
        while True:
            try:
                Player_Class_Choice = int(input("Choice: "))
                break
            except:
                print("Only numbers are acceptable")

        if Player_Class_Choice in range(1, len(Classes)):
            Profile_data = open(Username + "_save" + ".txt", "w")
            Profile_data.write("Class: " + Classes[(Player_Class_Choice - 1)])
            Profile_data.close()

            return Classes[Player_Class_Choice]
        else:
            print("Only numbers from 1 to %d" % len(Classes[1:]))
