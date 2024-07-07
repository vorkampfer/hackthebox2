# HTB Enterprise
# Linux
# Difficulty: Medium -> but more like a hard or insane

## NOTE: This is a long box with some good twists and turns. The SQLi and buffer-flow was great learning for me.

### Synopsis:
To own Enterprise, I’ll have to work through different containers to eventually reach the host system. The WordPress instance has a plugin with available source and a SQL injection vulnerability. I’ll use that to leak creds from a draft post, and get access to the WordPress instance. I can use that to get RCE on that container, but there isn’t much else there. I can also use those passwords to access the admin panel of the Joomla container, where I can then get RCE and a shell. I’ll find a directory mounted into that container that allows me to write a webshell on the host, and get RCE and a shell there. To privesc, I’ll exploit a service with a simple buffer overflow using return to libc. In Beyond Root, I’ll dig more into the Double Query Error-based SQLI. ~0xdf

### Skill-set:
1. Wordpress Lcars Plugin SQLi Vulnerability
2. SQL Injection (boolean-base blind, error-based, time-based blind)
3. Wordpress Exploitation [www-data] (Theme Edition - 404.php Template)
4. Joomla Exploitation [www-data] (Template Manipulation)
5. Docker Breakout
6. Ghidra Binary Analysis
7. Buffer Overflow (no ASLR - Pie enabled)[RET2LIBC] (Privilege Escalation)
