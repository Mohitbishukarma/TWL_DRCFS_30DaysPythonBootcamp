import random

# variables
player_score = 0
computer_score = 0
game = 1
options  = ("rock", "paper","scissors")

# game loop
while round<=5:

    # optints showing
    print(f"<{'-'*10} ROUND : {round} {'-'*10}>")
    print(f"1. {options[0]}\t2. {options[1]}\t3. {options[2]}")
    print(f"<{'-'*31}>")
    
    # geting moves
    player_move = input("Enter your move: ")
    computer_move = options[random.randint(0,2)]
    
    # testing 
    print((player_move,computer_move),(player_score,computer_score))

    # scoring logic
    if player_move == computer_move:
        print("The game is tie.\n")
    else:
        if player_move == "rock" and computer_move == "scissors":
            player_score += 1
            print("You got +1 score\n")
        elif player_move == "scissors" and computer_move == "paper":
            player_score += 1
            print("You got +1 score\n")
        elif player_move == "paper" and computer_move == "rock":
            player_score += 1
            print("You got +1 score\n")
        else:
            computer_score += 1
            print("Computer got +1 score\n")
    round += 1

# winner checking
print(f"\n<{'-'*10} Result {'-'*10}>")
print(f"Your Score : {player_score}\nComputer Score : {computer_score}")
if player_score>computer_score:
    print("You win.")
elif player_score == computer_score:
    print("Draw")
else:
    print("You Lose.")

