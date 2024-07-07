#!/usr/bin/env bash

# This script was created originally by S4vitar for the box HTB Enterprise
# Updated by me (Pablo Honey)
# 04-05-24

# Colors
GREEN="\e[0;32m\033[1m"
NOCOLOR="\033[0m\e[0m"
RED="\e[0;31m\033[1m"
BLUE="\e[0;34m\033[1m"
YELLOW="\e[0;33m\033[1m"
PURPLE="\e[0;35m\033[1m"
CYAN="\e[0;36m\033[1m"
WHITE="\e[0;37m\033[1m"

function ctrl_c(){
    echo -e "\n\n${RED}[+] Exiting host discovery script...${NOCOLOR}\n"
    tput cnorm; exit 1
}

# Ctrl+C
trap ctrl_c SIGINT

tput civis

for i in $(seq 1 254); do
	timeout 1 bash -c "ping -c 1 172.17.0.$i" &>/dev/null && echo "[+] HOST 172.17.0.$i is active" &
done; wait

tput cnorm



