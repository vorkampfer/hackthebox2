# HTB Zipping
# Linux
# Difficulty: Medium

# Note: Corrupting the zip file to trick the server into accepting a cmd.php malicious file, and the symbolic-link fukery was great on this box. The (.so) file exploitation had me confused for a minute. I had to find a differently written payload to pull off the privesc.

### Synopsis:
Zipping has a website with a function to upload resumes as PDF documents in a Zip archive. I’ll abuse this by putting symlinks into the zip and reading back files from the host file system. I’ll get the source for the site and find a filter bypass that allows SQL injection in another part of the site. I’ll use that injection to write a webshell, and include it exploiting a LFI vulnerability to get execution. For root, I’ll abuse a custom binary with a malicious shared object. In Beyond Root, I’ll show two unintended foothold paths. The first arises from the differences between how PHP and 7z handle a file in a zip with a null byte in its name. The second uses the PHAR PHP filter to bypass the file_exists check and execute a webshell from an archive. ~0xdf

### Skill-set:
1. File uploading abuse (%00 Injection) [Failed]
2. ZipSlip Exploitation Technique for internal reading of files
3. SQL Injection + Regular Expression Bypass (%0a) + RCE through into outfile instruction
4. Custom binary abuse + Malicious Shared Object (.so) Injection [Privilege Escalation]
