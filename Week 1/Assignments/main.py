import random

# variables
player_score = 0
computer_score = 0
game = 1
options  = ("rock", "paper","scissors")

# game loop
while game<=5:
    # options showing
    print(f"{'-'*10} Game : {game} {'-'*10}")
    print(f"1. {options[0]}    2. {options[1]}    3. {options[2]}")
    print(f"{'-'*30}")
    
    # geting moves
    computer_move = options[random.randint(0,2)]
    player_move = input("Enter your move: ")
    
    # winner checking
    if player_move in options:
        if player_move == computer_move:
            print("The game is tie.\n")
        else:
            if player_move == "rock" and computer_move == "scissors":
                player_score += 1
                print("You win.\n")
            elif player_move == "scissors" and computer_move == "paper":
                player_score += 1
                print("You win.\n")
            elif player_move == "paper" and computer_move == "rock":
                player_score += 1
                print("You win.\n")
            else:
                computer_score += 1
                print("You Lose.\n")
        game += 1
    else:
        print("Please, enter the right move.\n")

# final score
print(f"\n<{'-'*10} Final Score {'-'*10}>")
print(f"Your Score : {player_score}\nComputer Score : {computer_score}")




#   # #testing 
    # print()
    # print((player_move,computer_move),(player_score,computer_score))
    # print()