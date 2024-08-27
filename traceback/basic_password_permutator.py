#!/usr/bin/env python3

# This is probrably the worst password permutator ever, but it can be improved upon.
# This takes a simple wordlist with NO special characters or numbers 
# and adds a couple numbers and special characters at the end.
# USAGE: ᐅ cat simple_words.txt | python3 basic_password_permutator.py
import random
from random import randint
import sys
import re

data = sys.stdin.readlines()
list = ["!",".","*",".","*","&","@","%","$","#","!","#","@"]
listb = ["-","!",".","*",".","*","&","@","%","$","#","!","#"]

for row in data:
    num = randint(1,999)
    num = str(num)
    ran = random.choice(list)
    ranb = random.choice(listb)
    row = re.sub("\n", "", row)
    new_word = row+num+ran+ranb
    print(new_word[:])