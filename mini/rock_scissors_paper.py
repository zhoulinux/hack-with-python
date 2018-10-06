#! /usr/bin/env python3
# _*_ encoding: utf-8 _*_


import random

keep_playing = True
count_round = 0
count_win = 0
choices = {'R': 'Rock', 'S': 'Scissors', 'P': 'Paper'}

print("Let's play!")

while keep_playing:
    count_round += 1

    player_choice = input("\nRock[R], Scissor[S], or Paper[P]? ").upper()
    if player_choice in choices.keys():
        player_choice = choices[player_choice]
    else:
        print("You must choose Rock[R], Scissors[S], or Paper[P]. Try again!")
        continue

    computer_choice = random.choice(list(choices.values()))
    print("Your choice is:", player_choice)
    print("Computer choice is:", computer_choice)

    if player_choice == computer_choice:
        print("Tie.")
    else:
        player_win = False
        if player_choice == 'Rock' and computer_choice == 'Scissors':
            player_win = True
        elif player_choice == 'Scissors' and computer_choice == 'Paper':
            player_win = True
        elif player_choice == 'Paper' and computer_choice == 'Rock':
            player_win = True

        if player_win:
            print("You won.")
            count_win += 1
        else:
            print("Computer won.")

    while True:
        finish = input("\nDo you want to keep playing? Yes or no [Y/N]? ").upper()
        if finish == "Y":
            keep_playing
        elif finish == "N":
            keep_playing = False
            print("Number of played games:", count_round)
            print("You winning turns:", count_win)
            print("Thank you for playing!")
        else:
            print("Please enter yes or no [Y/N].")
            continue

        break
