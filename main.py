# RJ FISHER
# WORDLE TYPE GUESSING GAME
import random
import numpy as np


# Print introduction before each completely new game.
def intro():
    print("Can you guess the word?")
    print("You will have 6 chances to guess a 5 letter word.")


def user_input():
    while True:
        guess = input("Enter a 5-letter Word :")
        if type(guess) != str or len(guess) != 5:
            print('Invalid Entry')
            continue
        else:
            return guess.upper()


# get random word from a list of 5-letter words.
def getWord():
    filename = 'FiveLetterWords.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=str)
    magicWord = random.choice(data)
    return magicWord


def play_game():
    magicWord = getWord()
    magic = np.array(list(magicWord.upper()))
    # print(true_arr)
    magic_idx = [[item, idx, None] for idx, item in enumerate(magic)]

    attempts = 0
    guess_store = []
    while attempts < 6:
        guess_word = user_input()
        guess_arr = np.array(list(guess_word))
        # print(guess_arr)
        guess_idx = [[item, idx, None] for idx, item in enumerate(guess_arr)]
        # print(guess_idx)
        matched = []
        existing = []
        matching = np.where(magicWord == guess_arr)[0]

        for item in matching:
            matched.append(guess_idx[item][0])
            guess_idx[item][2], magic_idx[item][2] = 'YES', 'YES'

            rem_guess = [item for item in guess_idx if item[2] != 'YES']
            rem_true = [item for item in magic_idx if item[2] != 'YES']

            for guess in rem_guess:
                for true in rem_true:
                    if guess[0] == true[0]:
                        if list(magicWord).count(guess[0]) > (matched.count(guess[0]) + existing.count(guess[0])):
                            existing.append(guess[0])
                            guess[2], true[2] = 'EX', 'EX'
                        else:
                            continue

                    # Apply logic to each value in DataFrame to Color letters

                def color_positive(val):
                    if val == val.upper() and len(val) == 1:
                        color = 'green'
                    elif len(val) == 2:
                        color = 'orange'
                    else:
                        color = 'black'
                    return 'color: %s' % color

                    # Mark letters based on match, exist, or not exist

                ###
                # final = mark_letters(guess_idx)

                # Turn current guess word into row in pandas DF
                # guess_df = build_df(attempt, final)
                # guess_store.append(guess_df)
                # new_df = pd.concat(guess_store)
                ###

                # Use color_positive function to color letters
                # s = new_df.style.applymap(color_positive)
                # display(s)

                if guess_word.lower() == magicWord:
                    print('##############################################################')
                    print(f'       HURRAY THE WORD WAS: {magicWord.upper()} ')
                    print('##############################################################')
                    print('YOU ARE A HUMAN GENIUS! YOU SHOULD BE FEARED AND RESPECTED!!!')
                    print('Give yourself a pat on the shoulder :)')
                    print("That student debt is finally paying off!!!")
                    print("WANNA PLAY AGAIN?")
                    break
                else:
                    attempts += 1

                    if attempts == 6:
                        print(f'Sorry, gotta read more BOOKS! The word was {magicWord.upper()}, OBVIOUSLY...')
                        break


intro()
getWord()
user_input()
play_game()
