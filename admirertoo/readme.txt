# HTB AdmirerToo
# OS: Linux
# Difficulty: Hard

### NOTE from Pablo: I recommend that in the Privilege Escalation portion just to scroll down to the TLDR RECAP i made. The privesc on this box had my head spinning. My notes are a rambling mess. Take care and thanks for following my guide. peace!

### Synopsis:
AdmirerToo is all about chaining exploits together. I’ll use a SSRF vulnerability in Adminer to discover a local instance of OpenTSDB, and use the SSRF to exploit a command injection to get a shell. Then I’ll exploit a command injection in Fail2Ban that requires I can control the result of a whois query about my IP. I’ll abuse a file write vulnerability in OpenCats to upload a malicious whois.conf, and then exploit fail2ban getting a shell. In Beyond Root, I’ll look at the final exploit and why nc didn’t work for me at first, but ncat did. ~0xdf

### Skill-set:
1. Subdomain Enumerations
2. Adminer Enumeration
3. SSRF (Server Side Request Forgery) in Adminer [CVE-2021-21311]
4. Abusing redirect to discover internal services
5. OpenTSDB Exploitation [CVE-2020-35476] [Remote Code Execution]
6. Searching for valid metrics
7. OpenCats PHP Object Injection to Arbitrary File Write
8. Abusing Fail2ban [RCE][CVE-2021-32749]
9. PLaying with phpggc in order to serialize our data
10. Abusing whois config file + OpenCats + Fail2ban [PrivESC]
