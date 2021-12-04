import requests
import os
import sys
from colorama import Fore, Back, Style
import colorama
import time

banner = """
[!] WELCOME TO SUBDOMAIN TAKEOVER TESTER TOOL [!]

Coded by Xale
GitHub: @xaletr

"""
print(Fore.GREEN + banner)

if sys.argv[1] in ['-u', '--url']:
 url = sys.argv[2]
 resp = requests.get(url)
 #payloads
 spayload = '<div id="shop-not-found">'
 hpayload = '<iframe src="//www.herokucdn.com/error-pages/no-such-app.html"></iframe>'
 apayload = '<li>Message: The specified bucket does not exist</li>'
#shopify

 print(Fore.BLUE)
 print("Testing : Shopify Subdomain Takeover")
 time.sleep(3)
if spayload in resp.text:
 print(Fore.GREEN + "[FOUND]" + Fore.BLUE + " Vulnerable Found!")
else:
 print(Fore.RED + "[NOT FOUND]" + Fore.BLUE + " Vulnerable Found!")

#heroku
print("Testing : Heroku Subdomain Takeover")
time.sleep(3)
if hpayload in resp.text:
 print(Fore.GREEN + "[FOUND]" + Fore.BLUE + " Vulnerable Found!")
else:
 print(Fore.RED + "[NOT FOUND]" + Fore.BLUE + " Vulnerable Found!")

#aws
print("Testing : Amazon AWS Subdomain Takeover")
time.sleep(3)
if apayload in resp.text:
 print(Fore.GREEN + "[FOUND]" + Fore.BLUE + " Vulnerable Found!")
else:
 print(Fore.RED + "[NOT FOUND]" + Fore.BLUE + " Vulnerable Found!")
 
