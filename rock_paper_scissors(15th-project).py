# ROCK-PAPER-SCISSORS Game

"""import random

options = ["rock","paper","scissors"]
print("What do you want to choose? rock , paper , scissors or exit ?")
user_action = input()
computer_action = random.choice(options)


def game(user_action,computer_action):
    user_points = 0
    computer_points = 0
    exit = False

    if user_action == 'exit':
        print("Game ended")
        print("You won a total score of "+str(user_points)+"and the computer total score is"+str(computer_points))
        exit = True

    while exit == False:
        if user_action == computer_action:
            print("SHOOT,it's a draw ! ")
            break

        elif user_action == 'rock':
            if computer_action == 'scissors':
                print("user input rock")
                print("computer input scissors")
                print("Rock smashes scissors! You win!")
                user_points += 1
            elif computer_action == 'paper':
                print("user input rock")
                print("computer input paper")
                print("Paper covers rock! You lose.")
                computer_points += 1
        elif user_action == 'scissors':
            if computer_action == 'paper':
                print("user input scissors")
                print("computer input paper")
                print("Scissors cuts paper! You win!")
                user_points += 1
            elif computer_action == 'rock':
                print("user input scissors")
                print("computer input rock")
                print("Rock smashes scissors! You lose.")
                computer_points += 1

        elif user_action == 'paper':
            if computer_action == 'rock':
                print("user input paper")
                print("computer input rock")
                print("Paper covers rock! You win!")
                user_points += 1
            elif computer_action == 'scissors':
                print("user input paper")
                print("computer input scissors")
                print("Scissors cuts paper! You lose.")
                computer_points += 1

        elif user_action != "rock" or user_action != "paper" or user_action != "scissors"or user_action != "exit":
            print("Invalid input ")



game(user_action,computer_action)



#             ...............................infinity hocche....................................










"""

# --------------------------------------Done--------------------------------------------


import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s tie'

    # r > s, s > p, p > r (meaning that rock beats scissors, scissors beats paper,  paper beats rock)
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'


def is_win(player,opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
     or (player == 'p' and opponent == 'r'):
        return True


print(play())





