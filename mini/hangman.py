#! /usr/bin/env python3
# _*_ encoding: utf-8 _*_


import random

print(" --- HANGMAN --- \n")
print("Let's play! Guess the word if you don't want to hang!\n")

# computer chooses a word to guess
words = ["carrot", "dragon", "computer", "elephant", "letter", "window", "pearl", "house",\
                 "rabbit", "orange", "adventure", "mirror", "kitchen", "example", "picture", "telephone"\
	         "money", "weather", "beauty", "nothing", "birthday", "airport", "decision", "driver"\
		 "opportunity", "advertisement", "entertainment", "mountain", "button", "hairdresser"]
secret_word = random.choice(words)
board = "*" * len(secret_word)
letters = []
guess = 0
play = True

while play:
    letter = input("\nEnter a letter to guess: ").lower()

    if letter in letters:
        print("You've entered this letter before.")
    else:
        letters.append(letter)

    # Use up 1 chance only if missed.
    if letter not in secret_word:
        guess += 1

    for i in range(len(secret_word)):
        if secret_word[i] == letter:
            board = board[:i] + letter + board[i+1:]
    print(board)

    # If player win, end the game.
    if board == secret_word:
        play = False
        print("\nCongratulation! You won!")

    print("")

    # Draw hangman. If played more than 6 times, end the game.
    if guess >6:
            play = False
            print("Sorry but you didn't guess and now you're a HANGMAN!")
            print("(BTW this secret word is: " +  secret_word + ")")
            print("______ ")
    if guess >5:
            print("|/ |  ")
    if guess >4:
            print("|  O  ")
    if guess >3:
            print("| /|\ ")
    if guess >2:
            print("| / \ ")
    if guess >1:
            print("|      ")
    if guess >0:
            print("======")

print("\nBye, bye!")
