# HTB Perfection
### OS: Linux
### Difficulty: Easy

### NOTE: Probrably the easiest privilege escalation I have ever done on HTB.

### Synopsis:
Perfection starts with a simple website designed to calculate weighted averages of grades. There is a filter checking input, which I’ll bypass using a newline injection. Then I can exploit a Ruby server-side template injection to get execution. I’ll find a database of hashes and a hint as to the password format used internally, and use hashcat rules to crack them to get root access. In Beyond Root, I’ll look at the Ruby webserver and the SSTI vulnerability.~0xdf

### Skill-set:
1. Ruby SSTI via burpsuite.
2. Exfiltrate sqlite3 db passwords
3. Find the hash mode for cracking with hashcat using bruteforce `-a 3`
4. sudo -l reveals susan has ALL in sudoers.
