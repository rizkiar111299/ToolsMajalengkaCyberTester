from colorama import Fore, Back, Style, init

init()

print(Fore.YELLOW + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')