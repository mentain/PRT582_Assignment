
#3rd Requirement
points_to_win = 5
CONSTANTS_ROCK = 'ROCK'
selection_list = ("Rock", "Paper", "Scissors")


def who_win(player_action, computer_action):
    
    if player_action.lower() == computer_action.lower():
        print(f"Both players selected {player_action}. It's a tie!")
        return 0
    elif player_action.lower() == "rock":
        if computer_action.lower() == "scissors":
            print("[Player win!")
            return 1
        else:
            print("Player lose.")
            return 2
    elif player_action.lower() == "paper":
        if computer_action.lower() == "rock":
            print("Player win!")
            return 1
        else:
            print("Player lose.")
            return 2
    elif player_action.lower() == "scissors":
        if computer_action.lower() == "paper":
            print("Player win!")
            return 1
        else:
            print("Player lose.")
            return 2
    else:
        print("You entered the wrong input")






