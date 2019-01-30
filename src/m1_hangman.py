"""
Hangman.

Authors: Jack Franey and Jake Lauteri and Josiah Hasegawa.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random

def main():
    min_length = get_min_length()
    secret_word = get_word(min_length)
    game_loop(secret_word)


    # list = [spaces(secret_word)]
    # print(list)
    #
    # lst1 = []
    # for j in range(5+ len(secret_word)):
    #     lst1 = lst1 + [guess(secret_word)]
    #
    # for q in range(len(lst1)):
    #     for t in range(len(lst1[q])):
    #         change_word(lst1, list, secret_word[lst1[q][t]])


def get_word(min_length):

    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    # min_length = get_min_length()
    while True:

        r = random.randrange(0,len(words))
        secret_word = words[r]
        print(secret_word)
        if len(secret_word) >= min_length:
            return secret_word

def get_min_length():

    min_length = int(input('Enter the minimum length of the secret word:'))
    print(min_length)
    return min_length

def game_loop(secret_word):
    chances = 5
    spaces = []
    for _ in range(len(secret_word)):
        spaces = spaces + ['_']

    letter = guess()
    letter, k, result = check_guess(secret_word,letter,chances)
    spaces, letter = stuff_right(secret_word,letter,spaces)
    change_word(spaces)
    end_of_game(spaces, result, secret_word, chances)

def guess():

    letter = str(input('Enter a letter: '))
    return letter

def check_guess(secret_word,letter,chances):
    result = 'Correct'
    for k in range(len(secret_word)):
        if secret_word[k] == letter:
            return letter, k, result
        else:
            chances = chances - 1
            result = 'Wrong'
            return chances, None, result

def stuff_right(secret_word,letter,spaces):
    right = []
    for k in range(len(secret_word)):
        if secret_word[k] == letter:
            right = right + [secret_word[k]]
    for j in range(len(right)):
        if letter == right[j]:
            spaces[j] = letter
    return spaces, letter

    # for k in range(len(some_list)):
    #     secret_word[some_list[k]] = (w)
    # print(secret_word)
    # return secret_word

def change_word(spaces):
    blanks = ''
    for k in range(len(spaces)):
        blanks = blanks + spaces[k] + ' '
    print(spaces)

def end_of_game(spaces,result,secret_word,chances):
    if win(spaces,secret_word) == True:


def win(spaces,secret_word):
    number_right = 0
    for k in range(len(secret_word)):
        if spaces[k] == secret_word[k]:
            number_right = number_right +1
    if number_right == len(secret_word):
        return True
    else: return False




main()