import requests
import sys
from colorama import Fore
import os
def Tcp_scan():
    try:
        print(Fore.RED+"[!] BEGIN TCP PORT SCAN \n")
        domain=input(Fore.RED+"WEBTESTER"+Fore.BLUE+"~"+Fore.WHITE+"/HOME"+Fore.RED+"/"+Fore.CYAN+"Web"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Tcp-Port_Scan \n # ")
        result=requests.get('https://api.hackertarget.com/nmap/?q='+domain).text
        print(Fore.LIGHTBLUE_EX+result)
        try:
            input(Fore.GREEN+" [*] Back To Menu (Press Enter ...)")
        except:
            print("")
            sys.exit()
    except:
        print("\n Exit :)")
        sys.exit()

