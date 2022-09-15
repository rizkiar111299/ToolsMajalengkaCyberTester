from colorama import Fore, Back, Style, init

init()

class menu():
	def header():
		print(Fore.GREEN + """

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
	############################################################
    	# 	           Tools Pentester V 3.1                   #
    	#  	          Dev Rizki Alam Ramdhani                  #
    	# 	          Majalengka Cyber Tester                  #
    	# 	                 Python 3.10                       #
    	############################################################
	[1] Brute Force V1		  
	[2] Brute Force V2		  
	[3] Directory Web Scanner
	[4] Admin Finder
	[5] Bug Scanner
	[6] IP Geolocation
	[7] Subdomain Scanner
	[8] About	  
		""" + Style.RESET_ALL)