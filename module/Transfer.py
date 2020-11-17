import requests
import sys
from colorama import Fore
import os
def Transfer():
    try:
        print(Fore.RED+"[!] Online Test of a zone transfer that will attempt to get all DNS records for a target domain. The zone transfer will be tested against all name servers (NS) for a domain.\n")
        domain=input(Fore.RED+"WEBTESTER"+Fore.BLUE+"~"+Fore.WHITE+"/HOME"+Fore.RED+"/"+Fore.CYAN+"Web"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Transfer \n # ")
        result=requests.get('https://api.hackertarget.com/zonetransfer/?q='+domain).text
        print(Fore.LIGHTBLUE_EX+result)
        try:
            input(Fore.GREEN+" [*] Back To Menu (Press Enter ...)")
        except:
            print("")
            sys.exit()
    except:
        print("\n Exit :)")
        sys.exit()

