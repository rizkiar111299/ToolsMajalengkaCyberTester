import os
import requests
import datetime
from progress.bar import Bar
import urllib3
from colorama import Fore, Back, Style, init

init()

def adminfinder():   
    print(Fore.YELLOW + "##########################################")
    print("Scanner Find Admin panel")
    print("##########################################"+ Style.RESET_ALL)
    link = str(input(Fore.YELLOW + "Masukan Link Target : "+ Style.RESET_ALL))
    with open('././wordlist/adminfinder.txt','r') as py:
        payload_Sql = py.readlines()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
    for b in range(0,len(payload_Sql)):
        pay = payload_Sql[b].rstrip('\n')
        try:
            urllib3.disable_warnings()
            req2 = requests.get(link+pay, headers = headers, timeout=150,verify=False)
            if req2.status_code == 403:
                print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW +"{} : {}".format(req2.url + Style.RESET_ALL, req2.status_code), Fore.YELLOW + " Forbidden" + Style.RESET_ALL)
            elif req2.status_code == 200:
                print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW +"{} : {}".format(req2.url + Style.RESET_ALL ,req2.status_code), Fore.GREEN + " Live" + Style.RESET_ALL)
        except requests.exceptions.RequestException as e:
                print(e)
    print("Scanner Selesai")
