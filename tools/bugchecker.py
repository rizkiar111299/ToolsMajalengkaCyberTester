import os
import requests, builtwith
import datetime
from progress.bar import Bar
import urllib3
from colorama import Fore, Back, Style, init
init()

def BugChecker():
    print(Fore.YELLOW + "##########################################")
    print("Bug Scanner")
    print("##########################################"+ Style.RESET_ALL)
    print("")
    Temp_Method = int(input(Fore.YELLOW + "Pilih Method [1] Get or [2] Post : "+ Style.RESET_ALL))
    if Temp_Method == 1:
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

        #Scanner SQL Injection Start
        with open('././wordlist/Sql_Injection.txt','r') as py:
            payload_Sql = py.readlines()
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        bar = Bar(Fore.YELLOW +'Progress Scanner SQL Injection Sedang Berjalan'+ Style.RESET_ALL, max=1284 )
        for b in range(0,len(payload_Sql)):
            try:
                pay = payload_Sql[b].rstrip('\n')
                bar.next()
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
        #Scanner SQL Injection End

        #Scanner XSS Injection Start
        with open('././wordlist/Xss_Injection.txt','r',encoding = "utf8") as xss:
            xsspay = xss.readlines()
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        bar = Bar(Fore.YELLOW +'Progress Scanner XSS Injetion Sedang Berjalan'+ Style.RESET_ALL, max=6608 )
        for i in range(0,len(xsspay)):
            try:
                urllib3.disable_warnings()
                payxss = xsspay[i].rstrip('\n')
                bar.next()
                url = requests.get(link+payxss,verify = False, headers = headers, timeout = 150 ,allow_redirects=True)
                if 'menyatakan' in str(url.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln XSS Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"Xss Vuln     : {}".format(Style.RESET_ALL+url.url))
                    print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+payxss))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(url.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif url.status_code == 301 or url.status_code == 302 or url.status_code == 303 or url.status_code == 304 or url.status_code == 305 or url.status_code == 306 or url.status_code == 307 or url.status_code == 308:
                    print(Fore.YELLOW +"\n\n################### Link Vuln XSS Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"Xss Vuln     : {}".format(Style.RESET_ALL+url.url))
                    print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+payxss))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(url.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif url.status_code == 500:
                    print(Fore.YELLOW +"\n\n################### Link Vuln XSS Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"Xss Vuln     : {}".format(Style.RESET_ALL+url.url))
                    print(Fore.YELLOW +"Payload Code : {}".format(Style.RESET_ALL+payxss))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(url.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
            except requests.exceptions.RequestException as e:
                print(e)
        bar.finish()
        print("Scanner XSS Injection Selesai")
        #Scanner XSS Injection End

        #Scanner Directory traversal
        with open('././wordlist/directorytraversal.txt','r') as py:
            wordlist_dTraversal = py.readlines()

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
        bar = Bar(Fore.YELLOW +'Progress Scanner Directory Traversal Sedang Berjalan'+ Style.RESET_ALL, max=1534 )
        for b in range(0,len(wordlist_dTraversal)):
            pay = wordlist_dTraversal[b].rstrip('\n')
            bar.next()
            try:
                req3 = requests.get(link+pay, headers = headers, timeout=10,verify=False)
                if 'root:x:0:0:root:/root:/bin/bash' in str(req3.content):
                    print(Fore.YELLOW +"######################### Link Vuln Bug Directory Traversal #########################"+Style.RESET_ALL)
                    print("Link {} : {} Vuln!".format(req3.url,Style.RESET_ALL,req3.status_code))
                    print("#####################################################################################"+Style.RESET_ALL)
                    break
                elif req3.status_code == 500:
                    print(Fore.YELLOW +"######################### Link Vuln Bug Directory Traversal #########################" +Style.RESET_ALL )
                    print(Fore.YELLOW +"Link {} : {} Vuln! \n".format(req3.url,Style.RESET_ALL,req3.status_code))
                    print(Fore.YELLOW +"#####################################################################################" +Style.RESET_ALL)
                    break
            except requests.exceptions.RequestException as e:
                print(e)
        bar.finish()
        print("Scanner Directory Traversal Selesai")
        #Scanner Directory Traversal End

        #Scanner RFI Start
        with open('././wordlist/RFI.txt','r',encoding = "utf8") as RFI:
            RFIpay = RFI.readlines()
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        bar = Bar(Fore.YELLOW +'Progress Scanner RFI Sedang Berjalan'+ Style.RESET_ALL, max=3 )
        for i in range(0,len(RFIpay)):
            try:
                urllib3.disable_warnings()
                payRFI = RFIpay[i].rstrip('\n')
                bar.next()
                url2 = requests.get(link+payRFI,verify = False, headers = headers, timeout = 150 ,allow_redirects=True)
                if url2.status_code == 200:
                    print(Fore.YELLOW +"\n\n################### Link Vuln RFI ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"RFI Vuln     : {}".format(Style.RESET_ALL+url2.url))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(url2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
            except requests.exceptions.RequestException as e:
                print(e)
        bar.finish()
        print("Scanner Remote File Inclusion Selesai")
        #Scanner RFI End

        #Scanner LFI Start
        with open('././wordlist/LFI.txt','r',encoding = "utf8") as a:
            apay = a.readlines()
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        bar = Bar(Fore.YELLOW +'Progress Scanner RFI Sedang Berjalan'+ Style.RESET_ALL, max=70466 )
        for i in range(0,len(apay)):
            try:
                urllib3.disable_warnings()
                paya = apay[i].rstrip('\n')
                bar.next()
                url3 = requests.get(link+paya,verify = False, headers = headers, timeout = 150 ,allow_redirects=False)
                if url3.status_code == 500:
                    print(Fore.YELLOW +"\n\n################### Link Vuln LFI ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"LFI Vuln     : {}".format(Style.RESET_ALL+url3.url))
                    print(Fore.YELLOW +"Status Code  : {}".format(Style.RESET_ALL+str(url3.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
            except requests.exceptions.RequestException as e:
                print(e)
        bar.finish()
        print("Scanner Local File Inclusion Selesai")
        #Scanner LFI End        

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
                if 'SQL' in str(req2.content) or 'sql' in str(req2.content) or 'Database' in str(req2.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"SQL Vuln        : {}".format(Style.RESET_ALL+req2.url))
                    print(Fore.YELLOW +"Payload Code    : {}".format(Style.RESET_ALL+pay))
                    print(Fore.YELLOW +"Status Code     : {}".format(Style.RESET_ALL+str(req2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif 'error' in str(req2.content) or 'Error' in str(req2.content):
                    print(Fore.YELLOW +"\n\n################### Link Vuln SQL Injection ###################"+ Style.RESET_ALL)
                    print(Fore.YELLOW +"SQL Vuln        : {}".format(Style.RESET_ALL+req2.url))
                    print(Fore.YELLOW +"Payload Code    : {}".format(Style.RESET_ALL+pay))
                    print(Fore.YELLOW +"Status Code     : {}".format(Style.RESET_ALL+str(req2.status_code)))
                    print(Fore.YELLOW +"###############################################################"+ Style.RESET_ALL)
                    break
                elif int(req2.status_code) == 500:
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
        print("")
        with open('././wordlist/Xss_Injection.txt','r',encoding = "utf8") as xss:
            xsspay = xss.readlines()
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }
        bar = Bar(Fore.YELLOW +'Progress Scanner XSS Injetion Sedang Berjalan'+ Style.RESET_ALL, max=6606 )
        for i in range(0,len(xsspay)):
            try:
                bar.next()
                urllib3.disable_warnings()
                payxss = xsspay[i].rstrip('\n')
                data_dict = {parameter:payxss }
                url = requests.post(link,verify = False, headers = headers, timeout = 150,data = data_dict,allow_redirects=True)
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