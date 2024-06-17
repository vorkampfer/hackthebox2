# HTB Wifinetic
# Linux
# Difficulty: Easy

### Synopsis:
Wifinetic is a realitively simple box, but based on some cool tech Felemos did to virtualize a wireless network. I’ll start with anonymous access to an FTP server that contains a backup file with a WPA wireless config. That config has a pre-shared key (password) in it, that also works over SSH. On the box, I’ll find a few wireless interfaces configured, and the reaver WPA WPS pin crackign tool. This tool allows me to brute force leak the pre-shared key for the wireless network, which happens to be the root password. In Beyond Root, I’ll look at the wash command, and why it doesn’t work well on this box despite being in almost all of the reaver tutorials. ~0xdf

### Skill-set:
1. FTP Enumeration
2. Information Leakage
3. SSH Brute Force with CrackMapExec
4. Abusing Capabilities - Reaver
5. Abusing an APs WPS to get the Root password [Privilege Escalation]
6. Trying to change the password and showing how the WPS pin is still giving the new password
