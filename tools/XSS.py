import os
import requests
import datetime
from progress.bar import Bar
import urllib3

def xssinjection():   
    print("##########################################")
    print("Check Bug Xss Injection")
    print("##########################################")
    link = str(input("Masukan Link Target : "))
    with open('././wordlist/Xss_Injection.txt','r',encoding = "utf8") as py:
        payload_Sql = py.readlines()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        }
    bar = Bar('Progress Scanner Sedang Berjalan', max=6606 )
    for b in range(0,len(payload_Sql)):
        pay = payload_Sql[b].rstrip('\n')
        bar.next()
        try:
            urllib3.disable_warnings()
            req2 = requests.get(link+pay, headers = headers, timeout=150,verify=False)
            if 'menyatakan' in str(req2.content):
                print("\n\n################### Link Vuln Xss Injection ###################")
                print("Xss Injection Vuln!!! ".format(req2.url))
                print("Payload Code : {}".format(pay))
                print("Status Code : {}".format(req2.status_code))
                print("###############################################################")
                break
            elif req2.status_code == 500:
                print("\n\n################### Link Vuln Xss Injection ###################")
                print("Xss Injection Vuln!!! ".format(req2.url))
                print("Payload Code : {}".format(pay))
                print("Status Code : {}".format(req2.status_code))
                print("###############################################################")
                break
        except requests.exceptions.RequestException as e:
                print(e)
    print("Scanner Selesai")
    bar.finish()