#WELCOME TO GH SUBDOMAIN FINDER
#THIS IS SO SIMPLE PROGRAM THAT YOU CAN FIND WEBSITES SUBDOMAINS
#USAGE: JUST ENTER THE DOMAIN. FOR EXAMPLE greekhacking.gr
#CAREFUL: WITHOUT "www."
#CREATED BY <============================ MATA | https:www.greekhacking.gr ============================>

#imports

import requests
import pyfiglet
import colorama
import time
import sys
from colorama import *
colorama.init()

#logo 

print(Fore.LIGHTBLUE_EX + "")
logo = pyfiglet.figlet_format("GH Subdomain Finder  v2")
print(logo)
print("-" * 100)
print("                                           WELCOME TO GH SUBDOMAIN FINDER V2")
print("")
print("                 <============== CREATED BY MATA | https://www.greekhacking.gr | ==============>")
print("")
print("                 <============== The method that checks whether the site uses a wildcard was developed by PiRaTaS. ==============>")
print("-" * 100)
print(Fore.RESET + "")

print("")
print("")
print("")
print(Fore.YELLOW + "")
domain = input("    Enter Domain here (e.x greekhacking.gr):   ")
print(Fore.RESET + "")
print("")
print("")
print("")
print("")
print(Fore.RED + "                      <================================= Please wait... =================================>" + Fore.RESET)
time.sleep(4)
print("")
print("")
print("")


basic_file = open('basic.txt', 'r')
basic_content = basic_file.read()
basic_subdomains = basic_content.splitlines()

found_subdomains = []

print(Fore.CYAN + "[INFO] Checking subdomains from basic.txt... If subdomains are found, it means that the site uses the wildcard subdomain method, making it impossible to perform an objective scan.\n" + Fore.RESET)

for subdomain in basic_subdomains:
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    try:
        requests.get(url1)
        print(Fore.GREEN + "    Found Subdomain " + Fore.RED + " =====>  " + Fore.WHITE + str(url1))
        found_subdomains.append(subdomain)
        requests.get(url2)
        print(Fore.GREEN + "    Found Subdomain " + Fore.RED + " =====>  " + Fore.WHITE + str(url2) + Fore.RESET)
    except requests.ConnectionError:
        pass
    except KeyboardInterrupt:
        print("Exiting.......")
        time.sleep(1)
        sys.exit()


if set(found_subdomains) == set(basic_subdomains):
    print(Fore.GREEN + "\n[INFO] All subdomains in basic.txt found. This site accepts even incorrect subdomains, indicating that it uses a wildcard subdomain method." + Fore.RESET)
    print(Fore.YELLOW + "\n[INFO] No further scanning can be performed as the site accepts incorrect subdomains." + Fore.RESET)
    sys.exit()


print(Fore.YELLOW + "\n[INFO] Not all subdomains in basic.txt were found. Proceeding with wordlist.txt...\n" + Fore.RESET)

file = open('wordlist.txt', 'r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
    url1 = f"http://{subdomain}.{domain}"
    url2 = f"https://{subdomain}.{domain}"
    try:
        requests.get(url1)
        print(Fore.GREEN + "    Possible Subdomain " + Fore.RED + " =====>  " + Fore.WHITE + str(url1))
        requests.get(url2)
        print(Fore.GREEN + "    Possible Subdomain " + Fore.RED + " =====>  " + Fore.WHITE + str(url2) + Fore.RESET)

    except requests.ConnectionError:
        pass
    except KeyboardInterrupt:
        print("Exiting.......")
        time.sleep(1)
        sys.exit()
