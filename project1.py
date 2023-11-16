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

max_score = 50
player_scores = [0 for _ in range(players)] # loop number of players

while max(player_scores) < max_score:

    for player_id in range(players):
        print("\nPlayer number", player_id +1, "turn has just started!")
        print("Your total score is:", player_scores[player_id], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y": # convert input to lower case and check if it = y
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is over")
                current_score = 0
                break # end turn
            else: 
                current_score += value
                print("You rolled a: ", value)

            print("Your score is: ", current_score)
        
        player_scores[player_id] += current_score
        print("Your total score is: ", player_scores[player_id])
    
max_score = max(player_scores)
winning_id = player_scores.index(max_score)
print(f"Player number {winning_id + 1} is the winner with a score of: {max_score}") # +1 bc id starts at 0, and we want to display players 1-4, not 0-3