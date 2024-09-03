# HTB Bank
# OS: Linux
# Difficulty: Easy

### Synopsis:
Bank was an pretty straight forward box, though two of the major steps had unintended alternative methods. I’ll enumerate DNS to find a hostname, and use that to access a bank website. I can either find creds in a directory of data, or bypass creds all together by looking at the data in the HTTP 302 redirects. From there, I’ll upload a PHP webshell, bypassing filters, and get a shell. To get root, I can find a backdoor SUID copy of dash left by the administrator, or exploit write privileges in /etc/passwd. In Beyond Root, I’ll look at the coding mistake in the 302 redirects, and show how I determined the SUID binary was dash. ~0xdf

### Skill-set:
1. Domain Zone Transfer Attack - AXFR(dig)
2. Information Leakage
3. Abusing File Upload [RCE]
4. Abusing SUID Binary (WTF?)[Privilege Escalation]
