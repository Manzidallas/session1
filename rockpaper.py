# A program that generates a random and a user has to guess that number 

import random

game = ["rock", "paper", "scissor"]
#          1       2       3

def announce(user, computer):
    # cpu_chosen = computer-1
    usr_chosen = user -1

    print(f"You chose {game[usr_chosen]} and,")
    print(f"the computer chose {game[computer-1]}")

while True:

    computer = random.randint(1,3)
    user = int(input("Insert the integer: "))
    num = [1,2,3]
    if user in num:
        if (computer == 1 and user==3) or (computer == 2 and user==1) or (computer == 3 and user==2):
            print("You lose")
            announce(user, computer)
            continue
        elif (computer == user):
            print("Draw")
            announce(user, computer)
            continue
        else:
            print("You won")
            announce(user, computer)
            continue
    else:
        print("Please make sure you provided a number between 1 to 3")
        break




















# user = int(input("Input your guess number from 1-10"))

# if user == num_randomise:
#     print("You won")
# else:
#     print("You lost")

# print(num_randomise)