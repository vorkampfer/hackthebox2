# HTB Curling
# Linux
# Difficulty: Easy
### Note: Abusing the -K feature on Curl to overwrite the PASSWD file was fun.

### Synopsis:
Curling was a solid box easy box that provides a chance to practice some basic enumeration to find a password, using that password to get access to a Joomla instance, and using the access to get a shell. With a shell, I’ll find a compressed and encoded backup file, that after a bit of unpacking, gives a password to privesc to the next user. As that user, I’ll find a root cron running curl with the option to use a configuration file. It happens that I can control that file, and use it to get the root flag and a root shell. In Beyond root, I’ll look at how setuid applies to scripts on most Linux flavors (and how it’s different from Solaris as I showed with Sunday), and how the Dirty Sock snapd vulnerability from a couple months ago will work here to go to root. ~0xdf

### Skill-set:
1. Information Leakage wtf xd
2. Joomla Enumeration
3. Joomla Exploitation [Abusing Templates] [RCE]
4. Decompression Challenge
5. Abusing Curl [Playing with config files] [Privilege Escalation]
