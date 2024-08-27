# HTB Codify
# OS: Linux
# Difficulty: Easy

### Synopsis:
	The website on Codify offers a JavaScript playground using the vm2 sandbox. I’ll abuse four different CVEs in vm2 to escape and run command on the host system, using that to get a reverse shell. Then I’ll find a hash in a sqlite database and crack it to get the next user. For root, I’ll abuse a script responsible for backup of the database. I’ll show two ways to exploit this script by abusing a Bash glob in an unquoted variable compare. ~0xdf
