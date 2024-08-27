# HTB Writeup
# Linux
# Difficulty: Easy

### Synopsis:
 Writeup was a great easy box. Neither of the steps were hard, but both were interesting. To get an initial shell, I’ll exploit a blind SQLI vulnerability in CMS Made Simple to get credentials, which I can use to log in with SSH. From there, I’ll abuse access to the staff group to write code to a path that’s running when someone SSHes into the box, and SSH in to trigger it. In Beyond Root, I’ll look at other ways to try to hijack the root process. ~0xdf

### Skill-set:
1. A-lot of manual enumeration
2. How to properly enumerate a framework
3. PoC to understand how the python `cms made simple` exploit worked
4. Cracking Salted hash using hashcat
5. pspy build and usage
6. Command Injection to vulnerable file. Bad permissions and $PATH placement
