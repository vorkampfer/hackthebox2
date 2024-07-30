# HTB Tabby
## OS: Linux
### Difficulty: Easy

Tabby was a well designed easy level box that required finding a local file include (LFI) in a website to leak the credentials for the Tomcat server on that same host. The user who’s creds I gain access to only has access to the command line manager API, not the GUI, but I can use that to upload a WAR file, get execution, and a shell. I’ll crack the password on a backup zip archive and then use that same password to change to the next user. That user is a member of the lxd group, which allows them to start containers. I’ve shown this root before, but this time I’ll include a really neat trick from m0noc that saves several steps. In Beyond Root, I’ll pull apart the WAR file and show what’s actually in it.~0xdf

### Skill-set:
1. Local File Inclusion (LFI) 
2. Abusing Tomcat Virtual Host Manager 
3. Abusing Tomcat Text-Based-Manager 
4. Deploy Malicious War (Curl Method) 
5. LXC Exploitation (Privilege Escalation)
