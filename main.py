import os
from tools.main import *
from tools.DIRECTORITRAVERSAL import *
from tools.SQL import *
from tools.XSS import *
from tools.adminfinder import *
from tools.brutev1 import *
from tools.brutev2 import *
from plugins.header import menu
from colorama import Fore, Back, Style, init

init()
os.system("cls")
print(menu.header())
pilihan = int(input(Fore.YELLOW +"Masukan Menu : " + Style.RESET_ALL))
if(1 == pilihan):
	os.system("cls")
	print(menu.header())
	print(bruteV1())
elif(2 == pilihan):
	os.system("cls")
	print(menu.header())
	print(bruteV2())
elif(3 == pilihan):
	os.system("cls")
	print(menu.header())
	link = str(input(Fore.YELLOW +"Masukan Link Website : "+ Style.RESET_ALL))
	print(directorychecker(link))
elif(4 == pilihan):
	os.system("cls")
	print(menu.header())
	link = str(input(Fore.YELLOW +"Masukan Link Website : "+ Style.RESET_ALL))
	print(dTraversal(link))
elif(5 == pilihan):
	os.system("cls")
	print(menu.header())
	print(adminfinder())
elif(6 == pilihan):
	os.system("cls")
	print(menu.header())
	print(xssinjection())
elif(7 == pilihan):
	os.system("cls")
	print(menu.header())
	print(SqlInjection())
else:
	print()