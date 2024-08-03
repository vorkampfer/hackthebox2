# HTB CozyHosting
# OS: Linux
# Difficulty: Easy

### Synopsis:
CozyHosting is a web hosting company with a website running on Java Spring Boot. I’ll find a Spring Boot Actuator path that leaks the session id of a logged in user, and use that to get access to the site. Once there, I’ll find command injection in a admin feature to get a foothold. I’ll pull database creds from the Java Jar file and use them to get the admin’s hash on the website from Postgres, which is also the user’s password on the box. From there, I’ll abuse sudo ssh with the ProxyCommand option to get root. ~0xdf

### Skill-set:
1. Seclist specialized wordlist for Spring-Boot
2. Spring-boot enumeration
3. Command injection when using burpsuite to manually fuzz the connection settings parameter on the `/admin` page.
4. Jar file enumertion
5. PostgreSQL database enumeration. Dump hashes
6. Abusing sudoers privilege to get root 
