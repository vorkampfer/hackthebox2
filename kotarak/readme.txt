# HTB Kotarak
### OS: Linux
### Difficulty: Hard

### Synopsis:
Kotarak was an old box that I had a really fun time replaying for a writeup. It starts with an SSRF that allows me to find additional webservers on ports only listening on localhost. I’ll use that to leak a Tomcat config with username and password, and upload a malicious war to get a shell. From there, I can access files from an old Windows pentest to include an ntds.dit file and a system hive. That’s enough to dump a bunch of hashes, one of which cracks and provides creds I can use to get the next user. The root flag is actually in a container that is using Wget to request a file every two minutes. It’s an old vulnerable version, and a really neat exploit that involves sending a redirect to an FTP server and using that to write a malicious config file in the root home directory in the container. I’ll also show an alternative root abusing the user’s disk group to exfil the entire root filesystem and grab the flag on my local system. ~0xdf

### Skill-set:
1. Server Side Request Forgery (SSRF) [Internal Port Discovery]
2. Information Leakage [Backup]
3. Tomcat Exploitatation [Malicious WAR file]
4. Dumping hashes [NTDS.dit]
5. wget 1.12 vulnerability [CVE-2016-4971] [Privilege Escalation]
