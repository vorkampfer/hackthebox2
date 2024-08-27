#!/bin/bash

# If you have issues running this script change the name of the script.

old_process=$(ps -eo command)
while true; do
        new_process=$(ps -eo command)
        diff <(echo "$old_process") <(echo "$new_process") | grep "[\>\<]" | grep -vE "command|procmon|kworker|defunct"
        old_process=$new_process
done
