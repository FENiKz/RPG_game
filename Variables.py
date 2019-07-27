# Separate file for variables to increase readability of the main project file.


# Variable used for beautification of the displayed text.
Field_Separator = "\n\n------------------------------------------------------------------------------------------\n\n"

# Menu display variables.
menu_login_txt = Field_Separator + "[1] Register     [2] Login     [3] Exit" + Field_Separator + "Choice: "

menu_main_txt = (Field_Separator + "[1] New Game     [2] Continue     [3] Options     [4] Quit"
                 + Field_Separator + "Choice: ")

menu_game_txt = (Field_Separator + "[1] Enter the Mysterious Tower     [2] Character     [3] Inventory     "
                                   "[4] Main Menu" + Field_Separator + "Choice: ")

# Other display variables.
save_override_txt = (Field_Separator + "This will override your current save game."
                     "Are you sure you want to continue?\n\n[1] Yes   [2] No" + Field_Separator + "Choice: ")

options_txt = Field_Separator + "OPTIONS\n\n[1] Resolution:\n[2] Text Size:\n[3] Text Speed:"

exit_confirmation_txt = ("Are you sure you want to quit?"
                         "\n\n[1] Yes     [2] No" + Field_Separator + "Choice: ")
