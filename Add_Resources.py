# # Module that provides resources to the player if he defeated the Mysterious tower floor

import Check_save


def give_resources(difficulty, username, save_content):
    # Calculate the reward based on difficulty
    resource_reward = 100 * (difficulty ** 2)

    # Load current gold from the save file, increase the value and save it to the save_game file
    save_content["Gold:"]


    profile_data = open(username + "_save" + ".txt", "w")
    profile_data.write("Gold: ")
    profile_data.close()

    return resource_reward
