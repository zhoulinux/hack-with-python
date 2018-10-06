#! /usr/bin/env python3
# _*_ encoding: utf-8 _*_


import random

print (" --- MASTERMIND --- \n")
print ("Guess the secret color code in as few tries as possible.\n")
print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W) and pink(P)")

colors = ["R", "G", "B", "Y", "W", "P"]
attempts = 0
game = True

while game:
    color_code = random.sample(colors, 4)
    guessed_color = ""
    player_guess = input().upper()
    attempts += 1

    # Check if player's input is correct.
    if len(player_guess) != len(color_code):
        print ("\nThe secret code has exactly four colors. I know, you can count to four. Try again!")
        continue

    for i in range(4):
        if player_guess[i] not in colors:
            print ("\nLook up what colors you can use in this game. You are not a daltonist, are you?")
            continue

    # Comparison between player's input and secret code.
    for i in range(4):
        if player_guess[i] == color_code[i]:
            guessed_color += "X"
        else:
            guessed_color += "O"
    print(guessed_color + "\n")

    # Halt the game either win or attempt more than 6 times.
    if guessed_color == "XXXX":
        if attempts == 1:
            print ("Wow! You guessed at the first attempt!")
        else:
            print ("Well done... You used", attempts, "attempts to guess.")
        game = False
    else:
        if attempts >= 1 and attempts < 6:
            print ("Next attempt: ")
        elif attempts >= 6:
            print ("You didn't guess! The secret color code was:", color_code)
            game = False

    # Play or not to play.
    while game == False:
        finish = input("\nDo you want to play again (Y/N)? ").upper()
        attempts = 0
        if finish == "N":
            print ("Thanks for the game! Bye, bye!")
            break
        elif finish == "Y":
            game = True
            print ("So, let's play again... Guess the secret code: ")
