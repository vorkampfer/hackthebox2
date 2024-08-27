# HTB Soccer
# OS: Linux
# Difficulty: Easy

### Synopsis:
Soccer starts with a website that is managed over Tiny File Manager. On finding the default credentials, I’ll use that to upload a webshell and get a shell on the box. With this foothold, I’ll identify a second virtual host with a new site. That site uses websockets to do a validation task. I’ll exploit an SQL injection over the websocket to leak a password and get a shell over SSH. The user is able to run dstat as root using doas, which I’ll exploit by crafting a malicious plugin. ~0xdf
