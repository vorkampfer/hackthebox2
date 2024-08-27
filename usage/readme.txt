# HTB Usage
# OS: Linux
# Difficulty: Easy

### Synopsis:
Usage starts with a blind SQL injection in a password reset form that I can use to dump the database and find the admin login. The admin panel is made with Laravel-Admin, which has a vulnerability in it that allows uploading a PHP webshell as a profile picture by changing the file extension after client-side validation. I’ll find a password in a monit config, and then abuse a wildcard vulnerability in 7z to get file read as root. ~0xdf

### Skill-set:
1. FUZZING for sub-domains
2. sqlmap blind injection
3. CVE-2023-24249 laravel-admin - Arbitrary File Upload vulnerability
4. Abusing poor coding practices, wildcard asterisk [Privilege Escalation]
