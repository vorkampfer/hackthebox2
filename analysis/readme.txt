# HTB Analysis
# Windows
# Difficulty: Hard

### Note: This box Analysis was a-lot of fun. I learned a few things. I like using the webroot to exfiltrate a file. I recommend this box.

### Synopsis:
Analysis starts with a PHP site that uses LDAP to query a user from active directory. I’ll use LDAP injection to brute-force users, and then to read the description field of a shared account, which has the password. That grants access to the admin panel, where I’ll abuse an upload feature two ways - writing a webshell and getting execution via an HTA file. I’ll find credentials for the next user in autologon registry values and in web logs. To get administrator, I’ll abuse the Snort dynamic preprocessor feature writing a malicious DLL to where Snort will load it. ~0xdf

### Skill-set:
1. SMB Enumeration
2. Virtual Hosting
3. Subdomain Enumertion
4. Kerberos - User Brute Force Enumeration (Kerbrute)
5. Web Fuzzing
6. LDAP Injection
7. Creating a Python script to easily exploit LDAP Injection
8. Discovering valid users through the LDAP Injection
9. Enumerating user discription through LDAP injection + Information Leakage
10. Testing ASREPRoast attack (Impacket-GetNPUsers)
11. Exploitation of customized analysis panel
12. Creating a PHP webshell for command execution + Reverse Shell with Nishang
13. System enumeration with WinPeas
14. Obtaining user credentials stored in the autologon registry
15. Abusing Snort (Loading Dynamic Modules) [Privilege Escalation]
16. Creation of Malicious DLL with msfvenom for loading into snort
