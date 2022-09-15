import os
import requests
import datetime
from time import time
from alive_progress import alive_bar
from colorama import Fore, Back, Style, init
import urllib3

init()

Tanggal = datetime.datetime.now()
file_name = Tanggal.strftime("%d%b%Y_%H%M%S")	
def directorychecker(link):
	print(Fore.YELLOW +"#####################################################################################################################"+ Style.RESET_ALL)
	print(Fore.YELLOW +"Scanner Directory Web"+ Style.RESET_ALL)
	print(Fore.YELLOW +"#####################################################################################################################"+ Style.RESET_ALL)
	with open('././wordlist/directory.txt','r') as f:
		data = f.readlines()

	headers = {

		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}

	#menghitung keseluruhan data pada wordlist
	jumlah = sum(1 for _ in data)

	with alive_bar(jumlah, force_tty=True,bar='classic' , spinner='classic') as Bar:
		for i in range(0,len(data)):
			try:
				payload = data[i].rstrip('\n')
				urllib3.disable_warnings()
				req = requests.get(link+payload,verify=False, headers = headers, timeout=150,allow_redirects=False)
				status = int(req.status_code)
				if(int(status) == 403):
					print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW +"{} : {}".format(req.url + Style.RESET_ALL ,req.status_code), Fore.RED + " Forbidden" + Style.RESET_ALL)
				elif(int(status) == 404):
					print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW +"{} : {}".format(req.url + Style.RESET_ALL ,req.status_code), Fore.BLUE + " Not Found" + Style.RESET_ALL)

				else:
					print(Fore.GREEN +"[SUCCESS]", Style.RESET_ALL,Fore.YELLOW +"{} : {}".format(req.url + Style.RESET_ALL ,req.status_code), Fore.GREEN + " Live" + Style.RESET_ALL)
				Bar()
			except requests.exceptions.RequestException as e:
				print(e)