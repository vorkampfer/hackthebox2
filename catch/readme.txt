# HTB Catch
# Linux
# Difficulty: Medium

### Synopsis:
Catch requires finding an API token in an Android application, and using that to leak credentials from a chat server. Those credentials provide access to multiple CVEs in a Cachet instance, providing several different paths to a shell. The intended and most interesting is to inject into a configuration file, setting my host as the redis server, and storing a malicious serialized PHP object in that server to get execution. To escalate to root, I’ll abuse a command injection vulnerability in a Bash script that is checking APK files by giving an application a malicious name field. ~0xdf

### Skill-set:
1. APK Analysis [apktool, d2-dex2jar]
2. JD-GUI - Code Inspection
3. Information Leakage - Visible Token Values
4. Cachet Framework Exploitation - SQLI
5. Lets Chat Exploitation - Abusing API (Reading Private Messages)
6. Cachet Framework Exploitation - Server Side Template Injection (SSTI) [RCE]
7. Abusing Cron Job [Privilege Escalation]
