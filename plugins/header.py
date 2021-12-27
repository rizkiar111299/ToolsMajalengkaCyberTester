from colorama import Fore, Back, Style, init

init()

class menu():
	def header():
		print(Fore.GREEN + """
	############################################################
    	# 	           Tools Pentester V 1.1                   #
    	#  	          Dev Rizki Alam Ramdhani                  #
    	# 	          Majalengka Cyber Tester                  #
    	# 	                 Python 3.9                        #
    	############################################################
	[1] Brute Force V1		  [5] Admin Finder
	[2] Brute Force V2		  [6] XSS Injection Checker
	[3] Directory Web Scanner 	  [7] SQL Injection Checker
	[4] Directory Traversal Checker		  
		""" + Style.RESET_ALL)