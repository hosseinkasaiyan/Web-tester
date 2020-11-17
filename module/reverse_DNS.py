import requests
import sys
from colorama import Fore
import os
def reversedns():
    try:
        print(Fore.RED+"[!] IP addresses or a domain name\n")
        domain=input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"Web-Tester"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Reverse_Dns \n # ")
        result=requests.get('https://api.hackertarget.com/reversedns/?q='+domain).text
        print(Fore.LIGHTBLUE_EX+result)
        try:
            input(Fore.GREEN+" [*] Back To Menu (Press Enter ...)")
        except:
            print("")
            sys.exit()
    except:
        print("\n Exit :)")
        sys.exit()

