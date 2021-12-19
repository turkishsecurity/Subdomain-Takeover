import urllib.request
import os 
import requests
import sys
import time
import colorama
from colorama import Back, Fore, Style

if sys.argv[1] in ['-t', '--targets', '-T']:
 filename = sys.argv[2]
 time.sleep(3)
 print("-----------------------------")
 print("SUBDOMAIN TAKEOVER TESTER ")
 print("CODED BY XALE ~ @xaletr")
 print("-----------------------------")
file = open(filename, "r")
lines = file.readlines()


for site in lines:
  st = "http://"+site
  try:
   req = requests.get(st)
    #payloads
   spayload = '<div id="shop-not-found">'
   hpayload = '<iframe src="//www.herokucdn.com/error-pages/no-such-app.html"></iframe>'
   apayload = '<li>Message: The specified bucket does not exist</li>'
   if spayload in req.text:
    print(Fore.GREEN + "[!] BASARILI : "+req.url+" [SHOPIFY]")
   elif hpayload in req.text:
    print(Fore.GREEN + "[!] BASARILI : "+req.url+Fore.PURPLE+" [HEROKU]")
   elif apayload in req.text:
    print(Fore.GREEN + "[!] BASARILI : "+req.url+Fore.RED+" [AWS]")
   else:
    print("[!] HATA "+st)
  except:
   print("[!] HATA "+st)
