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
        bar = Bar(Fore.YELLOW +'Progress Scanner SQL Injection Sedang Berjalan'+ Style.RESET_ALL, max=1533 )
        for b in range(0,len(payload_Sql)):
            pay = payload_Sql[b].rstrip('\n')
            bar.next()
            try:
                urllib3.disable_warnings()
                req2 = requests.get(link+pay, headers = headers, timeout=150,verify=False)
                if 'SQL' in str(req2.content) or 'sql' in str(req2.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"SQL Vuln        : {}".format(Style.RESET_ALL+req2.url))
                    print(Fore.YELLOW +"Payload Code    : {}".format(Style.RESET_ALL+pay))
                    print(Fore.YELLOW +"Status Code     : {}".format(Style.RESET_ALL+str(req2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif 'error' in str(req2.content) or 'ERROR' in str(req2.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"SQL Vuln        : {}".format(Style.RESET_ALL+req2.url))
                    print(Fore.YELLOW +"Payload Code    : {}".format(Style.RESET_ALL+pay))
                    print(Fore.YELLOW +"Status Code     : {}".format(Style.RESET_ALL+str(req2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif req2.status_code == 500:
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"SQL Vuln        : {}".format(Style.RESET_ALL+req2.url))
                    print(Fore.YELLOW +"Payload Code    : {}".format(Style.RESET_ALL+pay))
                    print(Fore.YELLOW +"Status Code     : {}".format(Style.RESET_ALL+str(req2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
            except requests.exceptions.RequestException as e:
                print(e)
        bar.finish()
        print("Scanner SQL Injection Selesai")
        print("")
        with open('././wordlist/Xss_Injection.txt','r',encoding = "utf8") as xss:
            xsspay = xss.readlines()
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        bar = Bar(Fore.YELLOW +'Progress Scanner XSS Injetion Sedang Berjalan'+ Style.RESET_ALL, max=6606 )
        for i in range(0,len(xsspay)):
            try:
                urllib3.disable_warnings()
                payxss = xsspay[i].rstrip('\n')
                bar.next()
                url = requests.get(link+payxss,verify = False, headers = headers, timeout = 150)
                if 'menyatakan' in str(url.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln Xss Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"Xss Vuln     : {}".format(Style.RESET_ALL+url.url))
                    print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+payxss))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(url.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif url.status_code == 302:
                    print(Fore.YELLOW +"\n\n################### Link Vuln Xss Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"Xss Vuln     : {}".format(Style.RESET_ALL+url.url))
                    print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+payxss))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(url.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
            except requests.exceptions.RequestException as e:
                print(e)
        bar.finish()
        print("Scanner Selesai")
    elif Temp_Method == 2:
        link = str(input(Fore.YELLOW +"Masukan Link Target : "+ Style.RESET_ALL))
        parameter = str(input(Fore.YELLOW +"Masukan Parameter : "+ Style.RESET_ALL))
        with open('././wordlist/Sql_Injection.txt','r') as py:
            payload_Sql = py.readlines()
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        bar = Bar(Fore.YELLOW +'Progress Scanner Sedang Berjalan'+ Style.RESET_ALL, max=1284 )
        for b in range(0,len(payload_Sql)):
            pay = payload_Sql[b].rstrip('\n')
            bar.next()
            data_dict = {parameter:pay }
            try:
                urllib3.disable_warnings()
                req2 = requests.post(link,data = data_dict, headers = headers, timeout=150, verify=False, allow_redirects=True)
                if 'Username Belum Terdaftar' in str(req2.content) or 'Username Belum Terdaftar!' in str(req2.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"Link         : {}".format(Style.RESET_ALL+link))
                    print(Fore.YELLOW +"Parameter    : {}".format(Style.RESET_ALL+parameter))
                    print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+pay))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(req2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif 'SQL' in str(req2.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"Link         : {}".format(Style.RESET_ALL+link))
                    print(Fore.YELLOW +"Parameter    : {}".format(Style.RESET_ALL+parameter))
                    print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+pay))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(req2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif 'error' in str(req2.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"Link         : {}".format(Style.RESET_ALL+link))
                    print(Fore.YELLOW +"Parameter    : {}".format(Style.RESET_ALL+parameter))
                    print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+pay))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(req2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif req2.status_code == 500:
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"Link         : {}".format(Style.RESET_ALL+link))
                    print(Fore.YELLOW +"Parameter    : {}".format(Style.RESET_ALL+parameter))
                    print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+pay))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(req2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
            except requests.exceptions.RequestException as e:
                print(e)
        bar.finish()
        print("Scanner Selesai")
        # print("")
        # with open('././wordlist/Xss_Injection.txt','r',encoding = "utf8") as xss:
        #     xsspay = xss.readlines()
        # headers = {
        #         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        #     }
        # bar = Bar(Fore.YELLOW +'Progress Scanner XSS Injetion Sedang Berjalan'+ Style.RESET_ALL, max=6606 )
        # for i in range(0,len(xsspay)):
        #     try:
        #         bar.next()
        #         urllib3.disable_warnings()
        #         payxss = xsspay[i].rstrip('\n')
        #         data_dict = {parameter:payxss }
        #         url = requests.post(link,verify = False, headers = headers, timeout = 150,data = data_dict,allow_redirects=True)
        #         if 'menyatakan' in str(url.content):
        #             print(Fore.YELLOW +"\n\n################### Link Vuln Xss Injection ###################"+ Style.RESET_ALL)
        #             print(Fore.YELLOW +"Xss Vuln     : {}".format(Style.RESET_ALL+url.url))
        #             print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+payxss))
        #             print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(url.status_code)))
        #             print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
        #             break
        #         elif url.status_code == 302:
        #             print(Fore.YELLOW +"\n\n################### Link Vuln Xss Injection ###################"+ Style.RESET_ALL)
        #             print(Fore.YELLOW +"Xss Vuln     : {}".format(Style.RESET_ALL+url.url))
        #             print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+payxss))
        #             print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(url.status_code)))
        #             print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
        #             break
        #     except requests.exceptions.RequestException as e:
        #         print(e)
        #     bar.finish()
        #     print("Scanner Selesai")