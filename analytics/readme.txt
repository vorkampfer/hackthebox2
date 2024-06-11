# HTB Analytics
# Linux
# Easy

### Note: Scripting the little port_scanner.sh was fun. This is a very easy box imo. I realize proxying the exploit through burpsuite was not even necessary. The metabase exploit worked great and so did the GameOverlayFS exploit. Fun simple box with some good enumeration practice and some bash scripting.

### Synopsis:
Analytics starts with a webserver hosting an instance of Metabase. There’s a pre-auth RCE exploit that involves leaking a setup token and using it to start the server setup, injecting into the configuration to get code execution. Inside the Metabase container, I’ll find creds in environment variables, and use them to get access to the host. From there I’ll exploit the GameOver(lay) vulnerability to get a shell as root, and include a video explaining the exploit. ~0xdf

### Skill-set:
1. Sudomain Enumeration
2. Metabase Exploitation (CVE-2023-38646)
3. Docker Container Information Leakage
4. Kernel Exploitation - GamerOver(lay)/Abusing OverlayFS [Privilege Escalation]
