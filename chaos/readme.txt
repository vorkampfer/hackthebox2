# HTB CHAOS
# Linux
# Difficulty: Medium

### Synopsis:
Choas provided a couple interesting aspects that I had not worked with before. After some web enumeration and password guessing, I found myself with webmail credentials, which I could use on a webmail domain or over IMAP to get access to the mailbox. In the mailbox was an encrypted message, that once broken, directed me to a secret url where I could exploit an instance of pdfTeX to get a shell. From there, I used a shared password to switch to another user, performed an restricted shell escape, and found the root password in the user’s firefox saved passwords. That password was actually for a Webmin instance, which I’ll exploit in Beyond Root. ~0xdf

### Skill-set:
1. Password Guessing
2. Abusing e-mail service (claws-mail)
3. Crpyto Challenge (Decrypt Secret Message - AES Encrypted)
4. LaTeX injection [RCE]
5. Bypassing rbash (Restriced Bash)
6. Extracting Credentials from Firefox Profile
