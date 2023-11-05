import requests


def load_word_list():
    r = requests.get('https://random-word-api.herokuapp.com/word?number=10&length=4')
    return r.json()



def get_example():
    r = requests.get(f'https://random-word-api.herokuapp.com/word?length=4')
    return r.json()