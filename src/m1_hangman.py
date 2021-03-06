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
    wrong = 0
    spaces = []
    for _ in range(len(secret_word)):
        spaces = spaces + ['_']
    while True:
        letter = guess()
        letter, result, k = check_guess(secret_word,letter,wrong)
        progress, right = stuff_right(secret_word,letter,spaces)
        change_word(progress)
        message, wrong = end_of_game(progress, right, result, wrong)
        print(message)
        if message == 'Loser':
            print('The word was:', secret_word)
            break
        elif message == 'Winner':
            break

def guess():
    letter = str(input('Enter a letter: '))
    return letter

def check_guess(secret_word,letter,chances):
    result = 'Correct'
    for k in range(len(secret_word)):
        if secret_word[k] == letter:
            print('Wrong guesses left: ', chances)
            return letter, result, k
        else:
            chances = chances - 1
            result = 'Wrong'
            print(result, 'Wrong guesses left: ', chances)
            return chances, result, None

def stuff_right(secret_word,letter,spaces):
    right = []
    for k in range(len(secret_word)):
        right = right + [secret_word[k]]
    for j in range(len(secret_word)):
        if letter == right[j]:
            spaces[j] = letter
    return spaces, right

    # for k in range(len(some_list)):
    #     secret_word[some_list[k]] = (w)
    # print(secret_word)
    # return secret_word

def change_word(spaces):
    blanks = ''
    for k in range(len(spaces)):
        blanks = blanks + spaces[k] + ' '
    print(blanks)

def end_of_game(progress,right,result,wrong):
    message = ''
    if win(progress,right) == True: #problem might be with win function?
        message = 'Winner'
    if result == 'Wrong':
        wrong = wrong + 1
    if wrong == 5:
        message = 'Loser'
    return message

# def win(spaces,right):
#     number_right = 0
#     for k in range(len(spaces)):
#         if spaces[k] == right[k]:
#             number_right = number_right +1
#     if number_right == len(right):
#         return True
#     else:
#         return False

def win(spaces, right):
    count = 0
    for k in range(len(spaces)):
        if spaces[k] == right[k]:
            count = count + 1
    if count == len(right):
        return True
    else:
        return False




main()