# HTB Europa
# Linux
# Difficulty: Medium

### Note: This was a really great box for practicing SQL querries as well as some python scripting. I really recommend this box. I have included different versions of the same script exploit for learning purposes. Enjoy!

### Synopsis:
Europa was a relatively easy box by today’s HTB standards, but it offers a good chance to play with the most basic of SQL injections, the auth bypass. I’ll also use sqlmap to dump the database. The foothold involves exploiting the PHP preg_replace function, which is something you’ll only see on older hosts at this point. To get root, I’ll find a cron job that calls another script that I can write. ~0xdf

### Skill-set:
1. SSL Certificate Inspection
2. Login Bypass - SQLI
3. SQLI (Blind Time Based) [Python Scripting]
4. Abusing preg_replace (REGEX Danger) [RCE]
5. Creating an AutoPwn script for Intrusion [Python Scripting]
6. Abusing Cron Job [Privilege Escalation]
