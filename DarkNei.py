# darknei domain finder... for educational purposes only
# admin - gospel chukwunonso
# facebook - gospel chukwunonso

# import necessary packages
import termcolor
from colorama import Fore, Back
import os
from googlesearch import search
from cfonts import render                                     
# clear screen output
if os.name == 'posix':
   os.system('clear')
elif os.name == 'nt':
   os.system('cls')                                                                                                         # title
print('\n')
print(Fore.RED+'DARKNEI - LINKS SCRAPER TOOLKIT'.center(66)+Fore.WHITE)
print(Fore.YELLOW+'admin - gospel chukwunonso'.center(66)+Fore.WHITE)
print(Fore.GREEN+'for educational purposes only'.center(66)+Fore.WHITE)

# darknei logo
output = render('DARKNEI', colors=['red', 'yellow'], align='center')
print(output)

# main
srch = input(Fore.YELLOW+'[*] Search Anything [image-username-domain-ipaddress] >> '+Fore.WHITE)
print(Fore.GREEN+'[*] Fetching Links Associated With {}\n'.format(srch)+Fore.WHITE)
print('[CTRL + C] To Terminate\n')
# start scrape
try:
    for url in search(srch):
        print(Fore.YELLOW+url+Fore.WHITE)
except:
    print(Fore.RED+'DarkNei Terminated...'.format(srch)+Fore.WHITE)