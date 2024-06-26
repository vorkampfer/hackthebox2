#!/bin/bash

function ctrl_c(){
    echo -e "\n\n${redColour}[+] Exiting procmon.sh script${endColour}\n"
    exit 1
}

# Ctrl+C
trap ctrl_c SIGINT

old_process=$(ps -eo user,command)

while true; do
        new_process=$(ps -eo user,command)
        diff <(echo "$old_process") <(echo "$new_process") | grep "[\>\<]" | grep -vE "command|diff|procmon|kworker"
        old_process=$new_process
done
