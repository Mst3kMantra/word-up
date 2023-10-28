import colorama
colorama.init(autoreset=True)

# color tester

guess = input('enter guess\n')
word = 'word'
colored_string = ''
str_code = []
for c in guess:
    if c in word:
        str_code.append(1)
    else:
        str_code.append(0)
for i in range(len(word)):
    if word[i] == guess[i]:
        str_code[i] = 2
for x in range(len(str_code)):
    if str_code[x] == 0:
        colored_string = colored_string + (colorama.Style.RESET_ALL + guess[x])
    elif str_code[x] == 1:
        colored_string = colored_string + (colorama.Fore.YELLOW + guess[x])
    elif str_code[x] == 2:
        colored_string = colored_string + (colorama.Fore.GREEN + guess[x])
for n in str_code:
    print(n)
print(colored_string)
