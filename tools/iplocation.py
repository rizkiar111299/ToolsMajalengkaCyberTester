import requests
import os
import sys
import ipapi
from colorama import Fore, Back, Style, init
init()

def iplocation(ip):
    site = ip
    source = ipapi.location(ip=site, key=None,)
    try:
        print(Fore.GREEN+" [!]"+Fore.RED+" See your info")
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" ip = "+ source["ip"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" city = " + source["city"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" region = "+ source["region"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" id country = "+source["country"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" country = "+ source["country_name"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" Calling Code = "+source["country_calling_code"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" Languages = "+source["languages"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" org = "+ source["org"]+ Style.RESET_ALL)
    except:
        print(Fore.RED+"Sorry Please Enter IP Address"+ Style.RESET_ALL)