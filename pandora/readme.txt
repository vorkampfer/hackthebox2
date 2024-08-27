# HTB Pandora
# OS: Linux
# Difficulty: Easy

### Synopsis:
Pandora starts off with some SNMP enumeration to find a username and password that can be used to get a shell. This provides access to a Pandora FMS system on localhost, which has multiple vulnerabilities. I’ll exploit a SQL injection to read the database and get session cookies. I can exploit that same page to get admin and upload a webshell, or exploit another command injection CVE to get execution. To get root, there’s a simple path hijack in a SUID binary, but I will have to switch to SSH access, as there’s a sandbox in an Apache module preventing my running SUID as root while a descendant process of Apache. I’ll explore that in depth in Beyond Root. ~0xdf

### Skill-set:
1. SNMP Fast Enumeration
2. Information Leakage
3. Local Port Forwarding
4. SQL Injection - Admin Session Hijacking
5. PandoraFM v7.0NG Authenticated Remote Code Execution [CVE-2019-20224]
6. Abusing Custom Binary - PATH Hijacking [Privilege Escalation]
