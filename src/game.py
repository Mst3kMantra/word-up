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
            print('Try and guess the 4 letter word with increasing hints to increase your score!')
            game_query = input('Start a new game?(Y/N)').upper()
            logic.bool_input_checker(game_query)
            if game_query == 'Y':
                print('\nEnter guess when prompted, incorrect guesses will show which characters you entered that were correct. Yellow if in word and green if in word and correct location.\n')
                print('Type _quit to exit')
                print('Type _skip to move to next word')
                print('Type _help to see commands again\n')
                input('Hit enter to continue')
                game = models.Game(utils.load_word_list())
                while game.round <= 10:
                    print('-----------------------------------------------')
                    print('New round starting!')
                    print(
                        f'------------- Round: {game.round}------------------\n\n')
                    random_word = random.choice(game.words)
                    game.words.remove(random_word)
                    word = models.Word(random_word, dictionary.meaning(
                        random_word))
                    #check if word is in dictionary and request word if not in until word in dictionary found
                    attempts = 1
                    while word.meanings == None or word.length != 4:
                        print(f'Invalid word, finding new word. Attempt {attempts}')
                        new_word = utils.get_example()
                        word = models.Word(new_word[0], dictionary.meaning(new_word[0]))
                        attempts += 1
                    round = models.Round()
                    guess = ''
                    while guess != word.name and round.guesses > 0:
                        print(f'\n{round.guesses} guesses left')
                        print(f'Try to guess the 4 letter word')
                        example = utils.get_example()
                        print(f'An example of a {word.length} letter word is {example[0]}')
                        logic.print_hint(word)
                        if len(round.guess_strings) > 0:
                            print('\nPrevious attempts:')
                            for s in round.guess_strings:
                                print(s)
                        guess = input('Enter your guess here\n').lower()
                        check = logic.command_checker(guess)
                        if check == True:
                            guess = input('Enter your guess here\n').lower()
                        elif check == False:
                            print('Skipping to next round')
                            game.round += 1
                            break
                        while len(guess) != word.length or dictionary.meaning(guess) is None:
                            check = logic.command_checker(guess)
                            if check == True:
                                guess = input('Enter your guess here\n').lower()
                            elif check == False:
                                break
                            else:
                                guess = input(
                                    'Invalid input. Guess is either incorrect length or not in dictionary. Try Again\n').lower()
                        if check == False:
                            print('Skipping to next round')
                            game.round += 1
                            print(f'Word was {word.name}')
                            check = None
                            break
                        result = logic.guess_checker(guess, word.name)
                        if result['bool']:
                            game.score = logic.score_add(
                                round.guesses, game.streak)
                            game.streak += 1
                            game.round += 1
                            print(f'\nCorrect, word was {word.name}')
                            print(f'Score is {game.score} with a streak of {game.streak}')
                            input('Enter to continue\n')
                        elif result['bool'] == False:
                            round.guesses -= 1
                            round.guess_strings.append(result['string'])
                            print(f'\nIncorrect guess, {round.guesses} left')
                            print(result['string'])
                            if round.guesses == 0:
                                print(f'\nWord was {word.name}')
                                input('Enter to continue\n')
                print(f'Game over, final score was {game.score}')
            else:
                input('Closing game. Press enter to close')
                exit()
