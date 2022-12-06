# Number guesser game

# importing modules
import random

# generating random number between 1 and 10
random_number = random.randint(1,10)

# variables 
guesses = 0

while True:
    user_number = int(input("Enter your guess between 1 and 10: "))
    if user_number>random_number:
        guesses +=1
        if guesses== 5:
            print(f"Game Over. The acutal number is {random_number}\n")
            break
        else:
            print(f"Your guess is too high.\t[Remaining Guesses: {5-guesses}]\n")
    elif user_number<random_number:
        guesses += 1
        if guesses==5:
            print(f"Game Over. The acutal number is {random_number}\n")
            break
        else:
            print(f"Your guess is too low.\t[Remaining Guesses: {5-guesses}]\n")
    elif user_number == random_number:
        guesses += 1
        print(f"You guessed it right in {guesses} attempts.\n")
        break