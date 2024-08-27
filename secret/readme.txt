# HTB Secret
# OS: Linux
# Difficulty: Easy

### Synopsis:
To get a foothold on Secret, I’ll start with source code analysis in a Git repository to identify how authentication works and find the JWT signing secret. With that secret, I’ll get access to the admin functions, one of which is vulnerable to command injection, and use this to get a shell. To get to root, I’ll abuse a SUID file in two different ways. The first is to get read access to files using the open file descriptors. The alternative path is to crash the program and read the content from the crashdump. ~0xdf

### Skill-set:
1. Code Analysis
2. Abusing an API
3. JSON Web Tokens (JWT) manipulation
4. Abusing/Leveraging Core Dump to gain root [Privilige Escalation]
