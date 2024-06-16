import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input("enter the numbers of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= plaers <= 4
        print("must be between 2 and 4 players.")
        break 
    else:
    print("invalid try again")

print(players)

max_scores = 30
player_scores = [0 for _ in range(players)]

while max(players_scores) < max_scores:
    for pplater_idx in range(players):
        current_score = 0
    should_roll = input("would you like to roll (y)?"):
    if should_roll.lower() != "y":
        break 

    value = roll()
    if value == 1:
        print("you rolled a 1! turn done!")
        break
    else:
        current_score += value
        print("you rolled a", value)

        print("your current score is:", current_score)

    player_scores[player.idx] += current_score
    print("your total score is:", player_scores[player.idx])

    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print("player number", winning_idx + 1,
          "is the winner with a score of:", max_score)