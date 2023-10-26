import requests
import models
import colorama


def load_word_list():
    r = requests.get('https://random-word-api.herokuapp.com/word?number=10')
    return r.json()


def input_checker(input):
    check = input
    while check != 'Y' or check != 'N':
        check = input('Invalid string please input "Y" or "N"')


def guess_checker(guess, answer):
    if guess == answer:
        return True
