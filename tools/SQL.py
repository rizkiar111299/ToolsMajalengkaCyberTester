import os
import requests
import datetime
from progress.bar import Bar
import urllib3
from colorama import Fore, Back, Style, init

init()


def SqlInjection():
    print(Fore.YELLOW + "##########################################")
    print("Check Bug SQL Injection")
    print("##########################################"+ Style.RESET_ALL)
    Temp_Method = int(input(Fore.YELLOW + "Pilih Method [1] Get or [2] Post : "+ Style.RESET_ALL))
    if Temp_Method == 1:
        link = str(input(Fore.YELLOW + "Masukan Link Target : "+ Style.RESET_ALL))
        with open('././wordlist/Sql_Injection.txt','r') as py:
            payload_Sql = py.readlines()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        bar = Bar('Progress Scanner Sedang Berjalan', max=1533 )
        for b in range(0,len(payload_Sql)):
            pay = payload_Sql[b].rstrip('\n')
            bar.next()
            try:
                urllib3.disable_warnings()
                req2 = requests.get(link+pay, headers = headers, timeout=150,verify=False)
                if 'SQL' in str(req2.content) or 'sql' in str(req2.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################")
                    print(Fore.YELLOW +"Link         : {}".format(req2.url))
                    print(Fore.YELLOW +"Payload Code : {}".format(pay))
                    print(Fore.YELLOW +"Status Code  : {}".format(req2.status_code))
                    print(Fore.YELLOW +"###############################################################")
                    break
                elif 'error' in str(req2.content) or 'ERROR' in str(req2.content):
                    print("\n\n################### Link Vuln SQL Injection ###################")
                    print("Link         : {}".format(req2.url))
                    print("Payload Code : {}".format(pay))
                    print("Status Code  : {}".format(req2.status_code))
                    print("###############################################################")
                    break
                elif req2.status_code == 500:
                    print("\n\n################### Link Vuln SQL Injection ###################")
                    print("Link         : {}".format(req2.url))
                    print("Payload Code : {}".format(pay))
                    print("Status Code  : {}".format(req2.status_code))
                    print("###############################################################")
                    break
            except requests.exceptions.RequestException as e:
                print(e)
        bar.finish()
        print("Scanner Selesai")
    elif Temp_Method == 2:
        link = str(input("Masukan Link Target : "))
        parameter = str(input("Masukan Parameter : "))
        with open('././wordlist/Sql_Injection.txt','r') as py:
            payload_Sql = py.readlines()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        bar = Bar('Progress Scanner Sedang Berjalan', max=1284 )
        for b in range(0,len(payload_Sql)):
            pay = payload_Sql[b].rstrip('\n')
            bar.next()
            data_dict = {parameter:pay }
            try:
                urllib3.disable_warnings()
                req2 = requests.post(link,data = data_dict, headers = headers, timeout=150, verify=False, allow_redirects=True)
                if 'Username Belum Terdaftar' in str(req2.content) or 'Username Belum Terdaftar!' in str(req2.content):
                    print("\n\n################### Link Vuln SQL Injection ###################")
                    print("Link         : {}".format(link))
                    print("Parameter    : {}".format(parameter))
                    print("Payload Code : {}".format(pay))
                    print("Status Code  : {}".format(req2.status_code))
                    print("###############################################################")
                    break
                elif 'SQL' in str(req2.content):
                    print("\n\n################### Link Vuln SQL Injection ###################")
                    print("Link         : {}".format(link))
                    print("Parameter    : {}".format(parameter))
                    print("Payload Code : {}".format(pay))
                    print("Status Code  : {}".format(req2.status_code))
                    print("###############################################################")
                    break
                elif 'error' in str(req2.content):
                    print("\n\n################### Link Vuln SQL Injection ###################")
                    print("Link         : {}".format(link))
                    print("Parameter    : {}".format(parameter))
                    print("Payload Code : {}".format(pay))
                    print("Status Code  : {}".format(req2.status_code))
                    print("###############################################################")
                    break
                elif req2.status_code == 500:
                    print("\n\n################### Link Vuln SQL Injection ###################")
                    print("Link         : {}".format(link))
                    print("Parameter    : {}".format(parameter))
                    print("Payload Code : {}".format(pay))
                    print("Status Code  : {}".format(req2.status_code))
                    print("###############################################################")
                    break
            except requests.exceptions.RequestException as e:
                print(e)
        bar.finish()
        print("Scanner Selesai")
        print("")