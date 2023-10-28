

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
    if guess == answer:
        return True
