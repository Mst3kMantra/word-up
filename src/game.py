import colorama
from PyDictionary import PyDictionary
import logic
import utils
import models
import random
from datetime import datetime


class WordUp:
    def __init__(self):
        self.seed = random.seed(datetime.now().timestamp())

    def main_loop(self):
        dictionary = PyDictionary()
        colorama.init(autoreset=True)
        while True:
            print('Welcome to WordUp, a word guessing game\n')
            print('Try and guess the word with increasing hints to increase your score!')
            game_query = input('Start a new game?(Y/N)').upper()
            logic.bool_input_checker(game_query)
            print('\nEnter guess when prompted, incorrect guesses will show which characters you entered that were correct. Yellow if in word and green if in word and correct location.\n')
            print('Type quit to exit')
            print('Type skip to move to next word')
            print('Type help to see commands again')
            input('Hit enter to continue')
            if game_query == 'Y':
                game = models.Game(utils.load_word_list())
                while game.round <= 10:
                    print('-----------------------------------------------')
                    print('New round starting!')
                    print(
                        f'------------- Round: {game.round}------------------\n\n')
                    random_word = random.choice(game.words)
                    game.words.remove(random_word)
                    word = models.Word(random_word, dictionary.meaning(
                        random_word), dictionary.synonym(random_word), dictionary.antonym(random_word))
                    round = models.Round()
                    guess = ''
                    while guess != word.name and round.guesses > 0:
                        print(f'{round.guesses} left')
                        print(f'The word is {word.length}(s) long\n')
                        guess = input('Enter your guess here').lower()
                        check = logic.command_checker(guess)
                        if check == True:
                            guess = input('Enter your guess here').lower()
                        elif check == False:
                            print('Skipping to next round')
                            game.round += 1
                            break
                        while len(guess) != word.length or dictionary.meaning(guess) is None:
                            print(f'The word is {word.length}(s) long\n')
                            guess = input(
                                'Invalid input. Guess is either incorrect length or not in dictionary. Try Again').lower()
                            # todo create guess interpreter and command to display current discovered correct characters
                        result = logic.guess_checker(guess, word.name)
                        if result['bool']:
                            print('')
            else:
                input('Closing game. Press enter to close')
                exit()
