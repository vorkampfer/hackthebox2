# HTB MetaTwo
# OS: Linux
# Difficulty: Easy

### Synopsis:
MetaTwo starts with a simple WordPress blog using the BookingPress plugin to manage booking events. I’ll find an unauthenticated SQL injection in that plugin and use it to get access to the WP admin panel as an account that can manage media uploads. I’ll exploit an XML external entity (XXE) injection to read files from the host, reading the WP configuration, and getting the creds for the FTP server. On the FTP server I’ll find a script that is sending emails, and use the creds from that to get a shell on the host. The user has a Passpie instance that stores the root password. I’ll crack the PGP key protecting the password and get a shell as root. ~0xdf

### Skill-set:
1. Wordpress enumeration using various wordpress scanners
2. sqlmap (dumping hashes)
3. Hashcat cracking hash
4. Using gpg2john
5. Abusing passpie password generator
