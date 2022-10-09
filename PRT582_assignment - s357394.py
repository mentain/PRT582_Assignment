
import random
def main():
    player_win=0
    cpu_win=0
    while True:
        player_action = input("Enter a choice (rock, paper, scissors): ")
        selection_list = ["Rock", "Paper", "Scissors"]
        computer_action = random.choice(selection_list)
        print(f"\nYou chose {player_action}, computer chose {computer_action}.\n")

        if player_action.lower() == computer_action.lower():
            print(f"Both players selected {player_action}. It's a tie!")
        elif player_action.lower() == "rock":
            if computer_action.lower() == "scissors":
                player_win=player_win + 1
                print("Player win!")
            else:
                cpu_win = cpu_win + 1
                print("Player lose.")
        elif player_action.lower() == "paper":
            if computer_action.lower() == "rock":
                player_win=player_win + 1
                print("Player win!")
            else:
                cpu_win = cpu_win + 1
                print("Player lose.")
        elif player_action.lower() == "scissors":
            if computer_action.lower() == "paper":
                player_win=player_win + 1
                print("Player win!")
            else:
                cpu_win = cpu_win + 1
                print("Player lose.")
        else:
            print("You entered the wrong input")
        if player_win >= 5 or cpu_win >=5:  
           if cpu_win < player_win:
                    print("Player won the game")
           else:
                    print("Computer won the game")  
           print("Final Scores:")
           print(f"Player:{player_win}")
           print(f"Comp:{cpu_win}")  
           play_again = input("Play again? (yes/no): ")
           if play_again.lower() != "yes":
            break
 

if __name__=="__main__":
    main()

