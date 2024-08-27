# HTB Union
# OS: Linux
# Difficulty: Medium

### Synopsis:
The November Ultimate Hacking Championship qualifier box is Union. There’s a tricky-to-find union SQL injection that will allow for file reads, which leaks the users on the box as well as the password for the database. Those combine to get SSH access. Once on the box, I’ll notice that www-data is modifying the firewall, which is a privileged action, using sudo. Analysis of the page source shows it is command injectable via the X-Forwarded-For header, which provides a shell as www-data. This account has full sudo rights, providing root access. ~0xdf

### Skill-set:
1. SQLI - UNION injections
2. SQLI - Read Files
3. HTTP Header Command Injection X-FORWARDED-FOR [RCE]
4. Abusing sudoers privilege [Privilege Escalation]
