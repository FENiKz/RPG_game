"""
Minigame where you are presented with a list of random words. Your goal is to type and submit one word from the list
and then you will be presented with a new list. You are limited by time and your damage is based on the amount of
words you managed to type before the time ran out and the number of characters a word has. The more characters a
word has the more damage you will deal with that word. Be careful not to spend too much time typing long words.
Sometimes it is better to just type easier/shorter words.
"""

import random
import time

word_list = ['apple', 'car', 'class', 'school', 'bird', 'fish',
             'library', 'justice', 'success', 'goal', 'plan', 'wish']


def word_minigame(t_duration, dmg_boost, p_hp, m_level):
    t_end = time.time() + t_duration
    m_hp = 100 * m_level
    m_dmg = 20 * m_level
    while True:
        random_word_gen = random.randint(0, len(word_list[1:]))
        chosen_word = word_list[random_word_gen]
        print("\n" + chosen_word)
        user_word = input("\nAnswer: ")
        t_remaining = t_end - time.time()
        dmg_done = dmg_boost
        if t_remaining > 0:
            if user_word == chosen_word:
                if len(user_word) < 6:
                    dmg_done += 5
                elif len(user_word) >= 6 < 9:
                    dmg_done += 10
                else:
                    dmg_done += 15

                m_hp -= dmg_done
                if m_hp > 0:
                    print("\n%d Damage dealt! \
                           Monster is left with %d HP / %d seconds left!" % (dmg_done, m_hp, t_remaining))
                else:
                    print("\n%d Damage dealt! Congratulations! you have slain the monster!" % dmg_done)
                    return "Success"

            else:
                if t_remaining > 0:
                    print("\nYou Missed! %d seconds left!" % t_remaining)
                else:
                    print("\nYou Missed!\r")

        else:
            print("\nTimes up. Your last attack didn't count since you submitted after the time limit.")
            p_hp -= m_dmg
            if p_hp > 0:
                time.sleep(2)
                print("\nMonster dealt %d DMG to you!" % m_dmg)
                time.sleep(2)
                print("\nIt's your turn again! Type fast!")
                time.sleep(2)
                t_end = time.time() + t_duration
                continue
            else:
                print("\nMonster dealt %d DMG to you. You are gravely wounded and barely escaped from \
                                       the monster and retreated back to your camp." % m_dmg)
                return "Fail"
