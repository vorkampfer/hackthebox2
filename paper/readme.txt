# HTB Paper
# Linux 
# Difficulty: Easy

### NOTE:
Paper was a fun box. I enjoyed rooting this box.

### Synopsis:
Paper is a fun easy-rated box themed off characters from the TV show “The Office”. There’s a WordPress vulnerability that allows reading draft posts. In a draft post, I’ll find the URL to register accounts on a Rocket Chat instance. Inside the chat, there’s a bot that can read files. I’ll exploit a directory traversal to read outside the current directory, and find a password that can be used to access the system. To escalate from there, I’ll exploit a 2021 CVE in PolKit. In Beyond Root, I’ll look at a later CVE in Polkit, Pwnkit, and show why Paper wasn’t vulnerable, make it vulnerable, and exploit it. ~0xdf

### Skill-set:
1. Information Leakage
2. Abusing WordPress - Unauthenticated View Private/Draft Posts
3. Abusing Rocket Chat Bot
4. Polkit(CVE-2021-3560)[Privilege Escalation]
