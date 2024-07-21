# HTB Drive
# Linux
# Difficulty: Hard

### Note: I had a difficult time on this box in the Privilege Escalation mostly. I just went through the motions. I really did not understand how the exploit of the sqlite3 database worked. Overall great box. The subject of sqlite exploitation is important because it is the database that is on almost every device and computer today.

### Synopsis:
Drive has a website that provides cloud storage. I’ll abuse an IDOR vulnerability to get access to the administrator’s files and leak some creds providing SSH access. From there I’ll access a Gitea instance and use the creds to get access to a backup script and the password for site backups. In these backups, I’ll find hashes for another use and crack them to get their password. For root, there’s a command line client binary that has a buffer overflow. I’ll show that, as well as two ways to get RCE via an unintended SQL injection. ~0xdf

### Skill-set:
1. IDOR Exploitation + OOP Python Scripting
2. Information Leakage
3. Sqlite3 file enumeration
4. Cracking hashes
5. Gitea Enumeration + Information Leakage
6. Abusing Custom Binary
7. Binary Analysis with Ghidra
8. Exploiting SUID binary
9. Command injection through sqlite3 extension loading [Privilege Escalation]
