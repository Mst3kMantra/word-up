import colorama
import random

def bool_input_checker(prompt):
    check = prompt
    valid_answers = ['Y', 'N']
    while check not in valid_answers:
        check = input('Invalid string please input "Y" or "N"')


def command_checker(command):
    match command:
        case '_help':
            print('Type _quit to exit')
            print('Type _skip to move to next word')
            print('Type _help to see commands again\n')
            return True
        case '_quit':
            input('Program closing. Press enter to close.')
            exit()
        case '_skip':
            return False
        case _:
            return


def guess_checker(guess, answer):
    results = {}
    if guess == answer:
        results['bool'] = True
        return results
    elif guess != answer:
        colored_string = ''
        str_code = []
        for c in guess:
            if c in answer:
                str_code.append(1)
            else:
                str_code.append(0)
        for i in range(len(answer)):
            if answer[i] == guess[i]:
                str_code[i] = 2
        for x in range(len(str_code)):
            if str_code[x] == 0:
                colored_string = colored_string + \
                    (colorama.Style.RESET_ALL + guess[x])
            elif str_code[x] == 1:
                colored_string = colored_string + \
                    (colorama.Fore.YELLOW + guess[x])
            elif str_code[x] == 2:
                colored_string = colored_string + \
                    (colorama.Fore.GREEN + guess[x])
        results['bool'] = False
        results['string'] = colored_string
        return results


def score_add(guesses, streak):
    points = 0
    if guesses == 10:
        points = 1000
    elif guesses >= 8 and guesses <= 9:
        points = 800
    elif guesses >= 4 and guesses <= 7:
        points = 500
    elif guesses > 0 and guesses <= 3:
        points = 300
    if streak > 0:
        points *= streak
    print(f'You recieved {points} points')
    return points

def print_hint(word):
    if 'Noun' in word.meanings and word.meanings != None:
        print(f'Word is a noun meaning {random.choice(word.meanings['Noun'])}\n')
    elif 'Verb' in word.meanings and word.meanings != None:
        print(f'Word is a verb meaning {random.choice(word.meanings['Verb'])}\n')