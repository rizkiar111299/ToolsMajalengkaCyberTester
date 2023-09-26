import os
import requests, builtwith
import datetime
from alive_progress import alive_bar
import urllib3
from colorama import Fore, Back, Style, init

init()

def adminfinder():   
    print(Fore.YELLOW + "##########################################")
    print("Scanner Find Admin panel")
    print("##########################################"+ Style.RESET_ALL)
    link = str(input(Fore.YELLOW + "Masukan Link Target : "+ Style.RESET_ALL))
    #CMS Detection Start
    urllib3.disable_warnings()
    print("")
    print(Fore.YELLOW +"##########################"+ Style.RESET_ALL, Fore.YELLOW +"WebServer FingerPrint"+ Style.RESET_ALL, Fore.YELLOW +"##########################"+ Style.RESET_ALL)
    a = link.rsplit('/')
    if not 'https://' in a[2] or not 'http://' in a[2]:
        target = 'http://'+a[2]
    info = builtwith.parse(target)
    for name in info:
        value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val) 
        print(name+': '+value)
    print(Fore.YELLOW +"###########################################################################"+ Style.RESET_ALL)
    print("")
    #CMS Detection End
    with open('././wordlist/adminfinder.txt','r') as py:
        dict_admin = py.readlines()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
    with alive_bar(415, force_tty=True, bar='classic' , spinner='classic') as Bar:
        for i in range(0,len(dict_admin)):
            try:
                pay = dict_admin[i].rstrip('\n')
                urllib3.disable_warnings()
                req2 = requests.get(link+pay, headers = headers, timeout=150, verify=False, allow_redirects=True)
                if req2.status_code == 403:
                    print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW +"{} : {}".format(req2.url + Style.RESET_ALL, req2.status_code), Fore.YELLOW + " Forbidden" + Style.RESET_ALL)
                elif req2.status_code == 200:
                    print(Fore.GREEN +"[SUCCESS]", Style.RESET_ALL,Fore.YELLOW +"{} : {}".format(req2.url + Style.RESET_ALL ,req2.status_code), Fore.GREEN + " Live" + Style.RESET_ALL)
                Bar()            
            except requests.exceptions.RequestException as e:
                print(e) 
