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
    	# 	           Tools Pentester V 3.2                   #
    	#  	          Dev Rizki Alam Ramdhani                  #
    	# 	          Majalengka Cyber Tester                  #
    	# 	                 Python 3.10                       #
    	############################################################
	[1] Brute Force V1		  
	[2] Brute Force V2		  
	[3] Directory Web Scanner
	[4] Admin Finder
	[5] Directory Traversal Checker
	[6] Sql Injection Checker
	[7] XSS Injection Checker
	[8] IP Geolocation
	[9] Subdomain Scanner
	[10] About	  
		""" + Style.RESET_ALL) 