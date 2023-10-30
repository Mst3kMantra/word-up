import colorama


def bool_input_checker(input):
    check = input
    while check != 'Y' or check != 'N':
        check = input('Invalid string please input "Y" or "N"')


def command_checker(input):
    match input:
        case 'help':
            print('Type quit to exit')
            print('Type skip to move to next word')
            print('Type help to see commands again\n')
            return True
        case 'quit':
            input('Program closing. Press enter to close.')
            exit()
        case 'skip':
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
