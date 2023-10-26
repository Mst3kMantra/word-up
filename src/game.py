import colorama
from PyDictionary import PyDictionary
import utils
import models
import random
from datetime import datetime
dictionary = PyDictionary()
colorama.init(autoreset=True)


class WordUp:
    def __init__(self):
        self.seed = random.seed(datetime.now().timestamp())

    def main_loop(self):
        while True:
            print('Welcome to WordUp, a word guessing game\n')
            print('Try and guess the word with increasing hints to increase your score!')
            game_query = input('Start a new game?(Y/N)').upper()
            utils.input_checker(game_query)
            print('Type quit to exit')
            print('Type skip to move to next word')
            print('Type hint to recieve a hint')
            print('Type help to see commands again')
            input('Hit enter to continue')
            if game_query == 'Y':
                game = models.Game(utils.load_word_list())
                while game.round != 10:
                    print('-------------------------------')
                    print('New round starting!')
                    print('-------------------------------\n\n')
                    random_word = random.choice(game.words)
                    game.words.remove(random_word)
                    word = models.Word(random_word, dictionary.meaning(
                        random_word), dictionary.synonym(random_word), dictionary.antonym(random_word))
                    round = models.Round()
                    guess = ''
                    while guess != word.name or round.guesses > 0:
                        print(f'The word is {word.length}(s) long')
                        guess = input().lower()
                        # add command checker here
                        while len(guess) != word.length or dictionary.meaning(guess) is None:
                            guess = input(
                                'Invalid input. Guess is either incorrect length or not in dictionary. Try Again')
                            # todo create guess interpreter and command to display current discovered correct characters
            else:
                exit()
