# HTB iClean
# OS: Linux
# Difficulty: Medium

### Synopsis:
IClean starts out with a simple cross-site scripting cookie theft, followed by exploiting a server-side template injection in an admin workflow. I’ll abuse that to get a shell on the box, and pivot to the next user by getting their hash from the website DB and cracking it. For root, the user can run the a command-line PDF software as root. I’ll use that to attach files to PDF documents for file read as well. In Beyond Root, I’ll go through the structure of the PDF documents and use tools to pull the attachments out without opening the document. ~0xdf

### Skill-set:
1. Enumeration finding out the server is running Python with flask framework
2. Stealing admin session cookie.
3. Generating an Invoice and finding an SSTI
4. MySQL enumeration [Dumping hashes]
5. Abusing qpdf add attachment feature because of sudoers ALL privilege [Privilege Escalation]
