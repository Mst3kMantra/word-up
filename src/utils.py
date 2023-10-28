import requests


def load_word_list():
    r = requests.get('https://random-word-api.herokuapp.com/word?number=10')
    return r.json()
