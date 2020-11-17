import sys
import socket
import os
import time
from subprocess import Popen
from help import help
from module import cloudflare,cms,Dns_Servers,dnslookup,ip_location,panel_admin,reverse_DNS,robot,Subnet_Lookup,Tcp_Port_Scan,Transfer,wordpress


#R
try:
    from colorama import Fore
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install colorama\n
    pip3 install colorama
        """)



try:
    import requests
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install requests\n
    pip3 install requests
        """)
try:
    from subprocess import Popen
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install Popen\n
    pip3 install Popen 
        """)



try:
    import ipapi
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install ipapi\n
    pip3 install ipapi
        """)




try:
    import builtwith
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install builtwith\n
    pip3 install builtwith
        """)


while True:
    

    try:
        help.Banner()
        help.infolist1()
        number = input(Fore.RED+"WEBTESTER"+Fore.BLUE+"~"+Fore.WHITE+"/HOME"+Fore.WHITE+"""
""").lower()
    except:
        print("\n God Lock ... ")
        sys.exit()
    if number == '3':

        print()
        sys.exit()
            
        
       

    elif number == "2":
        help.infolist3()

        

    elif number == "":
        print(Fore.RED+" [!]"+Fore.BLUE+" Please Enter Number :))))")
        input("")



    elif number == '1':
        try:
            help.Banner()
            help.infolist2()
            infor = input(Fore.RED+"WEBTESTER"+Fore.BLUE+"~"+Fore.WHITE+"/HOME"+Fore.WHITE+"""
""").lower()
    
            if infor == "1":
                help.Banner()
                cloudflare.__start__()

                

            elif infor == "2":
                help.Banner()
                cms.__start__()

               


            elif infor == "3":
                help.Banner()
                Dns_Servers.Dns_server()

            


            elif infor == "4":
                help.Banner()
                dnslookup.dnslookup()

                

            elif infor == "5":
                help.Banner()
                ip_location.__start__()

               
            
            elif infor == "6":
                help.Banner()
                panel_admin.__start__()

                

            elif infor == "7":
                help.Banner()
                reverse_DNS.reversedns()

                #####################

            elif infor == "8":
                help.Banner()
                robot.__start__()

                #####################

            elif infor == "9":
                help.Banner()
                Subnet_Lookup.Subnet_Lookup()   

                #####################

            elif infor == "10":
                help.Banner()
                Tcp_Port_Scan.Tcp_scan()  
                #####################

            elif infor == "11":
                help.Banner()
                Transfer.Transfer()
                #####################

            elif infor == "12":
                help.Banner()
                wordpress.wpplug()

                #####################

            elif infor == "13":
                input(Fore.RED+" [!]"+Fore.GREEN+" Back To Menu (Press Enter...) ")

                #####################
            elif infor == "14":
                sys.exit()
                
                #####################
            elif infor == "":
                input(Fore.RED+" [!]"+Fore.GREEN+" Please Enter Number (Press Enter...) ")
        except KeyboardInterrupt:
            print("")
            sys.exit()

#------------------------------------------------------------------------------------------------
   


