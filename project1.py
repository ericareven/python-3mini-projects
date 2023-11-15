# PIG

import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# TEST
# value = roll()
# print(value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit(): # check if input is a number
        players = int(players) # convert string into integer
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")


