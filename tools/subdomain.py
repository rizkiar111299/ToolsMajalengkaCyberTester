import requests
import datetime
import time
import urllib3
from colorama import Fore,Back,Style,init
init()

def subdomain():
    try:
        site = input((str(Fore.YELLOW+"Masukan Domain xample.com : "+Style.RESET_ALL)))
        urllib3.disable_warnings()
        link = requests.get("https://api.hackertarget.com/hostsearch/?q="+site,verify=False,timeout=150)
        print(Fore.YELLOW+"\n###################################### Subdomain Scanner ######################################"+ Style.RESET_ALL)
        print(Fore.YELLOW+link.text+Style.RESET_ALL)
        print(Fore.YELLOW+"################################################################################################"+ Style.RESET_ALL)

    except:
        print('')