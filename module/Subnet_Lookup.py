import requests
import sys
from colorama import Fore
import os
def Subnet_Lookup():
    try:
        print(Fore.RED+"[!] Subnet Lookup Online \n")
        domain=input(Fore.RED+"WEBTESTER"+Fore.BLUE+"~"+Fore.WHITE+"/HOME"+Fore.RED+"/"+Fore.CYAN+"Web"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Subnet_Look \n # ")
        result=requests.get('https://api.hackertarget.com/subnetcalc/?q='+domain).text
        print(Fore.LIGHTBLUE_EX+result)
        try:
            input(Fore.GREEN+" [*] Back To Menu (Press Enter ...)")
        except:
            print("")
            sys.exit()
    except:
        print("\n Exit :)")
        sys.exit()

