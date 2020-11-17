import requests
import sys
from colorama import Fore
import os
def Dns_server():
    try:
        print(Fore.RED+"[!] Find hosts sharing DNS servers. Discovering additional domains and host names from a shared DNS server search enables a security analyst to link related systems. Finding all related and accessible systems is the only way to truly assess the security of an organization. \n")
        domain=input(Fore.RED+"WEBTESTER"+Fore.BLUE+"~"+Fore.WHITE+"/HOME"+Fore.RED+"/"+Fore.CYAN+"Web"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Dns_Servers \n # ")
        result=requests.get('https://api.hackertarget.com/findshareddns/?q='+domain).text
        print(Fore.LIGHTBLUE_EX+result)
        try:
            input(Fore.GREEN+" [*] Back To Menu (Press Enter ...)")
        except:
            print("")
            sys.exit()
    except:
        print("\n Exit :)")
        sys.exit()
        
