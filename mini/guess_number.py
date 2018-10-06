#! /usr/bin/env python3
# *_* encoding: utf-8 *_*


import random
import traceback

# Define constants to avoid magic numbers
start = 0
stop = 101
step = 1
secret_number = random.randrange(start, stop, step)
remaining_guesses = 6

print('--- GUESS THE NUMBER---')
print('Please guess the secret number between {start} and {stop}. You have {remaining} attempts!'.format(start=start, stop=stop-1, remaining=remaining_guesses))

while True:
    # Once the user input something, he use up 1 attemp.
    guess = input('Your number is:')
    remaining_guesses -= 1

    try:
        guess = int(guess)
    except ValueError:
        print(traceback.format_exc())
        print('You must input an integer.')
    else:
        if guess == secret_number:
            print('Correct! You win!')
            break
        elif guess > secret_number:
            print('Higher!')
        elif guess < secret_number:
            print('Lower!')

        if remaining_guesses > 0:
            print('You have %d attempts now.' % remaining_guesses)
        else:
            print('Sorry! You Lose! The secret number is %d!' % secret_number)
            break
