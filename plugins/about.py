#imort main
from clear_screen import clear
from colorama import Fore, Back, Style, init

init()


def about():
  clear()
  print(Fore.GREEN+"""

	   .---------       `---------.      `.-://::.``---  .----------------`    
   sddddddddd:      oddddddddd/    .+yddmmmmmdhsddd` +dddddddddddddddd:    
   :+smmdymmmd.    /mmhhmmmdo+-  `odmmmdho++oydmmmd` ommh++ymmmms++dmm:    
     -mmh.dmmmy`  .dmd.smmmd`    smmmmh-      .yddd` omms  ommmm:  hmm:    
     -mmh :mmmmo `hmm/ smmmd`   -mmmmd.        `---  /ss+  ommmm:  oss-    
     -mmh  +mmmm:smms  smmmd`   /mmmmh                     ommmm-          
     -mmh   ymmmdmmh`  smmmd`   -mmmmd.        .hs/-       ommmm-          
     .mmh   `hmmmmd.   smmmd`    smmmmh:`    `:hmmm/       ommmm-          
   :osmmdoo. -dmmm/  +ohmmmmoo-  `ommmmmdysoyhmmmd/     -oohmmmmsoo`       
   ommmmmmm:  /mms   dmmmmmmmm/    .+ydmmmmmmmdy/`      /mmmmmmmmmd`       
   .-------`   --`   ---------`      ``.-::-..`         `---------- 
	<=- Majalengka Cyber Tester -=>

    Tools ini dibuat untuk membantu mencari celah keamanan pada sebuah website yang biasa sering muncul.

    Penjelasan Menu:
                [1] BruteV1 : Tools ini digunakan untuk melakukan login dengan data yang sama dengan memanfaatkan celah keamanan Human Error (Kesalahan User).
                              Sistem kerja ini yaitu mengirimkan Paket Data ke server untuk mencari pengguna yang menggunakan password default/Bawaan Develop.
                [2] BruteV2 : Tools ini digunakan untuk melakukan login dengan ketentuan Username sudah di ketahui terlebih dahulu.
                              Sistem kerja ini yaitu mengirimkan Paket data ke server dengan cara berulang sesuai jumlah data pada wordlist password.
                [3] Directory Web Scanner : Tools ini memudahkan untuk mengecheck directory Web yang bisa di access.
                [4] Admin Finder          : Tools ini memudahkan pencarian panel admin
                [5] Bug Scanner           : Tools ini digunakan untuk melakukan pengecheckan Bug SQL Injection,XSS Injection,
                                            Directory Traversal,RFI,LFI dengan method Get dan POST. 
                [6] IP Geolocation        : Tools ini dapat menyimpulkan posisi geografis perangkat yang terhubung ke Internet.
    """+ Style.RESET_ALL)

  """menu_back = input("Kembali Kemenu : ")
  if('y' == menu_back or 'Y' == menu_back):
    main()"""