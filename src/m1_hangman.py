"""
Hangman.

Authors: Jack Franey and Jake Lauteri and Josiah .
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random

def main():
    print('boobs')
    # get_min_length()
    #print(get_word())
    secret_word = get_word()
    list = [spaces(secret_word)]
    print(list)
    guess(secret_word)



def get_word():

    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
    min_length = get_min_length()
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

def guess(secret_word):
    lst = []
    g = str(input('Enter a letter: '))
    for k in range(len(secret_word)):
        if secret_word[k] == g:
            lst = lst + [k]
    return lst

def spaces(secret_word):

    list = []
    for k in range(len(secret_word)):
        list = list + ['*']

    return list

def change_word(some_list, secret_word, w):
    









main()