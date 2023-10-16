import os
import platform
from tools.main import *
from tools.DIRECTORITRAVERSAL import *
from tools.SQL import *
from tools.XSS import *
from tools.adminfinder import *
from tools.brutev1 import *
from tools.brutev2 import *
from tools.subdomain import *
from tools.iplocation import *
from tools.directorychecker import *
from plugins.header import menu
from plugins.about import *
from colorama import Fore, Back, Style


if(platform.system() == "Windows"):
	os.system("cls")
elif(platform.system() == "Linux"):
	os.system("Clear")
print(menu.header())
pilihan = int(input(Fore.YELLOW +"Masukan Menu : " + Style.RESET_ALL))
if(1 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header()) 
	print(bruteV1())
elif(2 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header())
	print(bruteV2())
elif(3 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header())
	link = str(input(Fore.YELLOW +"Masukan Link Website : "+ Style.RESET_ALL))
	print(directorychecker(link))
elif(4 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header())
	print(adminfinder())
elif(5 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header())
	link = str(input(Fore.YELLOW +"Masukan Link Website : "+ Style.RESET_ALL))
	print(dTraversal(link))
elif(6 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header())
	print(SqlInjection())
elif(7 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header())
	print(xssinjection())
elif(8 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header())
	ip = str(input(Fore.YELLOW +"Masukan Ip Public : "+ Style.RESET_ALL))
	print(iplocation(ip))
elif(9 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header())
	print(subdomain())
elif(10 == pilihan):
	if(platform.system() == "Windows"):
		os.system("cls")
	elif(platform.system() == "Linux"):
		os.system("Clear")
	print(menu.header())
	print(about())
else:
	print()