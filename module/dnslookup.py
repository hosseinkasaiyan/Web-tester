import requests
import sys
from colorama import Fore
import os
def dnslookup():
    try:
        print(Fore.RED+"[!] Enter The Domain\n")
        domain=input(Fore.RED+"WEBTESTER"+Fore.BLUE+"~"+Fore.WHITE+"/HOME"+Fore.RED+"/"+Fore.CYAN+"Web"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Dnslookup \n # ")
        result=requests.get('https://api.hackertarget.com/dnslookup/?q='+domain).text
        print(Fore.LIGHTBLUE_EX+result)
        try:
            input(Fore.GREEN+" [*] Back To Menu (Press Enter ...)")
        except:
            print("")
            sys.exit()
    except:
        print("\n Exit :)")
        sys.exit()

