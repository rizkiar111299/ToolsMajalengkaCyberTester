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
        print(Fore.GREEN+" [!]"+Fore.RED+" Informasi Yang Di Peroleh Dari IP "+site)
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" ip                       = "+ source["ip"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" Kota                     = " + source["city"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" Provinsi                 = "+ source["region"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" id Negara                = "+source["country"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" Negara                   = "+ source["country_name"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" Kode Negara              = "+source["country_calling_code"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" Bahasa                   = "+source["languages"])
        print (Fore.GREEN+" [!]"+Fore.YELLOW+" Organisasi/Intansi/ISP   = "+ source["org"]+ Style.RESET_ALL)
    except:
        print(Fore.RED+"Sorry Please Enter IP Address"+ Style.RESET_ALL) 