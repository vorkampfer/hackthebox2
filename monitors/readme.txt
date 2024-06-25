# HTB Monitors
# Linux
# Difficulty: Hard

### Synopsis:
Monitors starts off with a WordPress blog that is vulnerable to a local file include vulnerability that allows me to read files from system. In doing so, I’ll discover another virtual host serving a vulnerable version of Cacti, which I’ll exploit via SQL injection that leads to code execution. From there, I’ll identify a new service in development running Apache Solr in a Docker container, and exploit that to get into the container. The container is running privilieged, which I’ll abuse by installing a malicious kernel module to get access as root on the host. ~0xdf

### Skill-set:
1. Information Leakage
2. WordPress Plugin Exploitation (Spritz)
3. Local File Inclusion (LFI)
4. Cacti 1.2.12 Exploitation
5. Apache OfBiz Deserialization Attack (RCE)
6. Docker Breakout(cap_sys_module Capability) [Privilege Escalation]
