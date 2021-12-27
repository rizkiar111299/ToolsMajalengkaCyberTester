import os
import requests
import datetime
from progress.bar import Bar
from colorama import Fore, Back, Style, init

init()

Tanggal = datetime.datetime.now()
file_name = Tanggal.strftime("%d%b%Y_%H%M%S")	
def directorychecker(link):
	print(Fore.YELLOW +"Scanner Directory Web"+ Style.RESET_ALL)
	with open('././wordlist/directory.txt','r') as f:
		data = f.readlines()

	headers = {

		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}
	for i in range(0,len(data)):
		payload = data[i].rstrip('\n')
		try:
			req = requests.get(link+payload, headers = headers, timeout=10)
			if req.status_code == 403:
				print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW + "{} : {}".format(req.url + Style.RESET_ALL, req.status_code), Fore.YELLOW + " Forbidden" + Style.RESET_ALL)
			elif req.status_code == 200:
				print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW +"{} : {}".format(req.url + Style.RESET_ALL ,req.status_code), Fore.GREEN + " Live" + Style.RESET_ALL)
				#link_temp = req.url
				#array = []
				#array.append(link_temp)
				simpan_log = "{} \n".format(req.url)
				log = open('././log/crawl/{}.txt'.format(Tanggal.strftime("%d%b%Y_%H%M%S")), 'a')
				log.write(str(simpan_log))
		except requests.exceptions.RequestException as e:
			print(e)
	print("\nScanner Success")
	print("Log Tersimpan Pada Folder log Dengan Nama {}.txt".format(file_name))

"""
	print("################################")
	print("Scanner Directory Traversal")
	print(dTraversal(file_name))	
def dTraversal(file_name):
	with open('././log/crawl/{}.txt'.format(file_name),'r') as link1:
		data2 = link1.readlines()
	with open('././wordlist/directorytraversal.txt','r') as py:
		wordlist_dTraversal = py.readlines()
		
	headers = {

		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
	}
	c = 0
	for i in range(0,len(data2)):
		link_check = data2[i].rstrip('\n')
		for b in range(0,len(wordlist_dTraversal)):
			pay = wordlist_dTraversal[b].rstrip('\n')
			try:
				req2 = requests.get(link_check+pay, headers = headers, timeout=10)
				if 'root:x:0:0:root:/root:/bin/bash' in str(req2.content):
					print("{} : {} Live".format(req2.url,req2.status_code))
				elif req2.status_code == 400:
					print("{} : {} Not Found".format(req2.url,req2.status_code))
				elif req2.status_code == 403:
					print("{} : {} Forbidden".format(req2.url,req2.status_code))
				elif req2.status_code == 500:
					print("{} : {} Internal Server Error".format(req2.url,req2.status_code))
			except requests.exceptions.RequestException as e:
				print(e)
"""